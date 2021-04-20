from packages import misc, generate_table

file_path = misc.load_rel_path(
    directory='files',
    filename='AW_2019_schemas',
    suffix='csv'
)

table_format = generate_table.TableFormat(
    schema_out='Person',
    table_out='Person'
).format_schema()

