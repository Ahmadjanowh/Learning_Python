# Строки и метод строк 

# name = "Hikmatulloh"    #  двойные кавычки
# surname = 'Ahmadjanow'  #  используем одинарные кавычки
# bio = """
# Ahmadjanow Hikmatillo
# Backend Python Developer
# """
# print(name)
# print(surname)
# print(bio)

"""
Мы получим следующее:

Hikmatulloh
Ahmadjanow

Ahmadjanow Hikmatillo
Backend Python Developer

"""
# text = 'Hi i'm Hikmatulloh' # получаем ошибку 
# первый вариант 
# text = 'Hi i\'m Hikmatulloh'
# print(text)
# второй вариант
# text = "Hi i'm Hikmatulloh"
# print(text)

# Конкантенация
# bio = "Hi" + " i'm" + " Hikmatulloh"
#  обратите внимание на пробелы. Пробел для питона считается отдельным символом
# print(bio)

# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# age = int(input('Введите возврост: '))

# print(name + " " + surname + ". Он(а) " + str(age) + " лет")

# Форматирование строк
# brand = 'Tesla'
# model = 'Models X'

# print('Бренд: {} модель: {}'.format(brand,model))
# print(f'Бренд: {brand} модель: {model}') # сокрошенный вариант 

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))

# print(f'{num1} + {num2} = {num2 + num2}')


# Методы сстрок 
text = 'hi Ken'
print(text.capitalize())    # : Возвращает строку с первой буквой в верхнем регистре
print(text.casefold())    # : Возвращает строку в нижнем регистре, пригодную для сравнения без учета регистра
print(text.count('h'))     # : Возвращает количество вхождений подстроки в строку.
print(text.find('h'))       # : Возвращает индекс первого вхождения подстроки в строку (или -1, если подстрока не найдена).
print(text.replace('h','O'))    # : Заменяет все вхождения подстроки в строке другой подстрокой.
print(text.split(' '))  # Разбивает строку на список подстрок по заданному разделителю.
print(text.strip())     # : Удаляет пробельные символы с начала и конца строки.
print(text.lower())     # : Возвращает строку в нижнем регистре.
print(text.upper())      # : Возвращает строку в верхнем регистре.
print(text.startswith('n')) # : Проверяет, начинается ли строка с определенной подстроки.
print(text.endswith('n')) # : Проверяет, заканчивается ли строка определенной подстрокой.
print(text.isalpha()) # : Проверяет, содержит ли строка только буквы.
print(text.isdigit()) # : Проверяет, содержит ли строка только цифры.
print(text.isspace()) # : Проверяет, состоит ли строка только из пробельных символов.
