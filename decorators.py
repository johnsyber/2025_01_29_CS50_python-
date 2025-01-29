def announce(f):
    def wrapper():
        print("Запуск функції")
        f()
        print("Завершення роботи функції")
    return wrapper

@announce
def hello():
    print("Привіт, світе!")

hello()