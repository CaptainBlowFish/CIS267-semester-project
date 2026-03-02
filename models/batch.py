#  Jacob Milham
#  CIS 267
#  Spring 2026
from datetime import datetime
import record


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.first_node: Node = None  # type: ignore
        self.__length = 0

    def __str__(self) -> str:
        desc_str = f"length={self.__length}\nlist position : data\n"
        temp = self.first_node
        count = 0
        while temp is not None:
            desc_str += f"{count} : {temp.data}\n"
            count += 1
            temp = temp.next
        return desc_str

    def get_len(self) -> int:
        return self.__length

    def prepend(self, data):
        """inserts a new node to the first position of the linked list."""
        self.first_node = Node(data, self.first_node)
        self.__length += 1

    def append(self, data):
        """adds a new node at the last position of the linked list."""
        temp = self.first_node
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)
        self.__length += 1

    def insert(self, data, ID):
        """Inserts a new node after the first node with the given ID."""
        temp: Node = self.first_node
        while 0 < ID:
            ID -= 1
            temp = temp.next  # type: ignore

            if temp.data is None:
                print("ID Does not exist.")
        temp.next = Node(data, temp.next)
        self.__length += 1

    def del_front(self):
        """deletes the node at the first position of the linked list."""
        if self.first_node is not None:
            self.first_node = self.first_node.next  # type: ignore
            self.__length -= 1

    def del_back(self):
        """deletes the node at the last position of the linked list."""
        curr = self.first_node
        prev = curr
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None
        del curr
        self.__length -= 1

    def del_at(self, ID):
        """deletes the node at the ID given from the linked list."""
        curr = self.first_node
        prev = curr
        while 0 < ID:
            ID -= 1
            prev = curr
            curr = curr.next  # type: ignore

            if curr.data is None:  # type: ignore
                print("ID Does not exist.")
        prev.next = curr.next  # type: ignore
        self.__length -= 1

    def find(self, ID):
        """finds and returns the node at the ID given from the linked list.
         returns None if it does not exist"""
        curr = self.first_node
        while 0 < ID:
            ID -= 1
            if curr.data is None:  # type: ignore
                return None
            curr = curr.next
        return curr.data  # type: ignore


class Batch:
    def __init__(self, file_name: str, date: datetime) -> None:
        self.file_name = file_name
        self.date = date
        self.records = LinkedList()

    def __str__(self) -> str:
        desc_str = f"file_name:{self.file_name}\ndate:{self.date}\n \
            records:{str(self.records)}"

        return desc_str

    def get_records_len(self) -> int:
        return self.records.get_len()

    def prepend(self, record_data) -> None:
        self.records.prepend(record_data)

    def append(self, record_data) -> None:
        self.records.append(record_data)

    def insert(self, record_data, record_ID):
        self.records.insert(record_data, record_ID)

    def del_front(self):
        self.records.del_front()

    def del_back(self):
        self.records.del_back()

    def del_at(self, record_ID):
        self.records.del_at(record_ID)

    def find_record(self, record_ID):
        return self.records.find(record_ID)
