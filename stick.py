print("Welcome to th game of sticks :)")
player_1=input("Enter the name of the player:")
player_2=input("Enter the name of the player:")
stick=16
while stick!=0:
 if stick!=0:
     print(stick)
     choice=int(input(f"{player_1} Please choose a number from(1,2,3) "))
     stick=stick-choice
     player=player_1
 if stick!=0 :
       print(stick)
       choice = int(input(f"{player_2} please choose  a number from(1,2,3) "))
       stick = stick-choice
       player= player_2
 if stick==0:
       print(f"{player} has lost the game")
