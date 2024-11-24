from currency_lib import convert_currency

def main():
    while True:
        try:
            base_currency = input("Enter the base currency (e.g., USD) or type 'exit' to quit: ").upper()
            if base_currency == 'EXIT':
                print("Goodbye!")
                break

            target_currency = input("Enter the target currency (e.g., EUR): ").upper()
            amount = float(input("Enter the amount to convert: "))

            converted_amount = convert_currency(base_currency, target_currency, amount)
            print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}.\n")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()