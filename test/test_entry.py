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
    e = Entry(
        site_name="GitHub",
        site_url="https://github.com",
        identifiant="john",
        password="secret",
        email="john@example.com",
        notes="Mon compte dev"
    )

    assert e.site_name == "GitHub"
    assert e.site_url == "https://github.com"
    assert e.identifiant == "john"
    assert e.password == "secret"
    assert e.email == "john@example.com"
    assert e.notes == "Mon compte dev"
