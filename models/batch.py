from .record import Record


class Batch:
    def __init__(self, file_name: str, date: str) -> None:
        self.file_name = file_name
        self.date = date
        self.records = []
        for i in range(5):
            self.records.append(Record("10/30/2026", "Sale", 300.99, "Jacob"))
