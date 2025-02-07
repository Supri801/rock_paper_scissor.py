import random

def get_user_choice():
    """Get the user's choice"""
    print("Enter your choice: rock, paper, or scissors")
    user_choice = input().lower()
    
    # Validate the user's choice
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input().lower()
    
    return user_choice

def get_computer_choice():
    """Get the computer's choice"""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the rules"""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    
    return "Computer wins!"

def play_game():
    """Play one round of the game"""
    print("Welcome to Rock, Paper, Scissors!")
    
    # Get the user's and computer's choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    # Display the choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
if __name__ == "__main__":
    play_game()
