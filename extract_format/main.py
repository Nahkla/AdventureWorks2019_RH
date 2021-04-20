from packages import misc, load_schema, generate_table

file_path = misc.load_rel_path(
    directory='files',
    filename='AW_2019_schemas',
    suffix='csv'
)

schemas = load_schema.LoadSchema(
    file_path=file_path
).read_file()

table_format = generate_table.TableFormat(
    schemas=schemas,
    schema_out='Person',
    table_out='Person'
).format_block_increments()


