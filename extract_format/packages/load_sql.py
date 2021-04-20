class LoadSQL:

    def __init__(
            self,
            db_details,
            db_name,
            sql_query
    ):
        self.db_details = db_details
        self.db_name = db_name
        self.sql_query = sql_query

    def return_df(self):
        import pyodbc
        import pandas as pd

        cnxn = pyodbc.connect(
            f'DRIVER={self.db_details["driver_ls"]["ODBC"]["driver_17"]}'
            f';SERVER={self.db_details["db_ls"][self.db_name]["server"]}'
            f';PORT=1433;DATABASE={self.db_details["db_ls"][self.db_name]["database"]}'
            f';UID={self.db_details["user_ls"]["admin"]["username"]};'
            f'PWD={self.db_details["user_ls"]["admin"]["pw"]}')

        sql_query = open(self.sql_query, 'r').read()

        return pd.read_sql(sql_query, cnxn)
