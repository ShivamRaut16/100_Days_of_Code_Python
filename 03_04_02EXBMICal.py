#Don't Change --- Start ----
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
#Don't Change --- End ----

######################################

# Write your code Here 
BMI = round(int(weight) / float(height) ** 2)
# print(BMI)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
     print(f"Your BMI is {BMI}, you have normal weight.")
elif BMI < 30:
     print(f"Your BMI is {BMI}, you are overweight.")
elif BMI < 35:
     print(f"Your BMI is {BMI}, you are obese.")
else:
     print(f"Your BMI is {BMI}, you are clinically obese.")
