from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Entry:
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	site_name: str = ""
	site_url: str = ""
	identifiant: str = ""
	password: str = ""
	email: str = ""
	notes: str = ""
	otherdata: dict = field(default_factory=dict)
	created_at: datetime = field(default_factory=datetime.now)
	updated_at: datetime = field(default_factory=datetime.now)
