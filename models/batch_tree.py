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
        self.left: TreeNode = left  # type: ignore
        self.right: TreeNode = right  # type: ignore

    def is_leaf(self) -> bool:
        if self.left is None and self.right is None:
            return True
        return False


class BatchTree:
    def __init__(self, rootDate: datetime) -> None:
        self.root = (self.__new_node(self.__new_node_data(date(rootDate.year,
                                                               rootDate.month,
                                                               rootDate.day))))

    def __new_node_data(self, new_date: date, batch=None) -> tuple[date, list]:
        if batch is None:
            return (new_date, [])
        else:
            return (new_date, [batch])

    def __new_node(self, data: tuple[date, list]) -> TreeNode:
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


if __name__ == "__main__":
    batches = []
    for x in range(10):
        for i in range(10):
            for j in range(1, 13):
                batches.append(b.Batch(f"{i},{j},{x}", datetime(1995+i, j, 1)))
    bt = BatchTree(datetime(2000, 1, 1))
    for i in batches:
        bt.add_batch(i)
    print("YAY")