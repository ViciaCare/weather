import mgr as mgr
import pyowm

import settings

own = pyowm.OWM(settings.APIkey)

place = input('В каком городе/стране?: ')
mgr = own.weather_manager()

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']

print('В городе ' + place + ' сейчас ' + w.detailed_status)
print('Темпиратура сейчас около ' + str(temp))

if temp < 10:
    print('Сейчас сильные морозы, одевайся теплее!!!')
elif temp < 20:
    print('Сейчас довольно холодно, не забудте одеть куртку.')
else:
    print('Темперетура нормальная, одевайся как хочешь.')