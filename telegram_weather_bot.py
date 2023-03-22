from pyowm.owm import OWM
import telebot
import pandas
import requests, json
api_key = "Key" # key for openweathermap
bot = telebot.TeleBot('Key') #key for telegram

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="hallo")

@bot.message_handler(content_types=['text'])
def func(message):   

    city = message.text
    owm = OWM(api_key)
    mgr = owm.weather_manager() 
    observation = mgr.weather_at_place(city)
    weather = observation.weather

    stat = weather.detailed_status
    temp = weather.temperature('celsius')["temp"]
    wind ="\nWind:\n    Speed: "+str(observation.weather.wind()['speed'])+" meters per second"+"\n    Degrees: "+str(observation.weather.wind()['deg'])
    pressure = "\n\nPressure: "+str(observation.weather.barometric_pressure()["press"])

    weather_info = (city+": "+stat+"\nTemperature: "+str(temp)+str(wind)+str(pressure))

    bot.send_message(message.chat.id,text=weather_info)

bot.infinity_polling()
