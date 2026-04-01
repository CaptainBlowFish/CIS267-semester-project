#  Jacob Milham
#  CIS 267
#  Spring 2026
from batch import Batch
from user import User
from datetime import datetime
import random


def _binary_search(arr: list, val, start: int, end: int):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return _binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return _binary_search(arr, val, start, mid - 1)
    else:
        return mid


class Company:
    def __init__(self, name: str, description: str, active: bool) -> None:
        self.name = name
        self.description = description
        self.__batches = []
        self.active = active
        for i in range(5):
            self.__batches.append(Batch("F"+str(i),
                                      datetime(2026,
                                               3,
                                               random.randint(1, 31))))
        self.users = []
        for i in range(5):
            self.users.append(User())

    def __str__(self) -> str:
        desc_str = f"Name: {self.name} \nDescription: {self.description} \n \
        Is active: {self.active}"
        desc_str += "Batches:"

        for i in self.__batches:
            desc_str += str(i)

        for i in self.users:
            desc_str += str(i)
        return desc_str

    def add_batch(self, b: Batch):
        self.__batches.insert(_binary_search(self.__batches,
                                             b,
                                             0,
                                             len(self.__batches)),
                              b)


if __name__ == "__main__":
    l = [random.randint(0, 10) for i in range(10)]
    j = []
    print("unsorted:")
    print(l)

    for i in l:
        j.insert(_binary_search(j, i, 0, len(j)-1), i)
    print("sorted")
    print(j)
