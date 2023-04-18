import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        """Реализация геттера для name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Реализация сеттера для name"""
        if len(value) >= 10:
            print("Длина наименования товара превышает 10 символов")
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def __repr__(self):
        """метод вывода"""
        class_name = self.__class__.__name__
        return f"{class_name}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @classmethod
    def instantiate_from_csv(cls):
        """Открытие файла csv"""
        cls.all = []
        with open("items.csv", encoding="utf8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name = row[0]
                price = int(row[1])
                quantity = int(row[2])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(number: str):
        """ Статик метод, возвращающий число из числа-строки"""
        int_number = int(number)
        return int_number


