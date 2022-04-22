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



class ValidationError(Exception):
    """Класс валидации данных на ошибки"""