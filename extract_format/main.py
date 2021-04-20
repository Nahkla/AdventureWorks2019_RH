from packages import misc, load_schema, generate_table, load_sql

query_path = misc.load_rel_path(
    directory='sql_queries',
    filename='schema_overview',
    suffix=''
)

connection_details = misc.load_db_essentials()

AdventureWorks2019 = load_sql.LoadSQL(
    db_details=connection_details,
    db_name='adventureworks2019',
    sql_query=query_path
).return_df()

schemas = load_schema.LoadSchema(
    db_df=AdventureWorks2019
).read_file()

print(schemas.loc['Sales', :].index.unique())

table_format = generate_table.TableFormat(
    schemas=schemas,
    schema_out=None,
    table_out='Store'
).automate_blocks()
