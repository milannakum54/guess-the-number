secret_number = 7
i=0
while i<3:
     guess = int(input("Guess the secret number (between 1 and 10): "))
     if guess == secret_number:
          print("Congratulations! You guessed the secret number.")
          break
     else:
          print("Wrong guess. Try again.")
     i += 1
print("Loop finished.")