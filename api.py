import requests

def convert_currency():

        url = "https://api.frankfurter.dev/v2/rates"

        base = input("What do you want to convert?: ").upper()
        quotes = input("What do you want to convert to?: ").upper()

        try:
            amount = float(input("How much do you want to convert?: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        if base == quotes:
            print("Both currencies are the same.")
            return

        params = {
            "base": base,
            "quotes": quotes
        }

        try:
            response = requests.get(url, params=params, timeout=5)
        except requests.exceptions.Timeout:
            print("The server took too long to respond.")
            return
        except requests.exceptions.ConnectionError:
            print("No internet connection.")
            return

        if response.status_code != 200:
            print("Invalid currency code!")
            return
        data = response.json()
        rate = data[0]["rate"]

        current_amount = amount * rate

        print(f"\nExchange rate: 1 {base} = {rate:.4f} {quotes}")
        print(f"{amount} {base} = {current_amount:.2f} {quotes}")

def is_supported_currency():

    url = "https://api.frankfurter.dev/v2/rates"

    currency = input("What currency do you want to check?: ").upper()
    params = {
        "base": currency,
        "quotes": currency
    }

    try:
        response = requests.get(url, params=params, timeout=5)
    except requests.exceptions.Timeout:
        print("The server took too long to respond.")
        return
    except requests.exceptions.ConnectionError:
        print("No internet connection.")
        return
    data = response.json()

    if not data or "status" in data:
        print("This currency is not supported.")
        return None

    else:
        print("This currency is supported.")
        return True

def make_choice():
    while True:
        print("1. Check Supported Currency")
        print("2. Convert Currency")
        print("3. Exit")

        choice = (input("What would you like to do?: "))

        if choice == "1":
            is_supported_currency()

        elif choice == "2":
            convert_currency()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    make_choice()