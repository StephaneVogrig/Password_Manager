import json
from src.password_list import PasswordList

class Storage:
    @staticmethod
    def save(password_list: PasswordList, path):
        with open(path, "w") as file:
            json.dump(password_list.to_list(),file)

    @staticmethod
    def load(path):
        with open(path,"r") as file:
            data = json.load(file)
        return PasswordList.from_list(data)
