# Работа с модулём os 
import os 

# print("Текушая дериктори: ",os.getcwd()) # Текущая дериктория 

# os.mkdir('test_os') # Создание новой папки в текушим дериктории

# Создайом папку если оно не создано 
if not os.path.isdir('test_os'):
    os.mkdir('test_os')

os.chdir('test_os') # Перейти в дерикторию 
# print("Текушая дериктори: ",os.getcwd()) # Проверям текушею дерикторию чтобы убидиться 

os.chdir('..') # Верномся в пережную дерикторию 
# print("Текушая дериктори: ",os.getcwd()) # Проверям текушею дерикторию чтобы убидиться 

# создайом текстовой файл 
# file = open('txt.txt','w',encoding='utf-8')
# file.write("Это текстовой файл!")
# file.close()

# Изменяем название файла
# os.rename('txt.txt','update.txt')

# Переместим это файл 
# os.replace('update.txt','test_os/update.txt')

# название фойлов и папок в текушем жериктории 
# print(os.listdir())

# Проверяем все файлы и папки в дериктории и все файлы и папки в этик папок (только я пйому)
# for dirpach, dirnames, filenames in os.walk('.'):
#     for dirname in dirnames:
#         print('Каталог: ',os.path.join(dirpach,dirname))
#     for filename in filenames:
#         print("Файлы: ",os.path.join(dirpach, filename))
    
# Удаление файла 
# os.remove('test_os/update.txt')

#удаление папки 
os.rmdir('test_os')

f = open('test.txt', 'w')
f.write("Test")
f.close()
#Информатция о файле 
# print(os.stat('test.txt'))

# имя пользователя, вошедшего в терминал 
print(os.getlogin())

# Копирование данных с одной папки в другой папку 

import shutil

# Путь к исходной папке, откуда будут копироваться файлы
source_folder = 'cpi/'
# Путь к целевой папке, куда будут скопированы файлы
target_folder = 'past'

# Получение списка файлов в исходной папке
file = os.listdir(source_folder)

# Копирование каждого файла из исходной папки в целевую папку
for file_name in file:
    # Формируем полные пути к файлам
    source_file = os.path.join(source_folder,file_name)
    target_file = os.path.join(target_folder,file_name)

    # Копируем файл из исходной папки в целевую
    shutil.copy(source_file,target_file)