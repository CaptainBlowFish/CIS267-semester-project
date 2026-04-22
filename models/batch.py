#  Jacob Milham
#  CIS 267
#  Spring 2026
from datetime import datetime


def _merge(arr, left: int, middle: int, right: int) -> None:
    n1 = middle - left + 1
    n2 = right - middle

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[middle + 1 + j]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def _mergeSort(arr: list, left: int, right: int) -> None:
    if left < right:
        middle = left + (right - left) // 2
        _mergeSort(arr, left, middle)
        _mergeSort(arr, middle + 1, right)
        _merge(arr, left, middle, right)


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
        if self.first_node is None:
            self.first_node = Node(data)
        else:
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

    def traverse(self) -> list:
        return_list = []
        temp = self.first_node
        while temp is not None:
            return_list.append(temp.data)
            temp = temp.next

        return return_list

    def sort(self) -> None:
        data = self.traverse()
        _mergeSort(data, 0, len(data) - 1)

        self.first_node = Node(data[0])
        current_node = self.first_node
        for i in data[1::]:
            current_node.next = Node(i)
            current_node = current_node.next


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

    def insert(self, record_data, record_ID) -> None:
        self.records.insert(record_data, record_ID)

    def del_front(self) -> None:
        self.records.del_front()

    def del_back(self) -> None:
        self.records.del_back()

    def del_at(self, record_ID) -> None:
        self.records.del_at(record_ID)

    def find_record(self, record_ID) -> None:
        return self.records.find(record_ID)

    def sort_records(self) -> None:
        self.records.sort()

    def __eq__(self, other) -> bool:
        return self.date == other.date

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        return self.date < other.date

    def __gt__(self, other) -> bool:
        return self.date > other.date

    def __ge__(self, other) -> bool:
        return self.__gt__(other) and self.__ge__(other)


if __name__ == "__main__":
    ll = LinkedList()
    for i in [1, 3, 4, 5, 2, 3, 4, 2, 5, 7, 10, 2]:
        ll.append(i)
    print("unsorted linked list")
    print(ll.traverse())
    print("sorted")
    ll.sort()
    print(ll.traverse())
