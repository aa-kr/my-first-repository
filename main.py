import telebot
import datetime
import time
import threading
import random


bot = telebot.TeleBot('ведите токен')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе вовремя принимать лекарство')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()
@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = [
        "Вовремя принимая лекарства, вы обеспечиваете поддержание стабильного уровня активного вещества в крови, что необходимо для их эффективного действия. Это особенно важно для антибиотиков, антидепрессантов, препаратов для контроля артериального давления и других медикаментов, где стабильность концентрации вещества критична для достижения лечебного эффекта.",

        "Для антибиотиков и противовирусных препаратов своевременный прием играет ключевую роль в предотвращении развития устойчивости микроорганизмов. Неправильный прием или пропуск доз может привести к тому, что бактерии или вирусы адаптируются, становясь устойчивыми к лечению, что делает будущие инфекции труднее поддающимися лечению.",

        "Некоторые лекарства могут вызывать побочные эффекты, если их принимать неправильно. Например, некоторые препараты нужно принимать с пищей, чтобы уменьшить раздражение желудка, или натощак для лучшего всасывания. Вовремя принимая лекарства, вы снижаете риск возникновения нежелательных побочных эффектов и обеспечиваете наиболее безопасное использование медикаментов."]

    random_fact = random.choice(list)
    bot.reply_to(message, f'Как правильно принимать лекарство {random_fact}')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, 'Принимать лекарство нужно по назначению врача')

def send_reminders(chat_id):
    first_rem = "07:56"

    second_rem = "07:57"

    end_rem = "07:58"
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem:
          bot.send_message(chat_id, "Напоминание - прими лекарство от давления")
          time.sleep(61)
        elif now == second_rem:
          bot.send_message(chat_id, "Напоминание - прими лекарство от кашля и витамины")
          time.sleep(61)
        elif now == end_rem:
          bot.send_message(chat_id, "Напоминание - прими лекарство и успокаивающее")
          time.sleep(61)

    time.sleep(1)



bot.polling(none_stop=True)


