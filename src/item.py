from csv import DictReader
from os import path
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name #делаем атрибут приватным
        self.price = price
        self.quantiti = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter

    def name(self, new_name: str) -> None:
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantiti

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        '''Класс-метод, инициализирующий экземпляры класса `Item`данными из файла ../src/items.csv'''
        cls.all.clear()
        with open(path.join('..', 'src', 'items.csv'), 'r', encoding='cp1251') as csvfile:
            data = DictReader(csvfile)
            for i in data:
                cls(i['name'], i['price'], i['quantity'])

    @staticmethod

    def string_to_number(number):
        '''Cтатический метод, возвращающий число из числа-строки'''
        return int(float(number))


