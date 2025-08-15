

""""
Create a simple Python console program called number_game.py that:
1. Asks the user to enter their name.
2. Greets them with "Hello, <name>! Let's play a guessing game.
3. Picks a secret number between 1 and 10 (store it in a variable)
4. Lets the user guess up to 3 times
5. Uses loops and conditionals to:
    Check if the guess is correct (print " You guessed it!" and stop the loop)
    if wrong, give hints "Too high! or Too low!
6. If they fail after 3 times, reveal the secret number 
"""
import random

def collect_username():
    print("Enter your name")
    name = input()
    print(f"Hello , welcome to the hub {name}")
    


def number_game():
	print("Welcome, Kindly Enter your name")
	name = input()
	print(f"Hello {name}! Let's play a guessing game.")
	secret_num = random.randint(1,10)
	attempts = 3
	
	for attempt in range(attempts):
		guess = int(input(f"Make your guess number {attempt + 1} \n"))
		
		if guess > secret_num:
			print("Too high!")
		elif guess < secret_num:
			print("Too low!")
		else:
			print(f"You guessed it! the number is {secret_num}")
			return
	print(f"You failed at 3 attempts. The secret number is {secret_num}")

number_game()
    	
   
