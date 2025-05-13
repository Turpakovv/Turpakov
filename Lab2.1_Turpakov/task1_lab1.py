import doctest
class Laptop:
    """
    Класс, описывающий ноутбук.
    """

    def __init__(self, brand: str, model: str, ram: int):
        """
        Инициализирует объект Laptop.
        Args:
            brand (str): Бренд ноутбука. Не может быть пустой строкой.
            model (str): Модель ноутбука. Не может быть пустой строкой.
            ram (int): Объем оперативной памяти в ГБ. Должен быть положительным числом.
        Raises:
            ValueError: Если brand, model пустые строки или ram не положительное число.
        Примеры:
        >>> laptop = Laptop("HONOR", "MagicBook 14", 16) # Corrected example
        """
        if not brand:
            raise ValueError("Бренд не может быть пустым.")
        if not model:
            raise ValueError("Модель не может быть пустой.")
        if ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным числом.")
        self.brand: str = brand
        self.model: str = model
        self.ram: int = ram

    def upgrade_ram(self, additional_ram: int) -> None:
        """
        Увеличивает объем оперативной памяти.
        Args:
            additional_ram (int): Дополнительный объем оперативной памяти в ГБ. Должен быть положительным числом.
        Raises:
            ValueError: Если additional_ram не положительное число.
        Примеры:
        >>> laptop = Laptop("HONOR", "MagicBook 14", 16) #Corrected example
        >>> laptop.upgrade_ram(8)
        Объем оперативной памяти увеличен на 8 ГБ. Текущий объем: 24 ГБ.
        """
        if additional_ram <= 0:
            raise ValueError("Дополнительный объем оперативной памяти должен быть положительным числом.")
        self.ram += additional_ram
        print(f"Объем оперативной памяти увеличен на {additional_ram} ГБ. Текущий объем: {self.ram} ГБ.")

    def get_specs(self) -> str:
        """
        Возвращает характеристики ноутбука.
        Returns:
            str: Строка с характеристиками ноутбука.
        Примеры:
        >>> laptop = Laptop("HONOR", "MagicBook 14", 16) #Corrected example
        >>> laptop.get_specs()
        'Бренд: HONOR, Модель: MagicBook 14, ОЗУ: 16 ГБ'
        """
        return f"Бренд: {self.brand}, Модель: {self.model}, ОЗУ: {self.ram} ГБ"


class Movie:
    """
    Represents a movie with its title, director, and duration.
    """

    def __init__(self, title: str, director: str, duration: int):
        """
        Initializes a Movie object.
        Args:
            title (str): The title of the movie.
            director (str): The director of the movie.
            duration (int): The duration of the movie in minutes. Must be positive.
        Raises:
            ValueError: If the duration is not a positive integer.
        """
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        self.title: str = title
        self.director: str = director
        self.duration: int = duration

    def watch(self, minutes: int) -> str:
        """
        Simulates watching a movie for a certain number of minutes.
        Args:
            minutes (int): The number of minutes to watch. Must be positive.
        Returns:
            str: A message about the viewing.
        Examples:
        >>> movie = Movie("Lord of the Rings", "Peter Jackson", 558)
        >>> movie.watch(30)
        'Вы посмотрели 30 минут фильма Lord of the Rings.'
        """
        if minutes <= 0:
            raise ValueError("Количество минут должно быть положительным числом.")
        return f"Вы посмотрели {minutes} минут фильма {self.title}."

    def is_long(self, threshold: int = 120) -> bool:
        """
        Checks if the movie is long based on the given threshold.
        Args:
            threshold (int): The duration threshold in minutes.
        Returns:
            bool: True if the movie is long, False otherwise.
        Examples:
        >>> movie = Movie("Lord of the Rings", "Peter Jackson", 558)
        >>> movie.is_long()
        True
        """
        return self.duration > threshold


class BankAccount:
    """
    A class describing a bank account.
    """

    def __init__(self, account_number: str, balance: float):
        """
        Initializes a BankAccount object.
        Args:
            account_number (str): The account number. Cannot be an empty string.
            balance (float): The account balance. Must be non-negative.
        Raises:
            ValueError: If account_number is empty or balance is negative.
        Examples:
        >>> account = BankAccount("123456789", 1000.0)
        """
        if not account_number:
            raise ValueError("Account number cannot be empty.")
        if balance < 0:
            raise ValueError("Balance must be non-negative.")
        self.account_number: str = account_number
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        """
        Deposits money into the account.
        Args:
            amount (float): The amount to deposit. Must be positive.
        Raises:
            ValueError: If amount is not positive.
        Examples:
        >>> account = BankAccount("123456789", 1000.0)
        >>> account.deposit(500.0)
        На счет внесено 500.0 единиц. Текущий баланс: 1500.0 единиц.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"На счет внесено {amount:.1f} единиц. Текущий баланс: {self.balance:.1f} единиц.")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws money from the account.
        Args:
            amount (float): The amount to withdraw. Must be positive and not exceed the current balance.
        Raises:
            ValueError: If amount is not positive or exceeds the current balance.
        Examples:
        >>> account = BankAccount("123456789", 1000.0)
        >>> account.withdraw(200.0)
        Со счета снято 200.0 единиц. Текущий баланс: 800.0 единиц.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Withdrawal amount cannot exceed the current balance.")
        self.balance -= amount
        print(f"Со счета снято {amount:.1f} единиц. Текущий баланс: {self.balance:.1f} единиц.")

    def get_balance(self) -> float:
        """
        Returns the current account balance.
        Returns:
            float: The current account balance.
        Examples:
        >>> account = BankAccount("123456789", 1000.0)
        >>> account.get_balance()
        1000.0
        """
        return self.balance


if __name__ == "__main__":
    doctest.testmod()