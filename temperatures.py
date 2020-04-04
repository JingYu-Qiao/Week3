def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice=="C":
            choice=choose_C()
        elif choice=="F":
            choice=choose_F()
        else:
            print("Invalid option")
        print(choice)
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def choose_C():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def choose_F():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9.0
    return celsius

main()