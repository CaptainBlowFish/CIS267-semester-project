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

    def __str__(self) -> str:
        ret_str = f"time stamp: {self.time_stamp}\t"
        ret_str += f"dollar value: {self.dollar_value}\t"
        ret_str += f"authorizor: {self.authorizor}"
        return ret_str


class SaleRecord(RecordBase):
    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str, taxable: bool) -> None:
        super().__init__(time_stamp, dollar_value, authorizor)
        self.taxable = taxable

    def __str__(self) -> str:
        return super().__str__() + f"\tis taxable: {self.taxable}"


class ServiceRecord(RecordBase):
    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str, taxable: bool) -> None:
        super().__init__(time_stamp, dollar_value, authorizor)
        self.taxable = taxable

    def __str__(self) -> str:
        return super().__str__() + f"\tis taxable: {self.taxable}"


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

    def __str__(self) -> str:
        return super().__str__() + f"\tpayroll type: {self.type}"


class RentRecord(RecordBase):
    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str, late_payment: bool) -> None:
        super().__init__(time_stamp, dollar_value, authorizor)
        self.late_payment = late_payment

    def __str__(self) -> str:
        return super().__str__() + f"\tlate payment: {self.late_payment}"


class TaxRecord(RecordBase):
    TAX_TYPES = ["Federal", "State", "Local", "Sales", "Import", "Export"]

    def __init__(self, time_stamp: datetime, dollar_value: float,
                 authorizor: str, tax_type: str) -> None:
        super().__init__(time_stamp, dollar_value, authorizor)
        if tax_type in self.TAX_TYPES:
            self.type = tax_type
        else:
            raise RuntimeError("Not allowed tax tyoe")

    def __str__(self) -> str:
        return super().__str__() + f"\ttax type: {self.type}"
