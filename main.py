from sqlite3 import converters
from currency_converter import CurrencyConverter
from config import API_KEY

def main():
    print("\n--- Calculadora de divisas ---")
    print("1. Convertir divisas")
    print("2. Salir")

    choice = input("Elige una opción: ")

    if choice == '1':
        from_currency = input("Divisa de origen (por ejemplo, USD): ").upper()
        to_currency = input("Divisa de destino (por ejemplo, EUR): ").upper()
        amount = float(input(f"Cantidad en {from_currency}: "))
        
        
        rate = converters.get_exchange_rate(from_currency, to_currency)
        
        if rate:
            converted_amount = amount * rate
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            print("Error al obtener la tasa de cambio.")
    
    elif choice == '2':
        print("Saliendo de la calculadora.")
    
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
