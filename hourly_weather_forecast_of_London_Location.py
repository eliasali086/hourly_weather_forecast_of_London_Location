import requests, json

import datetime as dt 
data=requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22").json()


def _Ddate():
    print("Enter the date (YYYY-MM-DD)")
    date=input()
    x=dt.datetime.now()
    x=x.hour
    x=str(x)
    if len(x)==1:
        x='0'+x

    date=date+' '+x+':00:00'

    return date


def get_weather():
    date=_Ddate()
    for d in data['list']:
        if date in d.values():
            print(f"Temperature : {d['main']['temp']}")
            print()


def get_wind_speed():
    date=_Ddate()
    for d in data['list']:
        if date in d.values():
            print(f"Wind Speed : {d['wind']['speed']}")
            print()



def get_pressure():
    date=_Ddate()
    for d in data['list']:
        if date in d.values():
            print(f"Pressure : {d['main']['pressure']}")
            print()

n=10
while not n==0:
    print("Choose:\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
    inp=int(input())
    if inp==1:
        get_weather()
    if inp==2:
        get_wind_speed()
    if inp==3:
        get_pressure()
    if inp==0:
        break