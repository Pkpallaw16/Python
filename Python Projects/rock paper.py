
import random
def game(user_select):
    option=["Rock","Paper","Scissor"]
    pc_selection=random.choice(option)
    print(pc_selection,user_select)
    if user_select=="Paper" and pc_selection=="Scissor":
        print("You Lost!")
    elif user_select=="Scissor" and pc_selection=="Paper":
        print("You Win!")
    elif user_select=="Rock" and pc_selection=="Scissor":
        print("You Win!")
    elif user_select=="Scissor" and pc_selection=="Rock":
        print("You Lost!")
    elif user_select=="Paper" and pc_selection=="Rock":
        print("You Win!")
    elif user_select=="Rock" and pc_selection=="Paper":
        print("You Lost!")
    else:
        print("Tie!")

user_option={1:"Rock",2:"Paper",3:"Scissor",4:"quit"}
quit=True
while quit:
    game(user_option[option])
    option = int(input("select your option 1:Rock,2:Paper,3:Scissor,4:quit"))
    if option == 4:
        quit = False
