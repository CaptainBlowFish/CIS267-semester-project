#  Jacob Milham
#  CIS 267
#  Spring 2026
class UserBase:
    def __init__(self, user_code: str = "generic identifier",
                 users_name: str = "generic name", start_date: str = "1/23/26",
                 end_date=None) -> None:
        """summary_

        Args:
            user_code (str, optional): _description_.
            Defaults to "generic identifier".
            users_name (str, optional): _description_.
            Defaults to "generic name".
            end_date (None or str, optional): _description_. Defaults to None.
            If it is None authorization is still active
        """
        self.user_code = user_code
        self.users_name = users_name
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self) -> str:
        output = f"user_code: {self.user_code}\nusers_name: {self.users_name} \
                \nstart_date: {self.start_date}\nend_date: {self.end_date}"
        return output


class User(UserBase):
    def __init__(self, user_code: str = "User",
                 users_name: str = "User", start_date: str = "1/23/26",
                 end_date=None) -> None:
        super().__init__(user_code, users_name, start_date, end_date)


class Admin(UserBase):
    def __init__(self, user_code: str = "Admin",
                 users_name: str = "Admin", start_date: str = "1/23/26",
                 end_date=None) -> None:
        super().__init__(user_code, users_name, start_date, end_date)


class Auditor(UserBase):
    def __init__(self, user_code: str = "Auditor",
                 users_name: str = "Auditor", start_date: str = "1/23/26",
                 end_date=None) -> None:
        super().__init__(user_code, users_name, start_date, end_date)


if __name__ == "__main__":
    testCases = [UserBase(), User(), Admin(), Auditor()]
    for case in testCases:
        print(case)
        print("_________________________")
