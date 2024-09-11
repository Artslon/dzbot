
import telebot
import datetime
from telebot import types

bot = telebot.TeleBot("7321353263:AAF6USYaUWPA4C7uhT4DumUpoW5gEKkZepY", parse_mode=None)

homework = "Математика номер 81, 83\nИстория римские цифры от 1 до 50\nРодной русский написать названия 5-6 сказок"
week = 3


@bot.message_handler(commands=['start', 'help', 'start@dz5a183bot'])
def send_welcome(message):
    username = str(message.from_user.first_name)
    print(f"{username}: /start")
    print(f"Bot: Привет {username}, как тебе помочь?")
    keyboard = types.InlineKeyboardMarkup()
    key_hw = types.InlineKeyboardButton(text="Узнать Домашнее задание", callback_data="hw")
    keyboard.add(key_hw)
    key_ls = types.InlineKeyboardButton(text="Узнать Расписание уроков", callback_data="ls")
    keyboard.add(key_ls)
    key_cs = types.InlineKeyboardButton(text="Узнать Расписание звонков", callback_data="cs")
    keyboard.add(key_cs)
    bot.reply_to(message, f"Привет {username}, как тебе помочь?", reply_markup=keyboard)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    username = str(message.chat.first_name)
    if message.text == 'uploadhw':
        print(f"{username}: uploadhw")
        bot.send_message(message, "Задайте ДЗ")
        print("Bot: Задайте ДЗ")
        bot.register_next_step_handler(message, save_hw)
    if message.text == "/hw@dz5a183bot":
        print(f"{username}: /hw@    dz4abot")
        bot.send_message(message.chat.id, f"Текущее ДЗ: {homework}")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEdJtmDDg7-A5GglKlC9EpxAteugJA5QACbEoAAhmoYEix2wlEP8YGBDQE")
        print(f"Bot: Текущее ДЗ: {homework}\nsticker")


