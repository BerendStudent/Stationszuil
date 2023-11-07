import psycopg2
import requests
from tkinter import *

"""location = requests.get("https://ipapi.co/json").json()
print(location)
print(location['latitude'][0], ',', location['longitude'][0])"""

def Weather(lat, lon):
    api = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid=43399931c44060b742dcbde016e6a11d"
    weer = requests.get(api)
    return weer

connection = psycopg2.connect(
    database="StationsReviews",
    user="postgres",
    password="password",
    host="20.82.106.102",
    port="5432"
)
cursor = connection.cursor()
query = """SELECT Naam, Inhoud FROM berichten ORDER BY datum LIMIT 5"""
cursor.execute(query)
output = cursor.fetchall()
tekst= (f"1. {output[0][0]} zegt, '{output[0][1]}',\n 2. {output[1][0]} zegt, '{output[1][1]}',\n"
        f"3. {output[2][0]} zegt, '{output[2][1]}',\n 4.  {output[3][0]} zegt, '{output[3][1]}',\n 5.  {output[4][0]} zegt, '{output[4][1]}'")

root = Tk()
text = Label(master=root,
             text=tekst,
             background='yellow',
             font=('arial'))
text.pack()
print(tekst, Weather(52.0893191, 5.1101691))

root.mainloop()