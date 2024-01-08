print("***** Welcome to Rock Paper Scissor Game *****")

print("Introduction to the game: p/P indicates paper, s/S indicates scissor and r/R indicates rock")
Player1 = input("Enter p/P or s/S or r/R: ").lower()
Player2 = input("Enter p/P or s/S or r/R: ").lower()

if len(Player1) == 1 and len(Player2) == 1:
    if Player1 == "r" and Player2 == "s":
        print("Player1 won!")
    elif Player1 == "p" and Player2 == "r":
        print("Player1 won!")
    elif Player1 == "s" and Player2 == "p":
        print("Player1 won!")
    elif Player1 == Player2:
        print("Oops it's a tie!")
    elif Player1 == "s" and Player2 == "r": 
        print("Player2 won!")
    elif Player1 == "r" and Player2 == "p": 
        print("Player2 won!")
    elif Player1 == "p" and Player2 == "s": 
        print("Player2 won!")    
    else:
        print("Invalid Input")      
else:
    print("Invalid Input")       
    
print("***** Thanks for playing *****")  
print("***** By : V Sahanashre *****")
        