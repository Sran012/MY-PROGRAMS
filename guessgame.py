print("Welcome to number guessing game")
name = input("Enter your name : ")
print ("Hii " + name + " guess a secret number to win ♡")
import random
secret_number = random.randint(0,10)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
	guess = int(input("Guess : "))
	guess_count +=1
	if guess == secret_number:
		print("hey " +name+ " you won!")
		break
	if guess < secret_number:
		print("try a large number")
	if guess > secret_number:
		print("try a small number")		
else:
	print("you failed")
	print
				
