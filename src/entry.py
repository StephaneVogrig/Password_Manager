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

	def to_dict(self) -> dict:
		return {
			"id": self.id,
			"site_name": self.site_name,
			"site_url": self.site_url,
			"identifiant": self.identifiant,
			"password": self.password,
			"email": self.email,
			"notes": self.notes,
			"otherdata": self.otherdata,
			"created_at": self.created_at.isoformat(),
			"updated_at": self.updated_at.isoformat(),
		}
	@staticmethod
	def from_dict(d: dict) -> "Entry":
		return Entry(
			id=d["id"],
			site_name=d.get("site_name", ""),
			site_url=d.get("site_url", ""),
			identifiant=d.get("identifiant", ""),
			password=d.get("password", ""),
			email=d.get("email", ""),
			notes=d.get("notes", ""),
			otherdata=d.get("otherdata", {}),
			created_at=datetime.fromisoformat(d["created_at"]),
			updated_at=datetime.fromisoformat(d["updated_at"])
		)
