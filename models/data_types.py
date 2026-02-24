#  Jacob Milham
#  CIS 267
#  Spring 2026
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.first_node: Node = None
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
            ID -=1
            temp = temp.next

            if temp.data is None:
                print("ID Does not exist.")
        temp.next = Node(data, temp.next)
        self.__length += 1

    def del_front(self):
        """deletes the node at the first position of the linked list."""
        if self.first_node is not None:
            self.first_node = self.first_node.next
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
            ID -=1
            prev = curr
            curr = curr.next

            if curr.data is None:
                print("ID Does not exist.")
        prev.next = curr.next
        self.__length -= 1

    def find(self, ID):
        """finds and returns the node at the ID given from the linked list.
         returns None if it does not exist"""
        curr = self.first_node
        while 0 < ID:
            ID -=1
            if curr.data is None:
                return None
            curr = curr.next
        return curr.data


class Queue:
    def __init__(self) -> None:
        self.__head: Node = None
        self.__tail: Node = None
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
        self.__head = self.__head.next
        self.__length -= 1
        return temp

    def peek(self):
        return self.__head.data


if __name__ == "__main__":
    ("________Linked_list_______")
    ll = LinkedList()
    for i in range(5, 0, -1):
        ll.prepend(i)

    for i in range(6, 10):
        ll.append(i)

    ll.insert(99, 5)
    print(ll)
    ll.del_front()
    print(ll)
    ll.del_back()
    print(ll)
    ll.del_at(4)
    print(ll)
    
    ("________Queue____________")
    queue = Queue()
    for i in range(0, 10):
        queue.enqueue(i)
    print(queue)

