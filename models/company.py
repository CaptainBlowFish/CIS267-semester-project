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
