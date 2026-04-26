from game1 import stone_paper_scissor
from game2 import dice_roll
while True:
    choice=int(input("\n\nEnter(1/2/3)\n1.Play Stone Paper Scissor\n2.Play Dice Roll\n3.Exit the game\n"))
    if choice==1:
        stone_paper_scissor()
    elif choice==2:
        dice_roll()
    elif choice==3:
        break
    else:
        print("invalid input!")