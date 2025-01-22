def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def menu():
    print("Convertisseur de Température")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Quit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        return menu()
    return choice

def main():
    choice = menu()
    while choice != 7:
        if choice == 1:
            celsius = float(input("Enter your Celsius temperature: "))
            print("Fahrenheit:", celsius_to_fahrenheit(celsius), "°F\n")
        elif choice == 2:
            fahrenheit = float(input("Enter your Fahrenheit temperature: "))
            print("Celsius:", fahrenheit_to_celsius(fahrenheit), "°C\n")
        elif choice == 3:
            celsius = float(input("Enter your Celsius temperature: "))
            print("Kelvin:", celsius_to_kelvin(celsius), "K\n")
        elif choice == 4:
            kelvin = float(input("Enter your kelvin temperature: "))
            print("Celsius:", kelvin_to_celsius(kelvin), "°C\n")
        elif choice == 5:
            fahrenheit = float(input("Enter your Fahrenheit temperature: "))
            print("Kelvin:", fahrenheit_to_kelvin(fahrenheit), "K\n")
        elif choice == 6:
            kelvin = float(input("Enter your kelvin temperature: "))
            print("Fahrenheit:", kelvin_to_fahrenheit(kelvin), "°F\n")
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
        choice = menu()
    print("Goodbye!")
    return 0

if __name__ == "__main__": 
    main()