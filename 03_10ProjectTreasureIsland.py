print("")
print(" _                                     _     _                 _ ")
print("| |                                   (_)   | |               | |")
print("| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |")
print("| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |")
print("| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |")
print("\__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|")
print("")
print("")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[      ]
*******************************************************************************
''')
print("")
print("")
print("Welcome to Treasure island")
print("Your mission is to find the treasure")
print("")
print("")
choice1 = input('You\'re at the cross road. Where you want to go Type "left" or "right"' ).lower()
if choice1 == "right":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input('You arrived at island unharmed. There is a house 3 doors . One red, one yellow and one blue, Which color do you choose ? ').lower()

        if choice3 == "red":
            print("It's room ful of fire. Game Over")
        elif choice3 == "yellow":
            print("You found a treasure! You Win! ")
        elif choice3 == "blue":
            print("You entered a room of beasts. Game Over")
    else :
        print("You attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game Over")

