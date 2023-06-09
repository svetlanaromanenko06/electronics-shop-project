from src.phone import Phone
import pytest

@pytest.fixture
def test_phone():
    return Phone('iPhone 14', 120_000, 5, 2)

def test_repr(test_phone):
    assert repr(test_phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_phone_init(test_phone):
    assert test_phone.number_of_sim == 2
    assert test_phone.name == 'iPhone 14'
    assert test_phone.price == 120000
    assert test_phone.quantity == 5


def test_number_of_sim_errors(test_phone):
    with pytest.raises(ValueError):
        test_phone.number_of_sim = -1
        test_phone.number_of_sim = 0

