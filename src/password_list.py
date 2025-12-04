from src.entry import Entry
from datetime import datetime

class PasswordList:
	def __init__(self):
		self.entries = {}

	def add(self, entry: Entry):
		self.entries[entry.id] = entry

	def get(self, entry_id: str):
		return self.entries.get(entry_id)

	def remove(self, entry_id: str):
		if entry_id in self.entries:
			del self.entries[entry_id]

	def update(self, entry: Entry):
		if entry.id in self.entries:
			entry.updated_at = datetime.now().replace(microsecond=0)
			self.entries[entry.id] = entry

	def to_list(self) -> list:
		return [entry.to_dict() for entry in self.entries.values()]

	@staticmethod
	def from_list(list_dict):
		password_list = PasswordList()
		for entry_dict in list_dict:
			entry = Entry.from_dict(entry_dict)
			password_list.add(entry)
		return password_list
