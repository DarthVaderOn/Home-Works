

""" Создать 3 переменных с одинаковыми данными с одинаковыми
идентификаторами """
print("Задание 1")

One_number = 1
Two_number = 1
Three_number = 1 


print(id(One_number))
print(id(Two_number))
print(id(Three_number))


print()

""" Создать 2 переменных с одинаковыми данными но с разными
идентификаторами """
print("Задание 2")

a_number = [1,2]
b_number = [1,2]

print(id(a_number))
print(id(b_number))


print()

""" *Поменять их типы так, чтобы у 1х трех были разные идентификаторы,
а у 2х последних были одинаковые """
print("Задние 3")

hard_one = list()
hard_two = list()
hard_three = list()

print(id(hard_one))
print(id(hard_two))
print(id(hard_three))

print()

hard_four = str()
hard_five = str()

print(id(hard_four))
print(id(hard_five))

