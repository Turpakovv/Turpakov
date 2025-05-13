from task_1 import Laptop, Movie, BankAccount  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
        laptop = Laptop("Dell", "XPS 13", 16)
        laptop.upgrade_ram(-4)  # Должно вызвать исключение
    except ValueError:
        print(f"Ошибка: неправильные данные")

    try:
        movie = Movie("Inception", "Christopher Nolan", 148)
        movie.watch(-10)  # Должно вызвать исключение
    except ValueError:
        print(f"Ошибка: неправильные данные")

    try:
        account = BankAccount("123456789", 1000.0)
        account.withdraw(2000.0)  # Должно вызвать исключение
    except ValueError:
        print(f"Ошибка: неправильные данные")