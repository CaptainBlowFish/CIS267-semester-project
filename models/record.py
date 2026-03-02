#  Jacob Milham
#  CIS 267
#  Spring 2026
from datetime import datetime


class RecordBase:
    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str) -> None:
        self.time_stamp = time_stamp
        self.dollar_value = dollar_value
        self.authorizor = authorizor


class SaleRecord(RecordBase):
    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str, taxable: bool) -> None:
        super().__init__(time_stamp, dollar_value, authorizor)
        self.taxable = taxable


class ServiceRecord(RecordBase):
    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str, taxable: bool) -> None:
        super().__init__(time_stamp, dollar_value, authorizor)
        self.taxable = taxable


class PayrollRecord(RecordBase):
    ALLOWED_TYPES = ["Contractor", "Salary Exempt",
                     "Salary Non-Exempt", "Hourly"]

    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str, type: str) -> None:
        super().__init__(time_stamp, dollar_value, authorizor)
        if type in self.ALLOWED_TYPES:
            self.type = type
        else:
            raise RuntimeError("Not allowed payroll type field")


class RentRecord(RecordBase):
    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str, late_payment: bool) -> None:
        super().__init__(time_stamp, dollar_value, authorizor)
        self.late_payment = late_payment


class TaxRecord(RecordBase):
    TAX_TYPES = ["Federal", "State", "Local", "Sales", "Import", "Export"]

    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str, tax_type: str) -> None:
        super().__init__(time_stamp, dollar_value, authorizor)
        if tax_type in self.TAX_TYPES:
            self.type = tax_type
        else:
            raise RuntimeError("Not allowed tax tyoe")
