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

def decorate(func):
    def warper(*args):
        print("Всем привет: ")
        func(*args)
        print('А мы с табой увидемся в следший раз: ')
    return warper()

@decorate
def get_links(instagram,github):
    print(f"""
        Instagram: https://instagram.com/h.ahmadjanow {instagram},
        Github: https://github.com/Ahmadjanowh {github}
        """)
    
# decorate(get_links)
