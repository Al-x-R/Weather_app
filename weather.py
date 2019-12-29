import requests
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time
from tkinter import messagebox

API_KEY = '78de6a7fc9f3d64b8af6cc331977a4dc'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

def choose(event):
    print(entry.current(), entry.get())

def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        press = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']
        sunrise_ts = weather['sys']['sunrise']
        sunset_ts = weather['sys']['sunset']
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime("%H:%M:%S", sunrise_struct_time)
        sunset = time.strftime("%H:%M:%S", sunset_struct_time)
        return f"Местоположение: {city}, {country} \nТемпература: {temp} °C \nАтм. давление: {press} гПа \nВлажность: {humidity}% \nСкорость ветра: {wind} м/с \nПогодные условия: {desc} \nВосход: {sunrise} \nЗакат: {sunset}"
    except:
        return "Ошибка получения данных..."

def get_weather(event=''):
    params = {
        'appid': API_KEY,
        'q': entry.get(),
        'units': 'metric',
        'lang': 'ru'
    }
    req = requests.get(API_URL, params=params)
    weather = req.json()
    label['text'] = print_weather(weather)

root = ThemedTk(theme='arc')
root.geometry('500x300')
root.resizable(0, 0)
root.title('Прогноз погоды')

s = ttk.Style()
s.configure('Label', padding=5, font='Arial 11')

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')


entry = ttk.Combobox(top_frame, values=[
    'Zaporizhzhia',
    'Melitopol',
    'Berdyansk',
    'Henichesk',
    'Dnipropetrovsk',
    'Kharkiv',
    'Donetsk',
    'Cherkasy',
    'Kiev',
    'Mykolayiv'
])
entry.place(relwidth=0.7, relheight=1)



button = ttk.Button(top_frame, text='weather', command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

low_frame = ttk.Frame(root)
low_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(low_frame, anchor='nw')
label.place(relwidth=1, relheight=1)

root.mainloop()