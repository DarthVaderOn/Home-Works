""" Написать декоратор для функции main, в котором будет в бесконечном цикле вызов main до тех пор, пока main функция не вернет значение True. 
True значение должно вернуться в том случае, если в main не было ни одной ошибки авторизации и пользователь был успешно авторизовано/зарегистрирован """


from errors import RegistrationError
from errors import AuthorizationError
from authenticator import Authenticator
import random
from datetime import datetime
  

def guess_number_game() -> str:
    """Функция 'Угадай число', где игроку будет предложено угадать число от 1 до 10.
       В зависимости от того что будет вводить пользователь, будет выводиться текст 
       и количество попыток потраченных на игру"""

    # Счетчик попыток в игре
    counter_game = 0
    game = random.randint(1, 10)
    
    print('Отлично, я загадал число от 1 и 10. Сможешь угадать?')
    #print(game)

    # Создаем цикл в котором будет выводиться сообщения в зависимости от введенных данных пользователя
    while True:

        guess = int(input("Введите целое число: "))

        if guess == game:
            print("Да ты Нострадамус! (◕ ‿ ◕)")
            print(f'Вы потратили {counter_game + 1} попыток!')
            return

        print("А нет, не угадал! ¯\_(ツ)_/¯")
        counter_game +=1
        print(f'Это ваша {counter_game + 1} попытка!')


# Декоратор main
def work_main(func):
    def wrapper(*args, **kwargs):
        while True:
            if func():
                break
    return wrapper


# Вызов метода 
module = Authenticator()


@work_main
# Создаем функцию в которой будут вызовы всех остальных функций и ввод данных.
def main():
    """Функция для вызова остальных функций. В зависимости того как будут введены данные - будет выводиться ошибка ввода данных с
       повторным запросом всех данных, либо приветсвенный текст. При выводе приветственного текста программа предложит сыграть в игру 
       'Угадай число' в которой так же будет указано количество попыток с момента начала игры и общего количества попыток потраченных 
       на завершение игры (отгадывания числа)."""


    # Запрос ввода данных от пользователя с информацией ошибок ввода дынных при авторизации   
    login = input("Привет пользователь! Введите свой логин : ")
    password = input("Введите свой пароль : ")

    if module.login:

    # Обработка введенных данных в зависимости от того зарегистрирован пользователь или нет.
        try:
            module.authorize(login, password)
            calendar = datetime.fromisoformat(module.last_success_login_at).strftime('%d.%m.%Y %H:%M:%S')
            print(f'Привет {module.login.title()}! \nВремя авторизации: {calendar}. \nВо время авторизации вы допустили: {module.errors_count} ошибок.\n\nДавай сыграем в игру!')

        except AuthorizationError as e:
            print(f'{e}')
            return False

    else:   

        try:
            module.registrate(login, password)

        except RegistrationError as e:
            print(f'{e}')
            return False

    guess_number_game()
    return True  
                                 
main()