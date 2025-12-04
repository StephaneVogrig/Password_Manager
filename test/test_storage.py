from src.storage import Storage
from src.entry import Entry
from src.password_list import PasswordList

def test_storage_save_and_load(tmp_path):
	entry = Entry(site_name="GitHub", identifiant="bob")
	pass_list = PasswordList()
	pass_list.add(entry)
	file = tmp_path / "data.json"

	Storage.save(pass_list, file)

	assert file.exists()

	content = file.read_text()

	assert entry.site_name in content
	assert entry.identifiant in content

	restored = Storage.load(file)

	assert restored.get(entry.id) == entry
