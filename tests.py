import pytest
from unittest import TestCase
from forex_python.converter import CurrencyRates
from currency_lib import convert_currency

@pytest.fixture
def real_exchange_rates():
    c = CurrencyRates()
    return c.get_rate('USD', 'EUR')


def test_convert_currency_success(real_exchange_rate):
    expected_converted_amount = 100 * real_exchange_rate
    converted_amount = convert_currency('USD', 'EUR', 100)
    tolerance = 0.05
    assert abs(converted_amount - expected_converted_amount) <= tolerance, \
        f"Expected {expected_converted_amount:.2f}, but got {converted_amount:.2f}"
    

def test_convert_currency_invalid_currency():
    with pytest.raises(ValueError):
        convert_currency('INVALID', 'EUR', 100)


def test_convert_currency_zero_amount():
    converted_amount = convert_currency('USD', 'EUR', 0)
    assert converted_amount == 0, f"Expected 0 but got {converted_amount}"


def test_convert_currency_same_currency():
    converted_amount = convert_currency('USD', 'USD', 100)
    assert converted_amount == 100, f"Expected 100 but got {converted_amount}"