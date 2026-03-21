#  Jacob Milham
#  CIS 267
#  Spring 2026
#  This will load/read different data types from the disk.
from datetime import datetime
from models import batch, record, user


def __conv_date(date: str) -> datetime:
    d, t = date.split(" ")
    d = d.split("-")
    d = list(map(int, d))
    t = t.split(":")
    t = list(map(int, t))
    return datetime(d[0], d[1], d[2], t[0], t[1], t[2])


def __load_record(rec_line: str) -> (record.PayrollRecord | record.RecordBase |
                                     record.RentRecord | record.SaleRecord |
                                     record.ServiceRecord | record.TaxRecord):
    rec = rec_line.split("\t")
    if rec[0] == "RecordBase":
        return record.RecordBase(__conv_date(rec[1]), float(rec[2]), rec[3])
    elif rec[0] == "SaleRecord":
        return record.SaleRecord(__conv_date(rec[2]), float(rec[3]), rec[4],
                                 rec[1] == "True")
    elif rec[0] == "ServiceRecord":
        return record.ServiceRecord(__conv_date(rec[2]), float(rec[3]), rec[4],
                                    rec[1] == "True")
    elif rec[0] == "PayrollRecord":
        return record.PayrollRecord(__conv_date(rec[2]), float(rec[3]), rec[4],
                                    rec[1])
    elif rec[0] == "RentRecord":
        return record.RentRecord(__conv_date(rec[2]), float(rec[3]), rec[4],
                                 rec[1] == "True")
    elif rec[0] == "TaxRecord":
        return record.TaxRecord(__conv_date(rec[2]), float(rec[3]), rec[4],
                                rec[1])
    else:
        raise NotImplementedError


def load_batch(file_name: str) -> batch.Batch:
    with open(file_name, "r") as f:
        current_line = f.readline().split("\t")
        return_batch = batch.Batch(current_line[0],
                                   __conv_date(current_line[1]))
        for line in f.read().splitlines():
            return_batch.append(__load_record(line))
    return return_batch


def load_user(users_name: str) -> user.User:
    with open(users_name+".dat", "r") as f:
        line = f.read().split("\t")
        if line[3] == "None":
            end_date = None
        else:
            end_date = __conv_date(line[3])

        return user.User(line[0], line[1], __conv_date(line[2]), end_date)


if __name__ == "__main__":
    #  Needs save.py to have been run first
    b = load_batch("generic_batch.dat")
    print(b)

    u = load_user("Generic_Admin")
    print(u)
    u = load_user("Generic_user")
    print(u)
