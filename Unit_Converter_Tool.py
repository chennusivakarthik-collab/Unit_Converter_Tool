def length_converter():
    print("\nLength Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"Result: {value * 0.621371:.2f} Miles")
    elif choice == 2:
        print(f"Result: {value / 0.621371:.2f} Kilometers")
    else:
        print("Invalid Choice")


def weight_converter():
    print("\nWeight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"Result: {value * 2.20462:.2f} Pounds")
    elif choice == 2:
        print(f"Result: {value / 2.20462:.2f} Kilograms")
    else:
        print("Invalid Choice")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"Result: {(value * 9/5) + 32:.2f} °F")
    elif choice == 2:
        print(f"Result: {(value - 32) * 5/9:.2f} °C")
    else:
        print("Invalid Choice")


def time_converter():
    print("\nTime Converter")
    print("1. Hours to Minutes")
    print("2. Minutes to Hours")
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"Result: {value * 60:.2f} Minutes")
    elif choice == 2:
        print(f"Result: {value / 60:.2f} Hours")
    else:
        print("Invalid Choice")


while True:
    print("\n==============================")
    print("     UNIT CONVERTER")
    print("==============================")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    print("4. Time Converter")
    print("5. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        length_converter()
    elif option == 2:
        weight_converter()
    elif option == 3:
        temperature_converter()
    elif option == 4:
        time_converter()
    elif option == 5:
        print("Thank you for using Unit Converter!")
        break
    else:
        print("Invalid Option! Please try again.")