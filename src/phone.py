from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_cards_num: int):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный код
        self.__sim_cards_num = sim_cards_num

    @property
    def sim_cards_num(self):
        return self.__sim_cards_num

    @sim_cards_num.setter
    def sim_cards_num(self, value):
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__sim_cards_num = value

    def __repr__(self):
        """Метод вывода новый"""
        parent_repr = super().__repr__()
        return f"{parent_repr.split(',')[0]}, {self.price}, {self.quantity}, {self.__sim_cards_num})"


