#Don't Change --- Start ----
print("Welcome to Love Calculator!")

name1 =input("What is your name ? ") 
name2= input("What is their name ? ")


#Don't Change --- End ----

######################################

# Write your code Here 
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

# print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score {love_score} ,You go together coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score{love_score},You are alright together ")
else :
    print(love_score)

