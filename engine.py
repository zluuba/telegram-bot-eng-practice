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

# print(random.sample(list(dictionary.keys()), 4))
# print(random.choice(list(dictionary.values())))


print('Hello, zluuba!')
while True:
    answers = random.sample(list(dictionary.keys()), 4)
    question = random.choice(answers)
    # print(answers)


    print(f'What is answer "{question}"?')
    for pos, answer in enumerate(answers):
        print(f"{pos + 1}. {dictionary[answer]}")
    answer = int(input())
    print(answer)
    if dictionary[answers[answer - 1]] == dictionary[question]:
        print('Correct')
    else:
        print(f'Incorrect. Correct answer is {dictionary[question]}')
