class LoadSQL:

    def __init__(
            self,
            db_details,
            db_name
    ):
        self.db_details = db_details
        self.db_name = db_name

    def connection(self):
        import pyodbc

        cnxn = pyodbc.connect(
            f'DRIVER={self.db_details["driver_ls"]["ODBC"]["driver_17"]}'
            f';SERVER={self.db_details["db_ls"][self.db_name]["server"]}'
            f';PORT=1433;DATABASE={self.db_details["db_ls"][self.db_name]["database"]}'
            f';UID={self.db_details["user_ls"]["admin"]["username"]};'
            f'PWD={self.db_details["user_ls"]["admin"]["pw"]}')

        return cnxn