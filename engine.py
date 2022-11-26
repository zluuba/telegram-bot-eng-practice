'''
    1. Пользователь запустил игру
    2. Игра приветствует игрока
    3. Игра задает вопрос видаЖ
    "what is answer <слово на английском>?"
        1. <>
        2. <>
        3. <>
        4. <>
    4. Пользователь вводит вариант ответа 1-4
    5.1 Если правильный ответ, то распечатать "Correct"
    5.2 Пользователь играет до тех пор, пока не выйдет из игры
'''
import random


dictionary = {
    "hello": "привет",
    "bye": "пока",
    "run": "запуск",
    "game": "игра",
    "file": "файл"
}


print('Hello, zluuba!')


while True:
    answers = random.sample(list(dictionary.keys()), 4)
    question = random.choice(answers)
    print(f'What is answer "{question}"?')
    for pos, answer in enumerate(answers):
        print(f"{pos + 1}. {dictionary[answer]}")
    answer = int(input())
    print(answer)
    if dictionary[answers[answer - 1]] == dictionary[question]:
        print('Correct')
    else:
        print(f'Incorrect. Correct answer is {dictionary[question]}')

# day2.


'''
    переходим в телеграм, переходим к BotFather, общаемся с ботом, создается токен
    библиотека: python-telegram-bot - устанавливаем
    библиотека: from telegram.ext, import Updater, MessageHandler, Filters
    api.telegram.org // подробнее о ботах, документация
    
    TOKEN = ...
    
    # пишешь текст, бот возвращает этот текст
    def parrot(update, context):
        context.bot.send_message(update.effective_chat.id, update.effective_message.text)
        
    
    bot = Updater(token=TOKEN)
    bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    bot.start_polling()
    
    --------------------------------------
    from telegram import keyboard
    
    # пишешь текст, бот возвращает этот текст
    def start_game(update, context):
    chat_id = update.effective_chat.id
    
    context.bot.send_message(update.effective_chat.id, "Hello, zluuba.")
    
    answers = random.sample(list(dictionary.keys()), 4)
    question = random.choice(answers)
    
    keyboard = ReplyKeyboardMarkup.from_column(answers, resize_keyboard = True, one_time_keyboard = True)
    
    context.bot.send_message(update.effective_chat.id, f"What is answer {question}", reply_markup=keyboard)
        
    
    bot = Updater(token=TOKEN)
    bot.dispatcher.add_handler(CommandHandler('start', start_game))
    bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    bot.start_polling()

'''


