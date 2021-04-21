from . import db_to_df


class DefineRel:

    def __init__(
            self,
            db_info,
            schema_out,
            table_out,
            connection
    ):
        self.db_info = db_info
        self.schema_out = schema_out
        self.table_out = table_out
        self.connection = connection

    def get_relationships(
            self,
            sch_out,
            tab_out,
    ):
        relation_set = self.db_info.loc[(sch_out, tab_out), :]
        relationship_df = relation_set[(relation_set.rel == '>-')]
        return relationship_df

    def check_cardinalities(self):
        relationship_df = self.get_relationships(
            self.schema_out,
            self.table_out
        )

        def query_func(column_ls, schem, tab):
            return f'SELECT {",".join(column_ls)} ' \
                   f'FROM {schem}.{tab}'

        initial_rel_query = query_func(
            column_ls=relationship_df.column_name,
            schem=self.schema_out,
            tab=self.table_out
        )
        participated_table_schemas = relationship_df.loc[(self.schema_out, self.table_out), ['primary_schema', 'primary_table']]
        participated_table_schemas = [f'{self.schema_out}{self.table_out}']+[''.join(i) for i in participated_table_schemas.values]
        fk_columns = ['pk_column_name', 'primary_schema', 'primary_table']
        fk_relationship_df_info = relationship_df.loc[(self.schema_out, self.table_out), fk_columns]
        fk_ls = [fk_relationship_df_info.iloc[i, :].to_list() for i in range(len(fk_relationship_df_info))]
        queries = [initial_rel_query] + [
            query_func(
                column_ls=[fk_ls[i][0]],
                schem=fk_ls[i][1],
                tab=fk_ls[i][2]
            ) for i in range(len(fk_ls))
        ]

        relationship_dfs = [
            db_to_df.ExecuteQuery(
                sql_query=query,
                connection=self.connection
            ).ex_query() for query in queries
        ]

        count_rows = [
            [len(i), [len(i[col].unique()) for col in i.columns]] for i in relationship_dfs
        ]

        return dict(
            zip(participated_table_schemas, count_rows)
        )

    def test(self):
        return self.get_relationships(self.schema_out, self.table_out)
