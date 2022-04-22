"""Домашка до понедельника (берём уже то, что вы сделали к последнему уроку):

1. Исправить все нюансы, которые были озвучены во время проверки домашки на последнем уроке.
2. Создать модуль exceptions, в нем класс ValidationError, который наследуется от Exception. 
   Никакие методы, свойства переопределять не нужно, необходимо только описать в docstring, что это класс ошибки валидации данных.
3. Создать модуль validator, в котором:
    i. Реализовать класс Data, конструктор которого принимает name и age аргументы, сохраняет их в одноименные переменные экземпляра класса. 
    Так же у этого класса должен быть метод _clear_whitespaces, который очищает от пробелов в начале и в конце переменные name и age у экземпляра класса. 
    Вызывать метод _clear_whitespaces необходимо из конструктора класса.
   ii. Реализовать класс DataWithDate, наследовавшись от класса Data. Конструктор должен делать то же самое, что и родительский класс, но дополнительно сохраняет текущее время, 
    когда был создан этот экземпляр класса ( см. datetime.utcnow).
  iii. Реализовать класс Validator. У класса Validator должны быть следующие методы:
        a.конструктор класса — в экземпляре класса создает переменную data_history, которая является пустым списком, но будет хранить объекты класса Data.
        b._validate_name — валидация имени (скопировать код из функции validate_name).
        c._validate_age — валидация возраста (скопировать код из функции validate_age).
        d.validate — принимает аргумент data (объект класса Data) и сохраняет в список data_history. Далее запускает методы валидации, описанные выше.
    При этом методы _validate_name и _validate_age должны брать имя и возраст из переменной Validator.data_history (самое последнее значение). А также выбрасывать исключения ValidationError вместо Exception. 
    Если переменная data_history пуста, тогда выбрасывать исключение ValueError.
4. В вашем основном файле, где вся текущая домашка:
    i. В самом верху необходимо импортировать класс Validator из модуля validator.
    ii. В самом верху необходимо импортировать класс ValidationError из модуля exceptions.    
    iii. В функции main до цикла создать объект класса. Вызвать метод validate вместо тех функций валидаций, которые были написаны в домашках ранее - эти функции необходимо удалить из этого файла. Обрабатывать ошибку ValidationError вместо Exception.
    iv. После того как пользователь ввел данные, необходимо создать объект класса DataWithDate и далее работать только с ним.
    v. Теперь количество попыток ввода данных должно выводиться только в том случае, если пользователь не смог с первого раза ввести верные данные.
    vi. После ввода верных данных и до запуска игры необходимо показать пользователю:
        a. Общее количество попыток
        b. Время первой попытки, время последней попытки
        c. Сколько времени понадобилось пользователю, чтобы от первой попытки дойти к последней (формат HH:MM:SS, где HH - часы, MM - минуты, SS - секунды)."""


from datetime import datetime
from exceptions import ValidationError


class Data:
    """ Родительский класс в котором:
        - Конструктор принимает аргументы name и age.
        - Метод очистки от пробелов."""

    def __init__(self, name: str, age: str):
        """ Конструтор сохраняет аргументы name и age в одноименные переменные экземпляра класса.
            Вызывает метод _clear_whitespaces. Age переводит в int."""

        self.name = name
        self.age = age
        self._clear_whitespaces()
        self.age = int(self.age)

    def _clear_whitespaces(self):
        """Метод очистки от пробелов вначале и в конце."""

        self.name = self.name.strip()
        #self.age = self.age.strip()

        
class DataWithDate(Data):
    """ Дочерний класс, наследуется от родительского класса Data. В котором:
        - Конструктор дополнительно сохраняет текущее время."""

    def __init__(self, name, age):
        """Конструктор выполняет то же самое, что и родительский класс, но дополнительно
           сохраняет текущее время, когда был создан этот экземпляр класса."""

        super().__init__(name, age)
        time = datetime.utcnow()


class Validator:
    """ Родительский класс в котором:
        - Конструктор класса.
        - Метод валидации имени.
        - Метод валидации возраста.
        - Метод валидации имени и возраста."""

    def __init__(self):
        """ Конструктор создает переменную data_history, которая является пустым списком,
            но будет хранить объекты класса Data."""

        self.data_history: list[Data] = []


    def _validate_name(self):
        """ Метод проверяющий name на ошибки:
            - На пустоту.
            - На длину имени менее 3 символов.
            - На большое количество пробелов между именем и фамилией."""

        name = self.data_history[-1].name

        if len(name) == 0:
            raise ValidationError("Не введено имя пользователя!")

        elif name.count(" ") > 1:
            raise ValidationError("Слишком много пробелов между именем и фамилией!")

        elif len(name) < 3:
            raise ValidationError("Слишком короткое имя пользователя!")

        return name

    def _validate_age(self):
        """ Метод проверяющий age на ошибки:
            - На отрицательный возраст.
            - На на ограничение возраста не менее 14 лет."""

        age = self.data_history[-1].age

        if age <= 0:
            raise ValidationError("Извините ошибка ввода возраста!")

        elif age < 14:
            raise ValidationError("Ваш возраст менее 14 лет!")

        return age

    def validate(self, data: Data):
        """ Принимает аргумент data (объект класса Data) и сохраняет в список data_history. 
            Далее запускает методы валидации, описанные выше."""

        self.data_history.append(data)
        name = self._validate_name()
        age = self._validate_age()

        return name, age