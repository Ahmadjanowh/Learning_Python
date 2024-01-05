# Условие if else elif 

# Регитьрация на лагер
# print('Региструйся чтобы попасть в летний лагерь!!!')
# name = input('Имя: ')
# surname = input('Фамилия: ')
# age = int(input("Возврост: "))

# if age > 18:
#     print("Регистрация успешно пройден !")
# else:
#     print("Вы не совершено лентий ")

# Проверка на чотность 
# num = int(input("Введите число: "))
# if num / 2 == 0:
#     print('Чотная число')
# else:
#     print("Не чотная число")

# Оценка успеваемости:
# ball = int(input('Ваш бал: '))

# if ball >= 60 and ball < 90:
#     print('Проходной балл достигнут')
# elif ball < 60 and ball > 0:
#     print("Требуется больше усилий")
# elif ball >= 90 and ball <= 100:
#     print("Супер!!!")
# else:
#     print("Щутите! ")

# Калькулятор 
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
options = input("Введите опцию +, -, *, /")

if options == '+':
    print(num1 + num2)
elif options == '-':
    print(num1 - num2)
elif options == '*':
    print(num1 * num2)
elif options == '/':
    print(num1 / num2)
else:
    print("Неверный опиратов !!!!")

