# Регудярное выражение 

import re 

# part1
s = 'AC/AC/AC/DC/DC/AC/DC/AC/DC/CA/CA'
result = re.match('DC',s) # ишет в начале строки 
result = re.search('DC',s) # ишет и возврашает первый
result = re.findall('DC',s) # шет все и возврашает список 
result = re.split('/',s,maxsplit=3)  # разбивает и возврашает список maxsplit=3 ограничение на разюиение 
result = re.sub('A','D',s)  # Заменит символы
result = re.fullmatch('A',s) # Является ли шаблон полным совпадением 
# print(result)

#part2 
s = "87242+684654    - ------ kjgufhohiuoheriobei493583, NHFHKFHKNF KNF fvknfdkjvn"
result = re.search(r"k.g",s) # одна точка это лбой символ кроме символа новой строки 
result = re.search(r"\d\d\d\d\d",s) # выведить рандомую цифру, если большой буква D рандомный символ
result = re.search(r"\s",s) # Лябой пробелный символ, если большой S любой без пробелный символ
result = re.search(r"\w",s) # Любая буква цифра и нижная подчоркивание _, если большой W набарот
result = re.search(r"\B KNF",s) # Начало и конец слова, если большой не укажут нам границу слова 
result = re.search(r"\d*",s) # Ноль или более вхождение наших симоволов после нашей найдеггый цифры 
result = re.search(r"\d+",s) # одно или более фхождение 
result = re.search(r"[gjkjd]",s) # определонный набор символов  
result = re.search(r"[4-8]",s)  # цифры от 4 до 8 
result = re.search(r"[^4-8]",s) # всен кроме деапазона 4-8
result = re.search(r"H|F",s) # Выведить либо H либо F 
result = re.search(r"\d{3}",s) # кватификаторы выведить 3 цифры 
result = re.search(r"\d{1,3}",s) #от одного до третий 
result = re.search(r"\d{4,}",s) # немене 4 цфр
result = re.search(r"\d{,3}",s) # не более 3 цфр
# print(result)

text = "Привет! как дела? А у меня нормально."

# Функция для поиска слов котрые начинаеться с согласними буквами 
def get_soglas(text):
    out = re.findall(r"[бвгджзклмнпрстфтхчшщБВГДЖЗКЛПРСТФТЧШЩ]\w+",text)
    return out

if __name__=='__main__':
    print(get_soglas(text))

"""
Конструкция if __name__ == '__main__': 
в Python используется для определения точки входа в программу. 
Этот блок кода позволяет проверить, запущен ли скрипт напрямую, 
или же он был импортирован в другой модуль.

Если файл запускается напрямую (то есть является точкой входа), 
код внутри блока if __name__ == '__main__': будет выполнен.
Если файл импортируется в другой скрипт, 
код внутри этого блока не будет выполнен, 
но другие функции и классы, определенные в этом файле, 
будут доступны для использования в импортирующем файле.
Это полезно, когда вы хотите, чтобы часть кода работала только 
при запуске файла напрямую, а не при импорте. Например, 
вы можете поместить в этот блок код, который запускает 
какие-то тесты или выполняет определенные действия, которые 
должны происходить только при запуске самого файла, 
но не при его импорте

"""