def save_hw(message):
    username = str(message.from_user.first_name)
    global homework
    homework = message.text
    print(f"{username}: {homework}")
    bot.reply_to(message, "ДЗ Задано")
    print("Bot: ДЗ Задано")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    date = datetime.datetime(2024, 9, week)
    today = week
    username = str(call.message.chat.first_name)
    if call.data == "hw":
        print(f"{username}: key_hw")
        bot.send_message(call.message.chat.id, f"Текущее ДЗ: {homework}")
        bot.send_sticker(call.message.chat.id,
                         "CAACAgIAAxkBAAEEdJtmDDg7-A5GglKlC9EpxAteugJA5QACbEoAAhmoYEix2wlEP8YGBDQE")
        print(f"Bot: Текущее ДЗ: {homework}\nsticker")
    if call.data == "ls":
        if week == 1:
            bot.send_message(call.message.chat.id,
                             "Классный час\nОДНК\nРусский язык\nТруд\nТруд\nЛитература\nМатематика(платная)/Башкирский язык")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdKZmDDqoNKJhjG4lTpgPmD62vqYc2wACm0wAAnRFYEgTtUws7heKmTQE")
            print(f"{username}: key_ls")
            print("Bot: Русский язык\nМатематика\nЛитература\nБашкирский язык\nsticker")
        elif week == 2:
            bot.send_message(call.message.chat.id,
                             "Музыка\nБиология\nГеография\nРусский язык\nРусский язык\nБашкирский язык/Математика(платная)")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdKZmDDqoNKJhjG4lTpgPmD62vqYc2wACm0wAAnRFYEgTtUws7heKmTQE")
            print(f"{username}: key_ls")
            print("Bot: Русский язык\nМатематика\nРодная литература\nОкружающий мир\nsticker")
        elif week == 3:
            bot.send_message(call.message.chat.id,
                             "Математика\nМатематика\nРодной язык\nАнглийский язык\nИстория\nИстория\nИЗО")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdKZmDDqoNKJhjG4lTpgPmD62vqYc2wACm0wAAnRFYEgTtUws7heKmTQE")
            print(f"{username}: key_ls")
            print("Bot: Русский язык\nМатематика\nЛитература\nМузыка\nАнглиский язык\nsticker")
        elif week == 4:
            bot.send_message(call.message.chat.id, "Математика\nМатематика\nРодной язык\nАнглийский язык\nОРКСЭ")
            bot.send_sticker(call.message.chat.id,
                             "AACAgIAAxkBAAEEdKZmDDqoNKJhjG4lTpgPmD62vqYc2wACm0wAAnRFYEgTtUws7heKmTQE")
            print(f"{username}: key_ls")
            print("Bot: Русский язык\nМатематика\nФизкультура\nОкрущающий мир\nОРКСЭ\nsticker")
        elif week == 5:
            bot.send_message(call.message.chat.id, "Русский язык\nЛитература\nРодной язык\nАнглиский язык")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdKZmDDqoNKJhjG4lTpgPmD62vqYc2wACm0wAAnRFYEgTtUws7heKmTQE")
            print(f"{username}: key_ls")
            print("Bot: Русский язык\nЛитература\nРодной язык\nАнглиский язык\nsticker")
        elif week == 6:
            bot.send_message(call.message.chat.id, "Нет уроков")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdClmDB_pgpYJWGrZGCN6HxWhIRQLRAACC0sAAjMiYEiaVwAB56yNR4s0BA")
            print(f"{username}: key_ls")
            print("Bot: Нет уроков\nsticker")
        elif week == 7:
            bot.send_message(call.message.chat.id, "Нет уроков")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdClmDB_pgpYJWGrZGCN6HxWhIRQLRAACC0sAAjMiYEiaVwAB56yNR4s0BA")
            print(f"{username}: key_ls")
            print("Bot: Нет уроков\nsticker")

    if call.data == "cs":
        date = datetime.datetime(2024, 9, week)
        today = (date.weekday() + 1)
        if today == 1:
            bot.send_message(call.message.chat.id,
                             "1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdKhmDDqp25p9sEuT27jLYO0QLZvKJQACbEYAAgH9aEh02_Z5UXeTQDQE")
            print(f"{username}: key_cs")
            print(
                "Bot: 1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05\nsticker")
        if today == 2:
            bot.send_message(call.message.chat.id,
                             "1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdKhmDDqp25p9sEuT27jLYO0QLZvKJQACbEYAAgH9aEh02_Z5UXeTQDQE")
            print(f"{username}: key_cs")
            print(
                "Bot: 1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05\nsticker")
        if today == 3:
            bot.send_message(call.message.chat.id,
                             "1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdKhmDDqp25p9sEuT27jLYO0QLZvKJQACbEYAAgH9aEh02_Z5UXeTQDQE")
            print(f"{username}: key_cs")
            print(
                "Bot: 1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05\nsticker")
        if today == 4:
            bot.send_message(call.message.chat.id,
                             "1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdKhmDDqp25p9sEuT27jLYO0QLZvKJQACbEYAAgH9aEh02_Z5UXeTQDQE")
            print(f"{username}: key_cs")
            print(
                "Bot: 1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05\nsticker")
        if today == 5:
            bot.send_message(call.message.chat.id,
                             "1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdKhmDDqp25p9sEuT27jLYO0QLZvKJQACbEYAAgH9aEh02_Z5UXeTQDQE")
            print(f"{username}: key_cs")
            print(
                "Bot: 1. 8:00-8:40\n2. 8:45-9:25\n3. 9:40-10:20\n4. 10:35-11:15\n5. 11:30-12:10\n6. 12:25-13:05\nsticker")
        if today == 6:
            bot.send_message(call.message.chat.id, "Нет уроков")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdClmDB_pgpYJWGrZGCN6HxWhIRQLRAACC0sAAjMiYEiaVwAB56yNR4s0BA")
            print(f"{username}: key_cs")
            print("Bot:Нет уроков\nsticker")
        if today == 7:
            bot.send_message(call.message.chat.id, "Нет уроков")
            bot.send_sticker(call.message.chat.id,
                             "CAACAgIAAxkBAAEEdClmDB_pgpYJWGrZGCN6HxWhIRQLRAACC0sAAjMiYEiaVwAB56yNR4s0BA")
            print(f"{username}: key_cs")
            print("Bot:Нет уроков\nsticker")

bot.infinity_polling()