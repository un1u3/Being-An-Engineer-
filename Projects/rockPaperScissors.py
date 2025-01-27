import random



def game():
    i = 0
    win = 0
    looses = 0 
    draw = 0 
    while i < 5:
        

        computer = random.randint(0,2)
        user_input = input("Enter Scissior,Paper or Rock").lower()
        valid = ['rock','paper','scissor']

        computer_choice = valid[computer]

        if user_input not in valid:
            print("Invalid input! Please choose Rock, Paper, or Scissor.")
            continue


            
        print(f"Computer input {computer_choice} and your choice {user_input}")
        if user_input == computer_choice:
            draw += 1
            print("It's a draw!")
        elif (user_input == 'rock' and computer_choice == 'scissor') or \
            (user_input == 'scissor' and computer_choice == 'paper') or \
            (user_input == 'paper' and computer_choice == 'rock'):
            win = win + 1 
            print("You win!")
        else:
            print("You lose!")
            looses = looses + 1 
        i = i+ 1 
            
            
            
    print(f"draw: {draw}")
    print(f"WIN: {win}")
    print(f"Loose: {looses}")
    
            
            
        
game()