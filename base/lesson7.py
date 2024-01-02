# Функция Анониманая функция(lambda)

# В Python функция - это блок кода, 
# который выполняет определённую задачу и
#  может быть вызван из других частей программы 
# для выполнения этой задачи.

def greet(name):
    """Функция привествие"""
    print(f"Привет, {name}!")

# Вызов функции
greet('Hikmatulloh')

def calculator(num1,num2):
    """Функция для сложение двух чисел"""
    return f"{num1} + {num2} = {num1 + num2}"

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(calculator(num1,num1))

def chis(number):
    """Функция для проверки число на чотност"""
    if number % 2 == 0:
        return True
    return False
print(chis(12))
print(chis(3))

def sum_numbers(nums):
    """Функция для подсчёта суммы чисел в списке"""
    return sum(nums)

nums = [12,32,43]
print(sum_numbers(nums))

def find_max(numbers):
    return max(numbers)
print(find_max(nums))

def summa(a,b,c):
    print(a,b,c)
summa(b=23,c=34,a=67) # Именованный аргумент 

# *args **kwargs

def summa(*args):
    print(sum(args))
summa(7,24,5,5,64)

def brand(**kwargs):
    print(type(kwargs)) 
    for x,y in kwargs.items():
        print(x,":",y)
brand(a='Apple',s='Samsung')

# Lambda

# Обычная функция
def rectangle_area(a,b):
    return a * b 
print(rectangle_area(17,12))
# lambda функция 
print((lambda a,b: a * b)(17,14))

def maximum(a,b):
    if a > b:
        return a
    else:
        return b 
print(maximum(15,12))

print((lambda a,b: a if a > b else b)(13,5))

# Филтрация списка с lambda
my_list = [1,2,3,4,5,6,7,8,9,10]
even_list = list(filter(lambda x: x % 2 == 0,my_list))
print(even_list)