#  Jacob Milham
#  CIS 267
#  Spring 2026
from datetime import datetime


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data}"


class Queue:
    def __init__(self) -> None:
        self.__head: Node = None  # type: ignore
        self.__tail: Node = None  # type: ignore
        self.__length: int = 0

    def __str__(self) -> str:
        desc_str = f"length={self.__length}\nqueue position : data\n"
        temp = self.__head
        count = 0
        while temp is not None:
            if temp == self.__head:
                desc_str += f"Head: {temp.data}\n"
            elif temp == self.__tail:
                desc_str += f"Tail: {temp.data}\n"
            else:
                desc_str += f"{count} : {temp.data}\n"
            count += 1
            temp = temp.next
        return desc_str

    def get_length(self) -> int:
        return self.__length

    def enqueue(self, data):
        if self.__head is None:
            self.__head = Node(data)
            self.__tail = self.__head
        else:
            self.__tail.next = Node(data)
            self.__tail = self.__tail.next
        self.__length += 1

    def dequeue(self):
        temp = self.__head.data
        self.__head = self.__head.next  # type: ignore
        self.__length -= 1
        return temp

    def peek(self):
        return self.__head.data


class FutureAction:
    def __init__(self, action: str, arguments=[]) -> None:
        self.action = action
        self.arguments = arguments


class BatchInfo:
    def __init__(self, file_name, date: datetime) -> None:
        self.file_name = file_name
        self.date = date
        self.actions = Queue()

    def enqueue_action(self, action: str, arguments=[]):
        self.actions.enqueue(FutureAction(action, arguments))

    def dequeue_action(self) -> FutureAction:
        return self.actions.dequeue()


class QueuedBatch:
    def __init__(self) -> None:
        self.queue = Queue()

    def enqueue_batch(self, file_name, date: datetime) -> None:
        self.queue.enqueue(BatchInfo(file_name, date))

    def dequeue_batch(self) -> BatchInfo:
        return self.queue.dequeue()
