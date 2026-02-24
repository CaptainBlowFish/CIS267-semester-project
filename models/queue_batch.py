#  Jacob Milham
#  CIS 267
#  Spring 2026
import data_types


class FutureAction:
    def __init__(self, action: str, arguments=[]) -> None:
        self.action = action
        self.arguments = arguments


class BatchInfo:
    def __init__(self, file_name, date) -> None:
        self.file_name = file_name
        self.date = date
        self.actions = data_types.Queue()

    def enqueue_action(self, action: str, arguments=[]):
        self.actions.enqueue(FutureAction(action, arguments))

    def dequeue_action(self) -> FutureAction:
        return self.actions.dequeue()


class QueuedBatch:
    def __init__(self) -> None:
        self.queue = data_types.Queue()

    def enqueue_batch(self, file_name, date) -> None:
        self.queue.enqueue(BatchInfo(file_name, date))

    def dequeue_batch(self) -> BatchInfo:
        return self.queue.dequeue()
