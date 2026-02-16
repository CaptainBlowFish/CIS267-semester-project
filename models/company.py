#  Jacob Milham
#  CIS 267
#  Spring 2026
from .batch import Batch
from .user import User


class Company:
    def __init__(self, name: str, description: str, active: bool) -> None:
        self.name = name
        self.description = description
        self.batches = []
        self.active = active
        for i in range(5):
            self.batches.append(Batch("F"+str(i), "10/30/2026"))
        self.users = []
        for i in range(5):
            self.users.append(User())

    def __str__(self) -> str:
        desc_str = f"Name: {self.name} \nDescription: {self.description} \n \
        Is active: {self.active}"
        desc_str += "Batches:"

        for i in self.batches:
            desc_str += str(i)

        for i in self.users:
            desc_str += str(i)
        return desc_str
