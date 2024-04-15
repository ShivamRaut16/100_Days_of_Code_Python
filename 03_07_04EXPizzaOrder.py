#Don't Change --- Start ----
print("Welcome to Python Pizza Deliveries !")

size = input("What size do you what? S, M, or L ") 

add_pepperoni = input("Do you what pepperoni ? Y or N ")

extra_cheese = input("Do you what cheese ? Y or N ")

#Don't Change --- End ----

######################################

# Write your code Here 
if size == "S" :
    bill = 15
    if add_pepperoni == "Y" :
        bill += 2
elif size == "M" :
    bill = 20
    if add_pepperoni == "Y" :
        bill += 3
elif size == "L" :
    bill = 25
    if add_pepperoni == "Y" :
        bill += 3

if extra_cheese == "Y" :
        bill += 1

print(f"Your final bill : ${bill}")     

