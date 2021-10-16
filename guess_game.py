print("""
Guess the Number,
You need to guess one number between 0 to 20,
You only have five chances to find right number, Good Luck!
""")
guessed_number = 14
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count = guess_count + 1
    # if you find the correct number stop the while loop then print the message
    if guess == guessed_number:
        print("\tCongratulations, You won!")
        break
    # if you're struggling to find the number. Print the hint after making 3 guesses
    if guess_count == 3:
        print("\tHint: The the number is even number and 60% of probability of more than ten")
    # if you guess number that is more than 20. Print the message
    if guess > 20:
        print("\tNumber must be less than 20")
    # if you didn't guess the number and lost all chances. Print the message
else:
    print("\tYou failed!, Try Again")
