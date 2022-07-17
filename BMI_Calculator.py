height = float(input("Input your height in meter: "))
weight = int(input("Input your weight in kilo: "))

BMI = weight/(height**2)

print(round(BMI,3))

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