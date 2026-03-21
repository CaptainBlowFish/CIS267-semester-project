#  Jacob Milham
#  CIS 267
#  Spring 2026
#  This will save/write different data types to the disk.
from datetime import datetime
from models import batch, record, user


def save_batch(b: batch.Batch) -> None:
    with open(b.file_name, "w") as f:
        f.write(f"{b.file_name}\t{b.date}\n")
        for r in b.records.traverse():
            if isinstance(r, record.SaleRecord):
                f.write(f"SaleRecord\t{r.taxable}")
            elif isinstance(r, record.ServiceRecord):
                f.write(f"ServiceRecord\t{r.taxable}")
            elif isinstance(r, record.PayrollRecord):
                f.write(f"PayrollRecord\t{r.type}")
            elif isinstance(r, record.RentRecord):
                f.write(f"RentRecord\t{r.late_payment}")
            elif isinstance(r, record.TaxRecord):
                f.write(f"TaxRecord\t{r.type}")
            else:
                f.write("RecordBase")
            f.write(f"\t{r.time_stamp}\t{r.dollar_value}\t{r.authorizor}\n")


def save_user(u: user.UserBase | user.User |
              user.Admin | user.Auditor) -> None:
    with open(u.users_name+".dat", "w") as f:
        f.write(f"{u.user_code}\t{u.users_name}\t{u.start_date}\t{u.end_date}")


if __name__ == "__main__":
    generic_date = datetime(2026, 3, 17)
    #  batch tests
    example_records = [
        record.RecordBase(generic_date, 2.00, "Jacob"),
        record.SaleRecord(generic_date, 12.60, "Jacob", False),
        record.ServiceRecord(generic_date, 90.20, "Jacob", True),
        record.PayrollRecord(generic_date, 15.03, "Jacob", "Hourly"),
        record.RentRecord(generic_date, 22.07, "Jacob", False),
        record.TaxRecord(generic_date, 14.15, "Jacob", "Sales")
    ]
    b = batch.Batch("generic_batch.dat", datetime(2026, 3, 17))
    for r in example_records:
        b.append(r)

    save_batch(b)

    #  user tests
    example_users = [
        user.User(users_name="Generic_user", end_date=generic_date),
        user.Admin(users_name="Generic_Admin"),
        user.Auditor(users_name="Generic_Auditor")
    ]

    for u in example_users:
        save_user(u)
