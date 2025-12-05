import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken

class Crypto:

	@staticmethod
	def _derive_key(password:str, salt:bytes) -> bytes:
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=100000,
			backend=default_backend()
		)
		key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
		return key

	@staticmethod
	def encrypt(plaintext: str, master_password:str) -> str:
		salt = os.urandom(16)
		key = Crypto._derive_key(master_password, salt)
		cipher = Fernet(key)
		encrypted = cipher.encrypt(plaintext.encode())
		combined = salt + encrypted
		return base64.urlsafe_b64encode(combined).decode()

	@staticmethod
	def decrypt(encrypted_data: str, master_password:str) ->str:
		try:
			combined = base64.urlsafe_b64decode(encrypted_data.encode())
			salt = combined[:16]
			encrypted = combined[16:]
			key = Crypto._derive_key(master_password, salt)
			cipher = Fernet(key)
			decrypted = cipher.decrypt(encrypted)
			return decrypted.decode()

		except InvalidaToken:
			raise Exception("Mot de passe incorrect ou donnees corrompue")
		except Exception as error:
			raise Exception(f"Erreur lors du dechiffrement: {str(error)}")
