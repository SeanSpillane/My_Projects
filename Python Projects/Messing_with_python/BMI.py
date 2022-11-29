input_weight = float(input("Enter your weight (kg) : "))

input_height = float(input("Enter your height (cm) : "))

divided_height = input_height / 100

bmi_height = divided_height * divided_height

bmi = input_weight / bmi_height

print(bmi)

if (bmi < 18.5):
    print("You Are underweight")

elif (bmi <= 24.9 and bmi >= 18.5):
    print ("You are a healthy weight :)")

elif (bmi >= 25 and bmi <= 29.9):
    print ("You are overweight")

else:
    print ("You are obese")