from src.item import Item


class Phone(Item):
    """Класс для представления категории товара "телефон". Содержит все атрибуты класса Item и
        дополнительно атрибут, содержащий количество поддерживаемых сим-карт"""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)

    @property
    def number_of_sim(self):
        return self.number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, num_sim):
        if num_sim > 0:
            self.number_of_sim = num_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"



