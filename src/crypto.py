import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet, InvalidToken

SALT_SIZE = 16
KDF_ITERATIONS = 300000
KEY_LENGTH = 32

class CryptoError(Exception):
	pass

def _derive_key(password: str, salt: bytes) -> bytes:
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=KEY_LENGTH,
		salt=salt,
		iterations=KDF_ITERATIONS,
	)
	key =kdf.derive(password.encode())
	return  base64.urlsafe_b64encode(key)

def encrypt_bytes(data: bytes, master_password: str) -> bytes:
	salt = os.urandom(SALT_SIZE)
	key = _derive_key(master_password, salt)
	cipher = Fernet(key)
	encrypted = cipher.encrypt(data)
	encrypted_data = salt + encrypted
	return encrypted_data

def decrypt_bytes(encrypted_data: bytes, master_password: str) ->bytes:
	try:
		salt = encrypted_data[:SALT_SIZE]
		encrypted = encrypted_data[SALT_SIZE:]
		key = _derive_key(master_password, salt)
		cipher = Fernet(key)
		data = cipher.decrypt(encrypted)
		return data
	except InvalidToken:
		raise CryptoError("Mot de passe incorrect ou donnees corrompue")
	except Exception as error:
		raise CryptoError(f"Erreur inattendue lors du dechiffrement: {str(error)}")

def encrypt_str_to_bytes(string: str, master_password: str) -> bytes:
	data = string.encode('utf-8')
	return encrypt_bytes(data, master_password)

def decrypt_bytes_to_str(encrypted_data: bytes, master_password: str) -> str:
	data = decrypt_bytes(encrypted_data, master_password)
	string = data.decode('utf-8')
	return string
