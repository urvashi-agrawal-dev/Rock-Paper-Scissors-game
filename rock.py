import random
while True:
    user_player=input("enter a choice(rock,paper,scissors):")
    possible_steps=["rock","paper","scissors"]
    computer_action=random.choice(possible_steps)
    print(f"\nYou choose{user_player},computer chose{computer_action}.\n")
    if user_player==computer_action:
        print(f"Both players selected{user_player}.It's a tie!")
    elif user_player=="rock":
        if computer_action=="scissors":
           print("Rock smashes scissors!You win!")
        else:
           print("Paper covers rock!You lose.")
    elif user_player=="paper":
        if computer_action=="rock":
           print("Paper covers rock!You win!")
        else:
           print("Scissors cuts paper!You lose")
    elif user_player=="scissors":
        if computer_action=="paper":
           print("Scisssors cuts paper!You win!")
        else:
           print("Rock smashesss scissors!You lose.")
    play_again=input("Play again?(Y/N):")
    if play_again.upper()!="Y":
       break


