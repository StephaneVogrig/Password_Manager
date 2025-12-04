from src.entry import Entry
from datetime import datetime, timezone

def test_entry_default_values():
    e = Entry()

    assert isinstance(e.id, str)
    assert e.site_name == ""
    assert e.site_url == ""
    assert e.identifiant == ""
    assert e.password == ""
    assert e.email == ""
    assert e.notes == ""
    assert isinstance(e.otherdata, dict)

    assert isinstance(e.created_at, datetime)
    assert isinstance(e.updated_at, datetime)

def test_entry_custom_values():
    entry = Entry(
        site_name="GitHub",
        site_url="https://github.com",
        identifiant="john",
        password="secret",
        email="john@example.com",
        notes="Mon compte dev"
    )

    assert entry.site_name == "GitHub"
    assert entry.site_url == "https://github.com"
    assert entry.identifiant == "john"
    assert entry.password == "secret"
    assert entry.email == "john@example.com"
    assert entry.notes == "Mon compte dev"

def test_entry_to_dict_and_back():
    entry = Entry(
        site_name="GitHub",
        site_url="https://github.com",
        identifiant="john",
        password="secret",
        email="john@example.com",
        notes="Mon compte dev",
        otherdata={"tag": "dev"}
    )

    d = entry.to_dict()
    restored = Entry.from_dict(d)

    assert restored.id == entry.id
    assert restored.site_name == entry.site_name
    assert restored.site_url == entry.site_url
    assert restored.identifiant == entry.identifiant
    assert restored.password == entry.password
    assert restored.email == entry.email
    assert restored.notes == entry.notes
    assert restored.otherdata == entry.otherdata

    assert isinstance(restored.created_at, datetime)
    assert isinstance(restored.updated_at, datetime)
    