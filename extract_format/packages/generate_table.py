import pandas as pd


class TableFormat:


    def __init__(
            self,
            schemas,
            schema_out,
            table_out
    ):
        self.schemas = schemas
        self.schema_out = schema_out
        self.table_out = table_out

    def format_block_increments(self):
        top_line = f'Table {self.schema_out}{self.table_out}' \
                   + ' as ' + \
                   f'{self.schema_out[0]}{self.table_out[0]}' \
                   + ' {'
        attributes, domains = [
            self.schemas.loc[pd.IndexSlice[(self.schema_out, self.table_out)],
                             col] for col in ['column_name', 'domain']
        ]
        attributes_domains = [
            ' '.join(i) for i in list(
                zip(
                    attributes.tolist(),
                    domains.tolist()
                )
            )
        ]
        bottom_line = '}'

        return {
            'top_line': top_line,
            'attributes_domains': attributes_domains,
            'bottom_line': bottom_line
        }


