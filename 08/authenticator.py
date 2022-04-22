""" Написать декоратор для функции main, в котором будет в бесконечном цикле вызов main до тех пор, пока main функция не вернет значение True. 
True значение должно вернуться в том случае, если в main не было ни одной ошибки авторизации и пользователь был успешно авторизовано/зарегистрирован """


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
            
            with open(r'C:\Python\Уроки TeachMeSkill\Home Works\08\auth.txt', 'r') as files:

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
        
        with open(r'C:\Python\Уроки TeachMeSkill\Home Works\08\auth.txt', 'w') as files:
            
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