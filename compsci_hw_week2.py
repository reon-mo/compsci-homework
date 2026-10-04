print("Welcome to the game of 21")

import random

def play_game():
    user_total = random.randint(1, 10)
    system_total = random.randint(1, 21)

    print(f"Your initial number is: {user_total}")
    print(f"The system's initial number is: {system_total}")

    while True:
        choice = input("Do you want to (A)dd a random value from 1 to 10 or (S)tay? ").strip().upper()
        
        if choice == "A":
            add_value = random.randint(1, 10)
            user_total += add_value
            print(f"You added {add_value}. Your new total is: {user_total}")
            
            if user_total > 21:
                print("You exceeded 21! You lose.")
                break
        elif choice == "S":
            print(f"You chose to stay with a total of: {user_total}")
            break
        else:
            print("Invalid choice. Please select A or S.")

    if user_total <= 21:
        print(f"The system's total is: {system_total}")
        if system_total > 21 or user_total > system_total:
            print("You win!")
        elif user_total < system_total:
            print("The system wins!")
        else:
            print("It's a tie!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

play_game()
