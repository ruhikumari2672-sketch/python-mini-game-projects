import random
def stone_paper_scissor():
    print("\n----Stone✊Paper✋scissor✌️----")
    user=input("enter stone,paper or scissor: ").lower()
    list=["stone","paper","scissor"]
    comp=random.choice(list)
    print("User:",user,",","Computer:",comp)
    if user==comp:
        print("Its a draw🤝")
    elif (user=="stone" and comp=="paper") or (user=="paper" and comp=="scissor") or (user=="scissor" and comp=="stone"):
        print("You Lose!Better Luck Next Time👍")
    elif (user=="stone" and comp=="scissor") or (user=="paper" and comp=="stone") or (user=="scissor" and comp=="paper"):
        print("You won🏆")
    else:
        print("Invalid input!,please enter Rock,Paper or Scissor")