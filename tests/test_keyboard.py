from src.keyboard import Keyboard
import pytest

@pytest.fixture
def test_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_init(test_keyboard):
    assert test_keyboard.name == 'Dark Project KD87A'
    assert test_keyboard.price == 9600
    assert test_keyboard.quantity == 5
    assert test_keyboard.language == 'EN'


def test_change_lang(test_keyboard):
    assert test_keyboard.language == 'EN'
    test_keyboard.change_lang()
    assert test_keyboard.language == 'RU'
    test_keyboard.change_lang().change_lang()
    assert test_keyboard.language == 'RU'