from . import misc
import pandas as pd


class ExecuteQuery:

    def __init__(self, sql_query, connection):
        self.sql_query = sql_query
        self.connection = connection

    def ex_query(self):
        try:
            query_path = misc.load_rel_path(
                directory='sql_queries',
                filename=self.sql_query,
                suffix=''
            )
            sql_query = open(query_path, 'r').read()
        except:
            sql_query = self.sql_query
        return pd.read_sql(sql_query, self.connection)
