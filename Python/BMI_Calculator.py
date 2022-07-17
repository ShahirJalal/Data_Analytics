
def get_input():
    height = float(input("Input your height in meter: "))
    weight = int(input("Input your weight in kilo: "))
    return height, weight

def BMI_calculator(height, weight):
    BMI = weight/(height**2)
    if BMI < 18.5:
        print("you are underweight")
    elif BMI >= 18.5 and BMI <= 24.9:
        print("You are normal weight")
    elif BMI >= 25.0 and BMI <= 29.9:
        print("You are overweight")
    elif BMI >= 30.0 and BMI <= 34.9:
        print("You are Obesity Class I")
    elif BMI >= 35.0 and BMI <=39.9:
        print("You are Obesity Class II")
    else:
        print("You are Obesity Class III")
    return BMI

def main():
    height, weight = get_input()
    BMI = BMI_calculator(height, weight)
    print(round(BMI,2))

main()