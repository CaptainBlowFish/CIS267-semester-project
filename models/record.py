#  Jacob Milham
#  CIS 267
ALLOWED_EVENTS = ["Sale", "Service", "Payroll", "Rent", "Tax"]


class Record:
    def __init__(self, time_stamp: str, event_type: str,
                 dollar_value: float, authorizor: str) -> None:
        self.time_stamp = time_stamp
        if event_type in ALLOWED_EVENTS:
            self.event_type = event_type
        else:
            raise RuntimeError("Not allowed event type")
        self.dollar_value = dollar_value
        self.authorizor = authorizor
