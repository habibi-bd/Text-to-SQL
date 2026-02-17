from sales import cursor, text_to_sql

def execute_sql(query):
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


sql_query = text_to_sql(question)
results = execute_sql(sql_query)
print("Results:", results)
