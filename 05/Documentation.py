"""Домашка до понедельника (берём уже то, что вы сделали к последнему уроку):

1. Оптимизировать алгоритм
2. Переименовать функции на:
   1. validate_name - проверка имени
   2. validate_age - проверка возраста
   3. clear_whitespaces - функция очистки строки от пробелов в начале и конце
   4. get_passport_advice - функция получения совета по замену паспорту
   5. guess_number_game - игра "угадай число", где пользователь вводит число и пытается отгадать случайно сгенерированное число от 1 до 5
3. Все функции валидации (`validate_name`, validate_age`) должны всегда возвращать `None, а в случае ошибки - делать raise Exception(текст ошибки).
4. Использовать функцию clear_whitespaces еще и для введенной строки, в которой должно быть число.
5. В функции main, необходимо отловить ошибки из функций validate_name, validate_age. Вывести пользователю: "Я поймал ошибку: {текст ошибки}". И если были ошибки, тогда вам необходимо заново запросить у пользователя ввод данных.
6. В функции main обрабатывать ошибку ValueError (не используем Exception) во время перевода строки к int.
7. Перед запросом данных в функции main пользователю должно печататься номер текущей попытки ввода данных. Пользователю отображать попытки начиная с 1, в коде попытки должны быть с 0.
8. Во время игры "угадай число" тоже должен быть счетчик попыток, который будет отображаться при успешно угаданному числу. Пользователю отображать попытки начиная с 1, в коде попытки должны быть с 0."""


from typing import Optional
import random


# Создем функцию, которая очищает введённые данные от лишних пробелов в начале и в конце строки.
def clear_whitespaces(value: str) -> int:
    """Функция удаления пробелов спереди и в конце."""

    return value.strip()


# Создаем функцию для проверки ввода имени
def validate_name(name: str) -> Optional[str]:
    """Функция имени. Проверка на ошибку ввода имени: проверку на пустоту, 
    проверка на минимальное количество символов, а также на большое количество 
    пробелов между фамилией и именем"""

    if len(name) == 0:
        raise Exception("Не введено имя пользователя.") 
    elif len(name) < 3:
        raise Exception("Слишком короткое имя пользователя.")
    if name.count(" ") > 1:
        raise Exception("Слишком много пробелов между фамилией и именем!") 

# Создаем функцию для проверки ввода возраста
def validate_age(age:int) -> Optional[str]:
    """Функция возраста. Проверка на ошибку ввода возраста на отрицательное число
    и если пользователю менее 14 лет"""

    if age <= 0:
        raise Exception("Извините ошибка ввода возраста !")   

    elif age < 14:
        raise Exception("Ваш возраст меньше 14.") 
    

# Создаем функцию для выдачи/замене паспорта
def get_passport_advice(age: int) -> str:
    """Функция выдачи/замены паспорта в зависимости от возраста"""

    if age == 16 or age == 17:
        return f"\nПолучите паспорт впервые!"

    elif age == 25 or age == 26:
        return f"\nЗамените паспорт впервые!"

    elif age == 45 or age == 46:
        return f"\nЗамените паспорт повторно!" 



def guess_number_game() -> str:
    """Функция 'Угадай число' где игроку будет предложено угадать число от 1 до 10.
    В зависимости от того что будет вводить пользователь, будет выводиться текст 
    и количество попыток потраченных на игру"""

    # Счетчик попыток игры
    counter_game = 0
    game = random.randint(1, 10)
    
    print('Отлично, я загадал число от 1 и 10. Сможешь угадать?')
    #print(game)

    # Создаем цикл в котором будет выводиться сообщения в зависимости от введенных данных пользователя
    while True:
        print(f'Это ваша {counter_game + 1} попытка!')
        guess = int(input("Введите целое число: "))

        if guess == game:
            print("Да ты Нострадамус! O_O")
            print(f'Вы потратили {counter_game + 1} попыток!')
            return

        print("А нет, не угадал! :P")
        counter_game +=1
        
            

# Создаем функцию в которой будут вызовы всех остальных функций и ввод данных.
def main():
    """Функция для вызова остальных функций. В зависимости того как будут введены данные - будет выводиться ошибка ввода данных с
    повторным запросом всех данных, либо приветсвенный текст. При выводе приветственного текста программа предложит сыграть в игру 
    'Угадай число' в которой так же будет указано количество попыток с момента начала игры и общего количества попыток потраченных 
    на завершение игры (отгадывания числа)."""

    # Счетчик попыток ввода данных
    counter = 0

    while True:

        # Запрос ввода данных от пользователя с индикацией попытки ввода дынных    
        print(f'Это ваша {counter + 1} попытка!')
        first_name = input("Привет пользователь! Как мне к вам обращаться ? ")
        first_name = clear_whitespaces(first_name)
        old_age = None 

        # Обработка введенных данных возраста в случае ввода не цифр
        try:
            old_age = input("Сколько тебе лет ? ")   
            old_age = int(clear_whitespaces(old_age)) 
        
        except ValueError as e:
            print(f'"Это ошибка ввода данных {e}. Нужно вводить числа! ')
            counter += 1
            continue

        # Обработка введенных данных на ошибки    
        try:
            validate_name(first_name) 
            validate_age(old_age) 
                
        except Exception as validation:
            print(f'Ой я словил ошибку: {validation}')
            counter += 1
            continue

        # Вывод приветственного сообщения при корректном вводе данных
        result_text = f'Ваше имя {first_name.title()}. Ваш возраст {old_age}. Приятно познакомиться!'

        # Проверка ввыдачи/замены паспорта. Так же будет отображаться в приветсвенном сообщении в соответствии с возрастом.
        passport_advace_text = get_passport_advice(old_age)
        if passport_advace_text:
            result_text += passport_advace_text
            
        print(result_text)
        print(f'Вы потратили {counter + 1} попыток что бы ввести имя и возраст!')
        print(guess_number_game())
        break         
main()
    
