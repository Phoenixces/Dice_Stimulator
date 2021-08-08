import random
def stimulator():
    x=random.randint(1,6)
    
    if x==1:
        print("---------")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print("---------")
    elif (x==2):
        print("---------")
        print("|       |")
        print("| o   o |")
        print("|       |")
        print("---------")
    elif (x==3):
        print("---------")
        print("|       |")
        print("| o o o |")
        print("|       |")
        print("---------")
    elif (x==4):
        print("---------")
        print("|  o o  |")
        print("|       |")
        print("|  o o  |")
        print("---------")
    elif (x==5):
        print("---------")
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
        print("---------")
    else:
        print("---------")
        print("|  o  o |")
        print("|  o  o |")
        print("|  o  o |")
        print("---------")

print("Lets stimulate the Dice...Happy game...:)")    
while True:

    choice=input("If you wish to stimulate the Dice : \nPress 'Y'/'y' and if not Press 'N'/'n' ..: ")
    if choice =='y' or choice=='Y':
        stimulator()
    
    elif choice=='n' or choice=='N': 
        break
    else:
        print("ENTER VALID INPUT.....:((")

    