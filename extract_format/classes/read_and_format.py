import pandas as pd
from extract_format.classes import misc

file_path = misc.load_rel_path(
    directory='files',
    filename='AW_2019_Schematas',
    suffix='csv'
)

class rnf:

    file = file_path

    def __init__(self):
        file = self.file

    def load_csv(self):

        schema_table = pd.read_csv(
            self.file, delimiter=';'
        )
        return schema_table

    def read_schemas(self):
        return self.load_csv()['Schema'].unique()

    def format_schema(self):
        print(self.read_schemas())
rnf().format_schema()