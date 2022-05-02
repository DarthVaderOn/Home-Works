"""
Дополнительная полезная домашка (сделать в Джанго или отдельно — выбирать вам):
1. Реализовать абстрактный класс машины (придумайте какие методы у машины есть, какие нужно у всех дочерних классов переопределять, а какие будут общие с готовой реализацией)
2. Реализовать несколько классов разных марок машин, наследуемых от базовой машины. Переопределить абстрактные методы, свойства. Придумать новые методы, которые есть только в конкретных марках машин.
3. Реализовать класс абстрактный класс самолета. Должно быть как минимум один или несколько одноименных атрибутов класса машины. То же самое из п.1
4. Реализовать несколько классов разных марок самолетов. То же самое из п.2
5. Создать несколько экземпляров каждой машины, каждого самолета, вызвать различные методы у этих объектов. «Поиграться», скажем так. А затем сделать коллекцию из этих объектов и через цикл пройтись по каждому
из этих объектов и вызвать те методы, которые есть во всех классах.

Таким образом мы все 4 принципа ООП на практике попробуем закрепить, которые проходили на прошлых уроках =) """



class Audi():
    producing_country = "Germany"
    firm = "VAG"
    brand = "Audi"
    color = "Grey"
    max_speed = 305
    VIN = "000000000"

    def __init__(self, color: str = 'Grey'):
        self.color = color

    def speed(self, max_speed: int = 305):
        self.max_speed = max_speed

    def info(self):
       print(f'Страна производитель {self.producing_country}. Компания {self.firm}. Цвет вашей машины {self.color}. Максимальная скорость {self.max_speed} км/ч. \nСпасибо что выбрали нашу компанию !')

    def _private_info(self, VIN: str = "000000000"):
        self.VIN = VIN
        print(f'VIN: {self.VIN}')


class Audi_A2(Audi):
    color = "White"
    max_speed = 205

    def __init__(self, color: str = 'White'):
        self.color = color

    def _Audi_A2_RS(self, power: int = 319):
        self.power = power
        print(f'Мощность данной комплектации {self.power} л.с.')


class Toyota_prius(Audi):
    producing_country = "Japan"
    firm = "Toyota Motor Corporation"
    brand = "Toyota"
    max_speed = 195

    def __init__(self, color: str = 'Red'):
        self.color = color


class Airplane():
    classification = "Пассажирский"
    range_of_flight = "Cреднемагистральный"
    max_speed = 800

    def __init__(self, types_of_transportation: str = 'Международный'):
        self.types_of_transportation = types_of_transportation

    def speed(self, max_speed: int = 800):
        self.max_speed = max_speed

    def info(self):
       print(f'Тип самолета: {self.classification}. \nТип по дальности полета: {self.range_of_flight}.\nТип по видам перевозок: {self.types_of_transportation}. \nМаксимальная скорость: {self.max_speed} км/ч.')


class Boeing_747(Airplane):
    max_speed = 980

    def speed(self, max_speed: int = 980):
        self.max_speed = max_speed


class TU_134(Airplane):
    classification = "Пассажирский"
    range_of_flight = "Ближнемагистральные"
    max_speed = 850

    def __init__(self, types_of_transportation: str = 'Региональные'):
        self.types_of_transportation = types_of_transportation

    def speed(self, max_speed: int = 850):
        self.max_speed = max_speed


class Boeing_F22_Raptor(Airplane):
    classification = "Военный"
    range_of_flight = "Многофункциональный истребитель"
    max_speed = 2410

    def __init__(self, weight_type: str = 'Средний истребитель'):
        self.weight_type = weight_type

    def speed(self, max_speed: int = 2410):
        self.max_speed = max_speed

    def info(self):
       print(f'Тип самолета: {self.classification}. \nТип по дальности полета: {self.range_of_flight}.\nТип по массе: {self.weight_type}. \nМаксимальная скорость: {self.max_speed} км/ч.')

    def _private_info(self, guns: str = ""):
        self.guns = guns
        print(f'Вооружение F-22: 20-мм пушка M61A2 Vulcan (480 снарядов); \nРакеты класса воздух-воздух: шесть AIM-120C AMRAAM; \nДве AIM-9M Sidewinder. Корректируемые авиабомбы JDAM.')



car = Audi()
car.info()
car.color = "Red"
car.info()
car.speed(355)
car.info()
car._private_info()
print()

car1 = Audi_A2()
car1.info()
car1.speed(355)
car1.info()
car1._Audi_A2_RS()
print()

car2 = Toyota_prius()
car2.info()
car2.color = "Black"
car2.info()
car2.speed(183)
car2.info()
car2._private_info('3FR65dFfD784')
print()

air = Airplane()
air.info()
air.speed(1000)
air.info()
print()

air1 = Boeing_747()
air1.info()
print()

air2 = TU_134()
air2.info()
print()

air3 = Boeing_F22_Raptor()
air3.info()
air3._private_info()