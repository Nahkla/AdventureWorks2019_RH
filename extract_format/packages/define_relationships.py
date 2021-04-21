import numpy as np
import pandas as pd

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
        participated_table_schemas = relationship_df.loc[
            (self.schema_out, self.table_out), ['primary_schema', 'primary_table']]
        participated_table_schemas = [f'{self.schema_out}{self.table_out}']+[''.join(i) for i in participated_table_schemas.values]
        fk_columns = ['pk_column_name', 'primary_schema', 'primary_table']
        fk_relationship_df_info = relationship_df.loc[(self.schema_out, self.table_out), fk_columns]
        fk_ls = [fk_relationship_df_info.iloc[i, :].to_list() for i in range(len(fk_relationship_df_info))]
        print(fk_relationship_df_info)
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

        row_count_level_0 = [
            dict(
                zip(i, [len(i[col].unique()) for col in i.columns])) for i in relationship_dfs
        ]

        row_count = dict(
            zip(participated_table_schemas, row_count_level_0)
        )

        df_len = [len(i) for i in relationship_dfs]
        df_len = dict(zip(participated_table_schemas, df_len))

        index_comparison_level_0 = [
            dict(zip(k, [df_len[i] - row_count[i][j] for j in row_count[i].keys()]))
            for i, k in zip(df_len.keys(),  [i.columns.tolist() for i in relationship_dfs])
        ]

        index_comparison= dict(
            zip(participated_table_schemas, index_comparison_level_0)
        )
        initial_rel_count = [
            row_count[f'{self.schema_out}{self.table_out}'][i] for i in row_count[f'{self.schema_out}{self.table_out}'].keys()
        ]

        return row_count#[i - index_comparison_level_0[j] for i,j in zip(initial_rel_count,

    def test(self):
        return self.get_relationships(self.schema_out, self.table_out)
