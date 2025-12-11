import json
from typing import Optional
from pathlib import Path
from src.password_list import PasswordList
from src.crypto import encrypt_str_to_bytes, decrypt_bytes_to_str, CryptoError

class StorageError(Exception):
    pass

class Storage:
    """
    Gestionnaire de stockage pour les listes de mots de passe.

    Permet de sauvegarder et charger des listes de mots de passe,
    avec chiffrement optionnel via un mot de passe maître.
    """
    def __init__(self, path: Path | str, password: Optional[str] = None) -> None:
        self.path = Path(path)
        self._password = password

    def save(self, password_list: PasswordList) -> None:
        """
        Sauvegarde la liste de mots de passe.
        
        Args:
            password_list: La liste à sauvegarder
        
        Raises:
            StorageError: Si la sauvegarde échoue
        """
        try:
            data = password_list.to_list()
            if self._password:
                data_json = json.dumps(data)
                data_encrypted = encrypt_str_to_bytes(data_json, self._password)
                with open(self.path, "wb") as file:
                    file.write(data_encrypted)
            else:
                with open(self.path, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=2)
        except CryptoError as error:
            raise StorageError(f"Erreur de chiffrement : {error}")
        except (IOError, OSError) as error:
            raise StorageError(f"Echec de la sauvegarde : {error}")

    def load(self) -> PasswordList:
        """
        Charge la liste de mots de passe depuis le fichier.

        Returns:
            La liste de mots de passe chargée

        Raises:
            FileNotFoundError: Si le fichier n'existe pas
            StorageError: Si le chargement échoue
        """
        if not self.path.exists():
            raise FileNotFoundError(f"Fichier de données introuvable : {self.path}")
        try:
            if self._password:
                with open(self.path, "rb") as file:
                    data_encrypted = file.read()
                    data = decrypt_bytes_to_str(data_encrypted, self._password)
                    data_json = json.loads(data)
            else:
                with open(self.path, "r", encoding="utf-8") as file:
                    data_json = json.load(file)
            return PasswordList.from_list(data_json)
        except json.JSONDecodeError:
            raise StorageError("Donnees corrompu : JSON invalide")
        except CryptoError as error:
            raise StorageError(f"Echec du déchiffrement : {error}")
        except (IOError, OSError) as error:
            raise StorageError(f"Echec du chargement : {error}")
