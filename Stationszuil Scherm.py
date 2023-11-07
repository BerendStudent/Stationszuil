import psycopg2

connection = psycopg2.connect(
    database="Project Stationszuil",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()
query = """SELECT Naam, Inhoud FROM berichten ORDER BY datum LIMIT 5"""
cursor.execute(query)
output = cursor.fetchall()
print(output)