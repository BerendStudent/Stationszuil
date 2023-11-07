import psycopg2
import requests
from tkinter import *



#Vraagt openweathermap om het weer op bepaalde coordinaten.
def Weather(lat, lon):
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=43399931c44060b742dcbde016e6a11d"
    weer = requests.get(api).json()
    return weer['weather'][0]['main']

def Coordinates(city):
    api = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=43399931c44060b742dcbde016e6a11d"
    answer = requests.get(api).json()
    coordinates = [answer[0]['lat'], answer[0]['lon']]
    return coordinates
def onclick(city):
    latlong = Coordinates(city)

    """"tekst volgt het algoritme: 1. NAAM uit PLAATS zegt BERICHT. Kan vast met een loop, maar dit werkt."""
    tekst = (f"Welkom in {city} \n" 
             f"1. {output[0][0]} uit {output[0][2]} zegt, '{output[0][1]}',\n 2. {output[1][0]} uit {output[1][2]} zegt, '{output[1][1]}',\n"
             f"3. {output[2][0]} uit {output[2][2]} zegt, '{output[2][1]}',\n 4.  {output[3][0]} uit {output[3][2]} zegt, '{output[3][1]}',\n "
             f"5.  {output[4][0]} uit {output[4][2]} zegt, '{output[4][1]}'\n"
             f" Het weer vandaag is:{Weather(latlong[0], latlong[1])}")
    text = Label(master=root,
                 text=tekst,
                 background='yellow',
                 font=('arial', 16, 'bold'),
                 foreground=('blue'),
                 width=800,
                 height=800)
    Utrecht.pack_forget()
    Amsterdam.pack_forget()
    Almelo.pack_forget()
    text.pack()

connection = psycopg2.connect(
    database="StationsReviews",
    user="postgres",
    password="password",
    host="20.82.106.102",
    port="5432"
)
cursor = connection.cursor()
query = """SELECT Naam, Inhoud, Stationsnaam FROM berichten ORDER BY datum DESC LIMIT 5"""
cursor.execute(query)
output = cursor.fetchall()


root = Tk()
root.title("Reviews")
Amsterdam = Button(root,text='Amsterdam Centraal', command=lambda: onclick('Amsterdam'))
Amsterdam.pack()
Utrecht = Button(root,text='Utrecht Centraal', command=lambda: onclick('Utrecht'))
Utrecht.pack()
Almelo = Button(root,text='Station Almelo', command=lambda: onclick('Almelo'))
Almelo.pack()

root.mainloop()