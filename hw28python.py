
#Задание 1
import random

def f1(numbers):
    # Создаем новый массив, в котором каждое число возводится в квадрат
    retnumbers = [num ** 2 for num in numbers]
    return retnumbers

# Создаем массив из 20 случайных чисел
numbers = []
for x in range(20):
    numbers.append(random.randint(1, 9))

# Выводим исходный массив на экран
print("Исходный массив:")
print(numbers)

# Возводим каждое число в квадрат
retnumbers = f1(numbers)

# Выводим новый массив на экран
print("Массив с числами, возведенными в квадрат:")
print(retnumbers)
print('###############################################')
#ЗАдание2

def q1(number):                                              #Функция q1 принимает число number и возвращает True
    return number % 5 != 0                                   #если число не делится на 5, и False в противном случае.

def q2(number):                                              #Функция q2 принимает число number и возвращает True
    return len(set(str(number))) == len(str(number))         #если число содержит уникальные цифры  и False в противном случае

def q3(numbers):                                             #Функция q3 принимает массив чисел numbers и применяет последовательно два фильтра
    # Убираем числа, кратные 5                                # сначала убирает числа, кратные 5, затем убирает повторы и
    numbers = list(filter(q1, numbers))                      #наконец, убирает числа с одинаковыми цифрами. Возвращается отфильтрованный массив чисел.
    # Убираем повторы
    numbers = list(set(numbers))
    # Убираем числа с одинаковыми цифрами
    numbers = filter(q2, numbers)
    return numbers
# Создаем массив из 100 случайных чисел
numbers = [random.randint(10, 100) for _ in range(100)]

# Применяем фильтры к массиву чисел
filternum = q3(numbers)

# Разбиваем отфильтрованные числа на группы по 3 элемента
numgroup1 = []                                                 # Происходит разбиение отфильтрованных чисел на группы по 3 элемента.
numgroup2 = []                                                 # В цикле for каждое число добавляется в numgroup2, и если размер numgroup2 достигает 3
for number in filternum:                                       # группа добавляется в numgroup1, а numgroup2 сбрасывается.
    numgroup2.append(number)                                   #Если в последней группе numgroup2 осталось менее 3 элементов
    if len(numgroup2) == 3:                                    # они добавляются в отдельную группу.
        numgroup1.append(numgroup2)
        numgroup2 = []

# Если в последней группе осталось менее 3 элементов, добавляем их в отдельную группу
if numgroup2:
    numgroup1.append(numgroup2)

# Выводим результат в виде таблицы
for group in numgroup1:                                         #Цикл for перебирает все группы group из numgroup1 и выводит их на печать.
    print(*group)
print('###########################################')
#ЗАдание3

car_brands = ["Toyota", "Honda", "BMW"]
car_numbers = ["ABC123", "DEF456", "GHI789"]
car_owners = [["John"], ["Alice", "Bob"], ["Emily", "David","Sin"]]

# Объединяем списки в зип
car_data = zip(car_brands, car_owners, car_numbers)
for data in car_data:
    print(*data)


# Добавление новой машины
new_brand = input("Введите марку новой машины: ")
new_number = input("Введите номер новой машины: ")
new_owners = input("Введите список владельцев новой машины (через запятую): ").split(",")

car_brands.append(new_brand)
car_numbers.append(new_number)
car_owners.append(new_owners)

car_data = zip(car_brands, car_owners, car_numbers)
for data in car_data:
    print(*data)
# Удаление машины по номеру
remove_number = input("Введите номер машины для удаления: ")
if remove_number in car_numbers:
    index = car_numbers.index(remove_number)
    car_brands.pop(index)
    car_numbers.pop(index)
    car_owners.pop(index)
    print("Машина успешно удалена.")
else:
    print("Машина с таким номером не найдена.")

car_data = zip(car_brands, car_owners, car_numbers)
for data in car_data:
    print(*data)
# Поиск машины по номеру
search_number = input("Введите номер машины для поиска: ")
if search_number in car_numbers:
    index = car_numbers.index(search_number)
    print("Марка авто:", car_brands[index])
    print("Список владельцев:", car_owners[index])
else:
    print("Машина с таким номером не найдена.")