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

    def format_block_increments(self, sch_out, tab_out):

        top_line = f'Table {sch_out}{tab_out}' \
                   + ' as ' + \
                   f'{sch_out[:2]}{tab_out[:2]}' \
                   + ' {'
        attributes, domains = [
            self.schemas.loc[pd.IndexSlice[(sch_out, tab_out)],
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
        bottom_line = f'}}\n//end of {tab_out} table'

        return {
            'top_line': top_line,
            'attributes_domains': attributes_domains,
            'bottom_line': bottom_line
        }

    def print_table(self, sch_out, tab_out):

        block = self.format_block_increments(sch_out, tab_out)

        return print(
            block['top_line'],
            *block['attributes_domains'],
            block['bottom_line'],
            sep='\n'
        )

    def automate_blocks(self):

        if self.schema_out is None:
            schemas_ls = self.schemas.index.get_level_values(0).unique()

        for sch in schemas_ls:
            for tab in self.schemas.loc[sch, :].index.unique():
                self.print_table(
                    sch_out=sch,
                    tab_out=tab
                )

        return
