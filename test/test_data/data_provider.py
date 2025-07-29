import json


my_data = open('test_data/test_data.json')
global_data = json.load(my_data)


class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get(self, property: str) -> str:
        return self.data.get(property)

    def getint(self, property: str) -> int:
        return int(self.data.get(property))

    def get_email(self) -> str:
        return self.data.get("email")

    def get_password(self) -> str:
        return self.data.get("password")

    