def main():
    print("Welcome to my Converter")
    
    while True:
        print("Enter what do you wnat to do (1,2,3)")
        print("1.Convert Currency ")
        print("2.Convert Temperature")
        print("3.exit")
        
        user = int(input("Enter yoyr choice \n"))
        if user == 1:
            currency_converter()
        if  user == 2:
            temperature()
        if user == 3:
            break
        else:
            continue
        
def temperature():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius}°C")
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C is {kelvin}K")
    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin}K is {celsius}°C")
    else:
        print("Invalid choice!")
        
def currency_converter():
    print("\nCurrency Converter")
    print("1. USD to NPR")
    print("2. NPR to USD")

    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        usd = float(input("Enter amount in USD: "))
        npr = usd * 132.0  # Approximate exchange rate
        print(f"${usd} USD is {npr} NPR")
    elif choice == 2:
        npr = float(input("Enter amount in NPR: "))
        usd = npr / 132.0  # Approximate exchange rate
        print(f"{npr} NPR is ${usd:.2f} USD")
    else:
        print("Invalid choice!")
        
        
        
if __name__ == "__main__":
    main()