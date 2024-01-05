# Set frozenset Dict 

# Типы данных 
# int, float , str, bool, list, tuple, set, frozenset, dict

# Повторение
lst = [x for x in range(1,21) if x % 2 == 0]
print(lst)
lst = [x ** 2 for x in range(1,11)]
print(lst)

my_list = [11,23,34,11,56,11]
print(my_list)
my_set = set(my_list) # тип данных set
print(my_set)

numbers = {12,23,43,12,23,1,1} 
num2 = {123,34,5,46,43}
print(numbers)
# print(numbers[1]) у set нет определонной структуры 

# Методы set 
print(numbers.add(34)) # Добавляет элемент 
print(numbers.remove(12)) # Удаляет указный элемент вызывает ошибку если элемент не неайден 
print(numbers.discard(5)) # Удаляет указенный элемент но не вызывает ошибку если элемент не найден 
print(numbers.pop()) # Удаляет рандомный элемент
print(numbers.union(num2)) # Возвращает объединение двух множеств
print(numbers.intersection(num2)) # Возвращает пересечение двух множеств (новое множество, содержащее только общие элементы).
print(numbers.clear())

# Frozen точно также как set Но оно не изменяемый тип данных 
frzset = frozenset({12,324,535,546,12,324})
print(frzset)