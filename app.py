import telebot
import requests
import json
from telebot import types
import datetime
import os  


bot = telebot.TeleBot('6033259761:AAGe25BeV-2QjckSa7BXxiTAVyvHCVDx8WE')
API = 'b8d0a8cef8058c8340ce9fb96e7ee98d'

name = None


@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'Привіт, радий тебе бачити! Напиши назву міста')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>Є такі команди: /start, /help, /city, /country, /clear.</b>', parse_mode="html")

@bot.message_handler(commands=['clear'])
def clear(message):
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id,'Я з міста Сміла.')

@bot.message_handler(commands=['Country', 'country' ,'Країни', 'країни'])
def country(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Ukraine')
    item2 = types.KeyboardButton('Belarus')
    item3 = types.KeyboardButton('France')
    item4 = types.KeyboardButton('USA')
    item5 = types.KeyboardButton('Spain')
    item6 = types.KeyboardButton('China')
    item7 = types.KeyboardButton('Turkey')
    item8 = types.KeyboardButton('Germany')
    item9 = types.KeyboardButton('United Kingdom')
    item10 = types.KeyboardButton('Thailand')
    item11 = types.KeyboardButton('Poland')
    item12= types.KeyboardButton('Ireland')
    item13 = types.KeyboardButton('Mexico')
    item14 = types.KeyboardButton('Italy')
    item15 = types.KeyboardButton('Netherlands')
    item16 = types.KeyboardButton('Japan')
    item17 = types.KeyboardButton('Philippines')
    item18 = types.KeyboardButton('Croatia')
    item19 = types.KeyboardButton('Hungary')
    item20 = types.KeyboardButton('Austria')
    

    markup.add(item1, item2, item3, item4, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20)

    bot.send_message(message.chat.id, 'Вибери назву країни.'.format(message.from_user), reply_markup = markup)


@bot.message_handler(commands=['UkraineCity', 'Ukrainecity', 'city'])
def city(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
     MyCity = types.KeyboardButton('Smila')
     item1 = types.KeyboardButton('Cherkasy')
     item2 = types.KeyboardButton('Kyiv')
     item3 = types.KeyboardButton('Uman')
     item4 = types.KeyboardButton('Vinitsa')
     item6 = types.KeyboardButton('Zhytomyr')
     item7 = types.KeyboardButton('Khmelnytskyi')
     item8 = types.KeyboardButton('Kherson')
     item9 = types.KeyboardButton('Dnipro')
     item10 = types.KeyboardButton('Zaporizhzhia')
     item11 = types.KeyboardButton('Rivne')
     item12 = types.KeyboardButton('Lutsk')
     item13 = types.KeyboardButton('Lviv')
     item14 = types.KeyboardButton('Ivano-Frankivsk')
     item15 = types.KeyboardButton('Odesa')
     item16= types.KeyboardButton('Donetsk')
     item17 = types.KeyboardButton('Mariupol')
     item18 = types.KeyboardButton('Poltava')
     item19 = types.KeyboardButton('Kryvyi Rih')
     item20 = types.KeyboardButton('Sevastopol')
     item21 = types.KeyboardButton('White Church')
     item22= types.KeyboardButton('Kremenchug')
     item23 = types.KeyboardButton('Korosten')
     item24 = types.KeyboardButton('Kramatorsk')
     item25 = types.KeyboardButton('Kamianets-Podilskyi')
    
     markup.add(MyCity, item1, item2, item3, item4, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25)

     bot.send_message(message.chat.id, 'Вибери назву міста.'.format(message.from_user), reply_markup = markup)


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:    
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        city = data["name"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        weather_description = data["weather"][0]["main"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }
        #hotandcold = 'Жарко' if temp > 20.0 else 'Холодно'
        weather_description = data["weather"][0]["main"]

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            # если эмодзи для погоды нет, выводим другое сообщение
            wd = "Посмотри в окно, я не понимаю, что там за погода..."

        bot.reply_to(message, 
        f"Погода в місті/країні: {city}\nТемпература: {temp}°C {wd}\n" 
        f'Відчувається як: {feels_like}°C\n'
        f"Вологість: {humidity}%\nВітер: {wind} м/с \n"
        f"Схід сонця: {sunrise_timestamp}\nЗахід сонця: {sunset_timestamp}\nТривалість дня: {length_of_the_day}\n"
        f"Гарного дня!"
        )

        #image = 'sunny.png' if temp > 10.0 else 'sun.png'
        #file = open('./' + image, 'rb')
        #bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Місто указано неправильно!')

@bot.message_handler(content_types=['photo', 'video'])
def photo(message):
    bot.reply_to(message, 'Навіщо мені це?')

@bot.message_handler(content_types=['audio'])
def photo(message):
    bot.reply_to(message, 'Навіщо мені музика?')

bot.polling(none_stop=True)