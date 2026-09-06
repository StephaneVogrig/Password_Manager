from pathlib import Path

class App:
    def __init__(self, filepath: str |None):
        self.sites = self.load(filepath) if filepath else {}

    def load(self, filepath: str) -> dict:
        vault_path = Path(path)
        if not vault_path.exists():
            raise FileNotFoundError(f"Le fichier '{path} n'existe pas.")

