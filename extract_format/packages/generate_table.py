import pandas as pd
from extract_format.packages import misc

file_path = misc.load_rel_path(
    directory='files',
    filename='AW_2019_schemas',
    suffix='csv'
)


class TableFormat:
    file = file_path
    schemas = schema_table = pd.read_csv(
        file, delimiter=';'
    )
    mx_array = [
        schemas['schema'].tolist(),
        schemas['table'].tolist()
    ]
    mx_tuples = list(
        zip(*mx_array)
    )
    schemas_index = pd.MultiIndex.from_tuples(
        mx_tuples,
        names=[
            'schema',
            'table'
        ]
    )
    schemas.index = schemas_index
    schemas = schemas.drop(
        [
            'schema',
            'table',
        ],
        axis=1
    )

    def __init__(
            self,
            schema_out,
            table_out
    ):
        self.schema_out = schema_out
        self.table_out = table_out

    def format_schema(self):
        top_line = f'Table {self.schema_out}{self.table_out}' \
                   + ' as ' + \
                   f'{self.schema_out[0]}{self.table_out[0]}' \
                   + ' {'
        self.schemas.sort_index(inplace=True)  # to get rid of performance warning line 837
        attributes, domains = [
            self.schemas.loc[pd.IndexSlice[(self.schema_out, self.table_out)],
                             col] for col in ['column', 'domain']
        ]
        attributes_domains = [
            ' '.join(i) for i in list(zip(attributes.tolist(), domains.tolist()))
        ]

        bottom_line = '}'

        return {'table': print(
            top_line,
            *attributes_domains,
            bottom_line,
            sep="\n")
        }
