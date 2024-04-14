#Don't Change --- Start ----
age = input("What is your current age ?")
#Don't Change --- End ----

######################################

# Write your code Here 
Lifeline = 40
age_int = int(age)
rem_Years = Lifeline - age_int 
rem_Months = rem_Years * 12 
rem_Weeks = rem_Years * 52
rem_Days = rem_Years * 365
print(f"You have {rem_Days} days,{rem_Weeks} weeks,{rem_Months} months left")