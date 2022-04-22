""" Домашка до понедельника.
1. Добить последнюю домашку. Это крайний срок сдачи.
2. Делаем систему регистрации-авторизации:
Создаем класс Authenticator в модуле authenticator. Методы класса:

    i Конструктор. В нем создаются переменные экземпляра класса self.login: str | None, self._password | None, self.last_success_login_at: datetime | None, self.errors_count: int. 
      По умолчанию у этих переменных должно быть None значение. У переменной errors_count значение 0. Вызывает метод _is_auth_file_exist. Если файл существует, вызвать метод _read_auth_file.
   ii _is_auth_file_exist - Проверяем наличие файла auth.txt рядом (в той же папке). Не принимает аргументов, возвращает bool значение. True - файл авторизации существует. False - не существует.
  iii _read_auth_file - Чтение данных из файла auth.txt. Данные из файла записываем в переменные объекта класса созданные ранее (self.login, self._password, etc). Ничего не возвращает. 
      В файле должно быть 4 строки:
        a.Логин
        b.Пароль
        c.datetime.utcnow().isoformat() строка, которую нужно перевести к datetime объекту
        d.количество проваленных попыток (ошибки)
   iv authorize(login, password) - Проверка логина и пароля. Принимает аргументы строки логина и пароля. Сравнивает логин и пароль из аргументов с логином и паролем из файла. 
      Если логин и пароль неверные, вызывает исключение AuthorizationError (нужно создать этот класс в соответствующем месте). Если логин и пароль неверные, 
      увеличиваем счетчик проваленных попыток-ошибок и перезаписываем их в файле. Вызывает метод _update_auth_file.
    v _update_auth_file - Перезапись файла auth.txt. Не принимает аргументов, не возвращает ничего. Метод должен перезаписать количество попыток авторизации и время авторизации,
       что лежат в переменных экземпляра.
   vi registrate(login, password) - Регистрация пользователя. Принимает аргументы строки логина и пароля. Делает проверку, что файла рядом auth.txt нет. Если он есть, 
      вызывает исключение RegistrationError (нужно создать этот класс в соответствующем месте). Создает файл auth.txt и сохраняет туда логин, пароль, datetime.utcnow().isoformat(), 
      количество проваленных попыток (ошибки) при попытке регистрации (Вызывает метод _update_auth_file).

3. В main функции (в файле main.py) создаем объект класса Authenticator.
4. Проверяем, что у объекта класса Authenticator есть логин (не None значение). Если его нет, сказать пользователю, что он проходит регистрацию. Если логин есть, сказать, 
   что нужно для авторизации вести логин и пароль.
5. В бесконечном цикле запрашиваем у пользователя логи и пароль. Нужно либо зарегистрировать пользователя, либо авторизовать в зависимости от предыдущей проверки в пункте выше. 
   Обрабатывать ошибки, вызываемые методами класса Authenticator.
6. Удаляем весь код с подсказкой паспорта, ввода имени и возраста. Класс валидатора, модуль валидатора и ошибку валидации удаляем (но не забываем, что это должно быть все в гит истории, 
   потому что к этому вернемся).
7. Приветствуем пользователя: пишем логин, время последней успешной авторизации (формат день.месяц.год час:минута:секунда) и сколько раз пытались войти в приложение с ошибкой авторизации.
8. Запускаем игру в отгадайку рандомного числа. """



from errors import RegistrationError
from errors import AuthorizationError
from datetime import datetime
import os.path


class Authenticator():
    """ Родительский класс в котором:
        - Конструктор.
        - Метод наличия файла.
        - Метод чтения данных из файла.
        - Метод авторитизации.
        - Метод записи в файле.
        - Метод регистрации."""

    def __init__(self):
        """ Конструктор в котором создаются переменные экземпляра класса
            Вызывает метод _is_auth_file_exist. 
            Если файл существует, вызваем метод _read_auth_file. """

        self.login: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0

        if self._is_auth_file_exist():
            print('Вход в систему!')
            self._read_auth_file()
        else:
            print('Регистрация пользователя!')
    

    def _is_auth_file_exist(self) -> bool: 
        """ Метод для проверки наличия файла auth.txt рядом (в той же папке). 
            Не принимает аргументов, возвращает bool значение. """
        return os.path.isfile(os.path.join(os.path.dirname(__file__), 'auth.txt'))

    
    def _read_auth_file(self):
            """ Метод чтение данных из файла auth.txt. В файле 4 строки:
                a.Логин
                b.Пароль
                c.datetime.utcnow().isoformat() строка, которую нужно перевести к datetime объекту
                d.Количество проваленных попыток (ошибки) """
            
            with open(r'C:\Python\Уроки TeachMeSkill\Home Works\7\auth.txt', 'r') as files:

                self.login = files.readline().strip()
                self._password = files.readline().strip()
                self.last_success_login_at = datetime.fromisoformat(files.readline().strip())
                error_count = files.readline().strip()

                if error_count == 0:
                    self.errors_count = int(error_count)
                

    def authorize(self, login, password):
        """ Метод проверка логина и пароля. Принимает аргументы строки логина и пароля. 
            Сравнивает логин и пароль из аргументов с логином и паролем из файла. 
            Либо выдает ошибку в случае пустых строк AuthorizationError """

        if login:

            if login != self.login or password != self._password:
                self.errors_count += 1
                self._update_auth_file()
                raise AuthorizationError('Ошибка авторизации !')
            
            else:
                self._update_auth_file()

        else:
            self.errors_count += 1
            raise AuthorizationError('Введите корректно логин и пароль!')
            

    def _update_auth_file(self) -> None:
        """ Метод перезаписи файла auth.txt. Не принимает аргументов, не возвращает ничего. """
        
        with open(r'C:\Python\Уроки TeachMeSkill\Home Works\7\auth.txt', 'w') as files:
            
            files.write(f'{self.login}\n')
            files.write(f'{self._password}\n')
            self.last_success_login_at = datetime.utcnow().isoformat(' ')
            files.writelines(self.last_success_login_at)
            files.write(f'\n{self.errors_count}')
           


    def registrate(self, login, password):
        """ Метод регистрация пользователя. Принимает аргументы строки логина и пароля. """

        if login: 
            
            self.login = login
            self._password = password
            self._update_auth_file() 

        else:
            self._is_auth_file_exist()
            self.errors_count += 1
            raise RegistrationError('Ошибка регистрации !')