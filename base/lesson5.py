# Списки картежи 

# Типы данных
# int , float, str, bool, list, tuple

numbers = [12,3,4,5,23,43]
        #   0 1 2 3 4  5
# начало:конец:шаг
# print(numbers)
# print(numbers[1])
# print(numbers[2:5]) # От 2 до 5 
# print(numbers[1:5:2])
# print(numbers[-2:])
# print(numbers[1:4])
# print(numbers[::-1])

# name =  input("Хотите узнать как будет ваша имя \n в повернутом формате ПИШИТЕ СВОе ИМЯ: ")
# print(name[::-1])

# student = ['Hikmatulloh','Ahmadjanow',12]
# print(f"Имя: {lst[0]} Фамилия: {lst[1]} Возврост: {lst[2]}")

# lst = [12,'go',12.12,False,[12,32],12]
# ex = [23,24,1,2]
# lst.append(23) #  Добавляет элемент в конец списка.
# print(lst) 
# lst.extend(ex) #  Расширяет список, добавляя элементы из другого списка или итерируемого объекта в конец.
# print(lst)
# lst.insert(0,"insert") # Вставляет элемент в определенную позицию списка.
# print(lst)
# lst.remove(12) # Удаляет первое вхождение указанного элемента из списка.
# print(lst)
# lst.pop(2) #  Удаляет элемент по индексу и возвращает его. Если индекс не указан, удаляется и возвращается последний элемент.
# print(lst)
# print(lst.count(12)) # Возвращает количество вхождений указанного элемента в списке.
# lst.reverse() # : Изменяет порядок элементов в списке на обратный.
# print(lst)
# ex.sort()  # Сортирует элементы списка по возрастанию (или в порядке, заданном параметром reverse=True для сортировки по убыванию).
# print(ex)
# lst.clear() # Удаляет все элементы из списка.
# print(lst)

students = []
# while True:
#     opt = int(input("Выберити действие 1-добавить 2-список 3-выйти"))
#     if opt == 1:
#         name = input("Имя: ")
#         surname = input("Фамилия: ")
#         year = input("Дата рождение: ")
#         grup = input("Группа: ")

#         student = [name,surname,year,grup]
#         students.append(student)

#         print(f"Студент {name} успешно добавлен!")
#     elif opt == 2:
#         n = 1
#         for item in students:
#             print(n,'.',str(item).replace('[',' ').replace(']',' ').replace("'"," ").replace(',',""))
#             n += 1
#     elif opt == 3:
#         break
#     else:
#         print("Неверный действие!!!")

"""
Картежи тоже точно также как список 
но не изменяемый тип данных и создайотс через круглые скобки ()
"""
items = ("hello",12,234.23,True,[12,243,13],(232,435,5))
print(items)
print(type(items))
# Чтобы изменить картеж можно сделать его списка потом обратно картеж 
items = list(items)
print(type(items))
items.append('Hikmatulloh')
print(items)
items = tuple(items)
print(type(items))
