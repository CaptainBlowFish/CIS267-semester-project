#  Jacob Milham
#  CIS 267
#  Spring 2026
import record
import data_types


class Batch:
    def __init__(self, file_name: str, date: str) -> None:
        self.file_name = file_name
        self.date = date
        self.records = data_types.LinkedList()

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
