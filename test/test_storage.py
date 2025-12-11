import json
import pytest
from pathlib import Path
from src.password_list import PasswordList
from src.entry import Entry
from src.storage import Storage, StorageError

def test_storage_save_and_load_no_password(tmp_path) -> None:
	entry = Entry(site_name="GitHub", identifiant="bob", password="mot de passe")
	pass_list = PasswordList()
	pass_list.add(entry)
	file = Path(tmp_path / "data.json")
	vault = Storage(path=file, password=None)

	vault.save(pass_list)
	assert file.exists()

	content = file.read_text()
	assert entry.site_name in content
	assert entry.identifiant in content

	data_loaded = json.loads(content)
	assert len(data_loaded) == 1

	restored_list = vault.load()
	assert restored_list is not None
	
	restored_entry = restored_list.get(entry.id)
	assert restored_entry is not None
	assert restored_entry.site_name == entry.site_name
	assert restored_entry.identifiant == entry.identifiant
	assert restored_entry.password == entry.password

def test_storage_save_and_load_password(tmp_path) -> None:
	entry = Entry(site_name="GitHub", identifiant="bob", password="mot de passe")
	pass_list = PasswordList()
	pass_list.add(entry)
	file = Path(tmp_path / "data.json")
	master_password = "un super mot de passe de la mort qui tue"
	vault = Storage(path=file, password=master_password)

	vault.save(pass_list)
	assert file.exists()

	content = file.read_bytes()
	assert b"GitHub" not in content
	assert b"bob" not in content
	assert b"mot de passe" not in content

	restored_list = vault.load()
	assert restored_list is not None
	
	restored_entry = restored_list.get(entry.id)
	assert restored_entry is not None
	assert restored_entry.site_name == entry.site_name
	assert restored_entry.identifiant == entry.identifiant
	assert restored_entry.password == entry.password

def test_load_wrong_password(tmp_path) -> None:
	entry = Entry(site_name="GitHub", identifiant="bob", password="mot de passe")
	pass_list = PasswordList()
	pass_list.add(entry)
	file = Path(tmp_path / "data.json")
	master_password = "un super mot de passe de la mort qui tue"
	vault = Storage(path=file, password=master_password)
	vault.save(pass_list)

	vault_wrong = Storage(path=file, password="wrong_password")
	with pytest.raises(StorageError):
		vault_wrong.load()

def test_load_non_existent_file(tmp_path: Path) ->None:
	non_existent_file = Path(tmp_path / "vault_missing.dat")
	assert not non_existent_file.exists()

	vault = Storage(path=non_existent_file, password="test_password")
	with pytest.raises(FileNotFoundError):
		restored_list = vault.load()
