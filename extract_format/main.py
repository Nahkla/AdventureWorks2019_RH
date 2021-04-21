from packages import misc, load_schema, generate_table, db_to_df, load_sql, define_relationships

connection_details = misc.load_db_essentials()

AdventureWorks2019 = load_sql.LoadSQL(
    db_details=connection_details,
    db_name='adventureworks2019',
).connection()

AdventureWorks2019_info = db_to_df.ExecuteQuery(
    sql_query='schema_overview',
    connection=AdventureWorks2019
).ex_query()

db_info = load_schema.LoadSchema(
    db_df=AdventureWorks2019_info
).read_file()

#table_format = generate_table.TableFormat(
 #   db_info=db_info,
 #   schema_out='Sales',
 #   table_out='Store'
#).automate_blocks()

test = define_relationships.DefineRel(
    db_info = db_info,
    schema_out='Sales',
    table_out='Store',
    connection=AdventureWorks2019
).check_cardinalities()
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print(test)

