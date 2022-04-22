""" Домашка до понедельника:
    1. Доделать последнюю домашку
    2. В файл сохранять теперь данные в формате json
    3. Разобраться как сериализовать datetime в json (Гугл, а потом написать подробно в комменте почему именно так)
    4. *Написать класс валидатора, написать валидацию для пароля: минимум 4 символа, минимум один заглавный символ, минимум один прописной символ, минимум одна цифра, минимум один спецсимвол.
    Хэшировать пароль любым алгоритмом на выбор, обосновать в комменте выбор алгоритма (можно хоть свой сделать). Написать метод валидации почты. Вместо логина у вас должен быть ввод почтового адреса. """


from errors import RegistrationError
from errors import AuthorizationError
from datetime import datetime
import json
import os.path


class Authenticator():
    """ Родительский класс в котором:
        - Конструктор.
        - Метод наличия файла.
        - Метод чтения данных из файла.
        - Метод авторизации.
        - Метод записи в файле.
        - Метод регистрации."""

    def __init__(self):
        """ Конструктор в котором создаются переменные экземпляра класса.
            Вызывает метод _is_auth_file_exist. 
            Если файл существует, вызываем метод _read_auth_file. """

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
        """ Метод для проверки наличия файла auth.json рядом (в той же папке).
            Не принимает аргументов, возвращает bool значение. """
        return os.path.isfile(os.path.join(os.path.dirname(__file__), 'auth.json'))

    
    def _read_auth_file(self):
        """ Метод чтение данных из файла auth.json. В файле 4 строки:
                a.Логин.
                b.Пароль.
                c.datetime.
                d.Количество проваленных попыток (ошибки) """
            
        with open(r'C:\Python\Уроки TeachMeSkill\Home Works\09\auth.json', 'r') as files:

            parsed_data = json.load(files)
            self.login = parsed_data['login']
            self._password = parsed_data['password']
            self.last_success_login_at = datetime.fromisoformat(parsed_data['data'])
            error_count = parsed_data['error_count']

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
        """ Метод записи/перезаписи файла auth.json. Не принимает аргументов, не возвращает ничего. """
        
        with open(r'C:\Python\Уроки TeachMeSkill\Home Works\09\auth.json', 'wt') as files:

            parsed_data = {
                'login': self.login,
                'password': self._password,
                'data': datetime.utcnow().isoformat(),
                'error_count': self.errors_count
            }

            ''' У нас есть ключ в котором дата и время Python (data), созданный с помощью datetime.untcnow(). Его значение:
                    datetime.datetime(2022, 4, 17, 21, 54, 35, 046484)
                Cериализовать его в json как строку даты и времени ISO 8601:
                    "2022-04-17 21:54:35.046484"                                                                              
                Эта строка, однажды полученная в Python, может быть десериализована обратно в объект datetime:
                    datetime.datetime(2022, 4, 17, 21, 54, 35, 046484)                                                      '''

            json.dump(parsed_data, files)


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