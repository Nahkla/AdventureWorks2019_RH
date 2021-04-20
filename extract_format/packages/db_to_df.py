import pandas as pd


class ExecuteQuery:

    def __init__(self, sql_query, connection):
        self.sql_query = sql_query
        self.connection = connection

    def ex_query(self):
        print(self.connection)
        sql_query = open(self.sql_query, 'r').read()
        return pd.read_sql(sql_query, self.connection)
