#  Jacob Milham
#  CIS 267
#  Spring 2026
import record


class Batch:
    def __init__(self, file_name: str, date: str) -> None:
        self.file_name = file_name
        self.date = date
        self.records = []
        for i in range(5):
            self.records.append(record.SaleRecord("10/30/2026", 300.99, "Jacob", True))
