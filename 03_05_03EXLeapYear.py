#Don't Change --- Start ----
year = int(input("Which year do you want to check ? "))
#Don't Change --- End ----

######################################

# Write your code Here 
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year.")
        else:
            print("leap year.")    
    else:
        print("leap year.")
else :
    print("Not leap year.")