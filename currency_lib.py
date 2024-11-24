from forex_python.converter import CurrencyRates

def convert_currency(base_currency, target_currency, amount):
    c = CurrencyRates()

    try:
        rate = c.get_rate(base_currency, target_currency)
        return rate * amount
    except Exception as e:
        raise ValueError("Failed to fetch exchange rates. Ensure the currency codes are valid.") from e