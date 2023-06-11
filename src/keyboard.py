from src.item import Item

class MixinLanguages:
    '''
    Миксин-класс для хранения и изменения раскладки клавиатуры
    '''

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):
        '''
        Метод для изменения языка (раскладки клавиатуры)
        '''

        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'EN':
            self.__language = 'RU'
        else:
            return self

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLanguages, Item):
    def __init__(self, name, price, quantity) :
        super().__init__(name, price, quantity)

'''
kb = Keyboard('Dark Project KD87A', 9600, 5)
print(str(kb)) # == "Dark Project KD87A"
print(str(kb.language)) #== "EN"
    
kb.change_lang()
print(str(kb.language)) # == "RU"
    
        # Сделали RU -> EN -> RU
kb.change_lang().change_lang()
print(str(kb.language)) #== "RU"

kb.language = 'CH'
    # AttributeError: property 'language' of 'KeyBoard' object has no setter
'''