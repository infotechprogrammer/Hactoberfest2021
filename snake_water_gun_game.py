import random
print("This is a **snake water gun** GAME")
print("Choose your option snake, water or gun (lowercase only)")
print("10 chances will be given ")
print("Lets see how much points you get out of 10")
print("Game Starts Now :")
i = 1
score = 0
while(i<11):
    list = ["snake","water","gun"]
    choice = random.choice(list)
    print("Chance ",i, " :")
    inp = input("Enter your input :")
    if(inp == choice):
        print("Tie")
        score = score + 1
    elif(inp == "snake" and choice == "water"):
        print("Yeah! you are Winner :)")
        score = score + 1
    elif(inp == "water" and choice == "gun"):
        print("Yeah! you are Winner :)")
        score = score + 1
    elif(inp == "gun" and choice == "snake"):
        print("Yeah! you are Winner :)")
        score = score + 1
    elif(choice == "gun" and inp == "snake"):
        print("Opps! you Loose :(")
    elif(choice == "water" and  inp == "gun"):
        print("Opps! you Loose :(")
    elif(choice == "snake" and inp == "water"):
        print("Yeah! you are Winner :)")
    else:
        print("Sorry its wrong input")    
    i = i + 1
print("Your Total Score is : ",score)
