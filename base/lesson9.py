# Декароторы

def my_decor(func):
    def warper(n):
        print("start")
        func(n)
        print('end')
    return warper

@my_decor
def my_func(number):
    print(number ** 2)
my_func(10)