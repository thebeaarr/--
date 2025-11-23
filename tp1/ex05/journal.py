from datetime import datetime

class JournalTaches:
	def __enter__(self):
		self.journal = open("journal.txt", "a", encoding="utf-8")
		return self

	def enregistrer(self, tache: str):
		timestamp = datetime.now().isoformat()
		self.journal.write(f"{tache} - {timestamp}\n")

	def __exit__(self, exc_type, exc, tb):
		self.journal.close()
