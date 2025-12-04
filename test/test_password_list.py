from src.entry import Entry
from src.password_list import PasswordList

def test_add_and_get_entry():
	password_list = PasswordList()
	entry = Entry(site_name="GitHub", identifiant="john")
	password_list.add(entry)
	result = password_list.get(entry.id)
	assert result == entry

def test_get_unknown_entry_returns_none():
    password_list = PasswordList()
    assert password_list.get("does-not-exist") is None

def test_remove_entry():
	password_list = PasswordList()
	entry = Entry(site_name="Github", identifiant="john")
	password_list.add(entry)
	password_list.remove(entry.id)
	assert password_list.get(entry.id) is None

def test_remove_unknown_entry():
	password_list = PasswordList()
	password_list.remove("unknown")
	assert password_list.entries == {}

def test_update_entry():
	password_list = PasswordList()
	entry = Entry(site_name="GitHub", identifiant="john")
	password_list.add(entry)
	old_updated_at = entry.updated_at

	updated_entry = Entry(
		id=entry.id,
		site_name="GitHub",
		identifiant="johnny",
		password = "new",
		email ="new@mail.com"
	)
	password_list.update(updated_entry)
	result = password_list.get(entry.id)

	assert result.identifiant == "johnny"
	assert result.site_name == "GitHub"
	assert result.identifiant == "johnny"
	assert result.password == "new"
	assert result.email == "new@mail.com"
	assert result.updated_at >= old_updated_at

def test_update_unknown_entry():
	password_list = PasswordList()
	entry = Entry(site_name="GitHub", identifiant="john")

	# ne doit pas generer d'erreurs
	password_list.update(entry)

	assert password_list.get(entry.id) is None
