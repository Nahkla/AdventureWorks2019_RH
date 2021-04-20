from packages import misc, load_schema, generate_table, load_sql, db_to_df

query_path = misc.load_rel_path(
    directory='sql_queries',
    filename='schema_overview',
    suffix=''
)

connection_details = misc.load_db_essentials()

AdventureWorks2019 = load_sql.LoadSQL(
    db_details=connection_details,
    db_name='adventureworks2019',
).connection()

AdventureWorks2019_info = db_to_df.ExecuteQuery(
    sql_query=query_path,
    connection=AdventureWorks2019
).ex_query()

schemas = load_schema.LoadSchema(
    db_df=AdventureWorks2019_info
).read_file()

print(schemas.columns)

table_format = generate_table.TableFormat(
    schemas=schemas,
    schema_out='Sales',
    table_out='Store'
).automate_blocks()
