#  Jacob Milham
#  CIS 267
#  Spring 2026
# Source - https://stackoverflow.com/a/16985066
# Posted by Aya, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-02, License - CC BY-SA 4.0

from datetime import datetime, date
import batch as b


class TreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        if self.left is None and self.right is None:
            return True
        return False


def inorder(root: TreeNode) -> list:
    """
    Returns the data of an ordered binary tree in order as a list
    """
    ret_list = []
    if root:
        for i in inorder(root.left):
            ret_list.append(i)
        ret_list.append(root.data)
        for i in inorder(root.right):
            ret_list.append(i)
    return ret_list


class BatchTree:
    def __init__(self, rootDate: datetime) -> None:
        self.node_count = 0
        self.root = (self.__new_node(self.__new_node_data(date(rootDate.year,
                                                               rootDate.month,
                                                               rootDate.day))))

    def __new_node_data(self, new_date: date, batch=None) -> tuple[date, list]:
        if batch is None:
            return (new_date, [])
        else:
            return (new_date, [batch])

    def __new_node(self, data: tuple[date, list]) -> TreeNode:
        self.node_count += 1
        return TreeNode(data)

    def add_batch(self, batch: b.Batch) -> None:
        date_of_batch = date(batch.date.year, batch.date.month, batch.date.day)
        current = self.root
        while date_of_batch != current.data[0]:
            if current.data[0] > date_of_batch:
                if current.left is None:
                    current.left = self.__new_node(
                        self.__new_node_data(date_of_batch))
                current = current.left
            else:
                if current.right is None:
                    current.right = self.__new_node(
                        self.__new_node_data(date_of_batch))
                current = current.right
        current.data[1].append(batch)

    def search(self, search_date: date) -> list[b.Batch] | None:
        """
            Returns the list of Batches created on the search date.\n
            None if none were created on that date
        """
        current = self.root
        while search_date != current.data[0]:
            if current.data[0] > search_date:
                current = current.left
            else:
                current = current.right
        if current is None:
            return None
        return current.data[1]

    def range_search(self, start_date: date | None, end_date: date | None) -> list[b.Batch]:
        order = inorder(self.root)
        begining_slice = 0
        ending_slice = len(order)
        if start_date is not None:
            while order[begining_slice][0] <= start_date:
                begining_slice += 1
        if end_date is not None:
            while order[ending_slice-1][0] >= end_date:
                ending_slice -= 1
        ret_list = []
        for i in order[begining_slice:ending_slice]:
            ret_list.append(i[1])
        return ret_list


if __name__ == "__main__":
    batches = []
    for x in range(10):
        for i in range(10):
            for j in range(1, 13):
                batches.append(b.Batch(f"{i},{j},{x}", datetime(1995+i, j, 1)))
    bt = BatchTree(datetime(2000, 1, 1))

    for i in batches:
        bt.add_batch(i)

#    print(f"Search date: {date(2000, 1, 1)}\n")
#    for i in bt.search(date(2000, 1, 1)):
#        print(i)
    for i in bt.range_search(date(2000, 1, 1), None):
        print(i)
