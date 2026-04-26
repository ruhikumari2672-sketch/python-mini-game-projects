import random
def dice_roll():
    print("\n------Dice Roll Game🎲------")
    user=random.randint(1,6)
    comp=random.randint(1,6)
    if user in [1,2,3,4,5,6]:
        print("You:",user,"Computer:",comp)
        if user==comp:
            print("Yeee🥳🥳YOU GUESSED IT RIGHT.🎲")
        else:
            print("OOPS! The dice rolled",comp,"Try Again!")
    else:
        print("Invalid Input! please enter(1/2/3/4/5/6)")