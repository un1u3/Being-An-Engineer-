import random



actualNumber = random.randint(1,10)

userStatus = True
while userStatus:
    
    try:
        user = int(input("Enter a number (1-100)"))

        if user == actualNumber:
            print(f"You won {actualNumber}=={user},")
            break
        else:
            print(f"Guessed Number {user}, Actual Number {actualNumber}")
    except ValueError:
        print("Value Error")
        