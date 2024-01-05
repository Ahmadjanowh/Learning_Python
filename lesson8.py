# Исключение, Работа с файлами

def calculator(num1,num2):
    try:
        return num1 + num2 
    except TypeError:
        return "Не правильный тип данных"
# print(calculator('dal',23))

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Ошибка! Неправильный формат числа")

# try:
#     print(10/0)
# except Exception  as error:
#     print("Ошика",error)

# Работа с файлами

# 'a' - режим добавления
file = open('text.txt', 'a') 
file.close() # Закрытие файла
 
# 'w' - режим записи
write = open('text.txt', 'w')
write.write("Hello world")
write.close() # Закрытие файла

# 'r' - режим чтения
read = open('text.txt', 'r', encoding='utf-8') # encoding='utf-8' - кодирование 
print(read.read()) # Выводить сожержимое в файле Hello world
read.close() # Закрытие файла

# Также рекомендуется использовать конструкцию with, 
# которая автоматически закрывает 
# файл после завершения операций с ним

with open('text.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content) 
# Файл будет автоматически закрыт после завершения блока кода

