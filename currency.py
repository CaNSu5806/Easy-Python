import requests

# API key and base URL
api_key = "{your_api}"
base_url = "https://v6.exchangerate-api.com/v6/{your_api}/latest/"

# Get input from the user
exchange_currency = input("Enter the currency you have (e.g., TRY) : ").upper()
foreign_exchange_received = input("Enter the currency you want to convert to (e.g., EUR): ").upper()

try:
    amount = float(input("Enter the amount: "))
except ValueError:
    print("ERROR, you entered invalid value")
    exit()

api_url = f"{base_url}{exchange_currency}"

try:
    #Make the API request
    response = requests.get(api_url)
    response.raise_for_status() # To error HTTP status codes
    data = response.json()
    
    if foreign_exchange_received in data.get("conversion_rates",{}):
        rate = data["conversion_rates"][foreign_exchange_received]
        new_amount = amount*rate
        print(f"{amount} {exchange_currency} = {new_amount:.2f} {foreign_exchange_received}")
    else:
        print(f"Error:Conversion rate for '{foreign_exchange_received}' was not found.")
        exit()
        
except requests.exceptions.RequestException as x:
    print(f"API request failed:{x}")
except KeyError:

    print("API response structure is incorrect or you entered an invalid currency code.")
