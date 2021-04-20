import pandas as pd


class LoadSchema:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        file = self.file_path
        schemas = pd.read_csv(
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
        schemas.sort_index(inplace=True)  # to get rid of performance warning line 837

        return schemas
