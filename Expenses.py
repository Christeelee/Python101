
def calculate_bmi():
    try:
        h = float(input("Enter height in meters: "))
        w = float(input("Enter weight in kg: "))

        bmi = w / (h ** 2)

        classification = ""
        if bmi < 18.5:
            classification = "Underweight"
        elif bmi < 25:
            classification = "Normal"
        elif bmi < 30:
            classification = "Overweight"
        else:
            classification = "Obese"

        print(f"BMI Calculator: {bmi:.2f} ({classification})")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

calculate_bmi()
