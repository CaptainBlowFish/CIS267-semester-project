class User:
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
