
def calculate_savings():
    try:
        income= float(input("Enter monthly income : "))
        expenses= float(input("Enter monthly expenses: "))

        savings= income - expenses

        print(f"your monthly net savings is {savings}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

calculate_savings()
