import random

def country_guessing_game():
    countries = ["Canada", "Brazil", "Germany", "Australia", "Japan", "India"]
    selected_country = random.choice(countries)
    print("Welcome to the Country Guessing Game!")
    print("Try to guess the country. You will receive clues one letter at a time.")
    
    for i in range(len(selected_country)):
        clue = selected_country[:i+1]
        guess = input(f"Clue: {clue}. Your guess: ")
        
        if guess.lower() == selected_country.lower():
            print("Congratulations! You guessed the country correctly.")
            return
        else:
            print("Incorrect guess. Here's another clue.")
    
    print(f"Sorry, you've used all your clues. The country was: {selected_country}")

def main():
    while True:
        print("\nMenu:")
        print("1. Play Country Guessing Game")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            country_guessing_game()
        elif choice == "2":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

country_guessing_game()
main()
