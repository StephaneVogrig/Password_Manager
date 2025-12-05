from src.crypto import encrypt_str_to_bytes, decrypt_bytes_to_str
import pytest

def test_encrypt_and_decrypt():
	master_password ="my_secure_password"
	data = "sensitive data"
	encrypted = encrypt_str_to_bytes(data, master_password)
	assert encrypted != data
	assert isinstance(encrypted, bytes)
	decrypted = decrypt_bytes_to_str(encrypted, master_password)
	assert decrypted == data

def test_encrypt_and_decrypt_wrong_password():
	master_password ="my_secure_password"
	wrong_password = "wrong_password"
	data = "sensitive data"
	encrypted = encrypt_str_to_bytes(data, master_password)
	with pytest.raises(Exception):
		decrypted = decrypt_bytes_to_str(encrypted, wrong_password)
