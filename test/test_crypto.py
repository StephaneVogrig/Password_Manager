from src.crypto import Crypto

def test_encrypt_and_decrypt():
	master_password ="my_secure_password"
	plaintext = "sensitive datat"

	encrypted = Crypto.encrypt(plaintext, master_password)

	assert encrypted != plaintext
	assert isinstance(encrypted, str)

	decrypted = Crypto.decrypt(encrypted, master_password)
	assert decrypted == plaintext
