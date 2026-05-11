import random 
n = random.randint(1, 100)

print('I have selected a number between 1 and 100. Can you guess?')


attempts = 0

# To ensure that the loop starts, set the done flag to False

done = False

while not done:
  guess = int(input('Guess the number\n'))
    
  attempts = attempts + 1
  
  if guess > n:
    print('My number is smaller than that.\n')
      
  if guess < n:
    print('My number is larger than that.\n')
    
  if guess == n:
    print('Bingo, that is correct.')
    print('You took ', attempts, 'attempts to guess it.')
    done = True

print()
print()
done = False

print('Now your chance. You select a number between 1 and 100')
print('Click enter when ready')

input()

# Simple but correct algorithm

guess = 0
attempts = 0
guess_step = 10; 
prev_answer = 'l'

while not done:
    # guess = round((low + high)/2)
    answer = input('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
    attempts = attempts + 1 

    if attempts > 1: 
      if answer != prev_answer:
        # guess_step = round(guess_step/2)
        guess_step = guess_step - 1
      
    prev_answer = answer
  
    if answer.lower() == 's':
        guess = guess - guess_step
    
    if answer.lower() == 'l':
        guess = guess + guess_step
    
    if answer.lower() == 'y':
      print('Bingo, I got it.')
      print('I took ', attempts, 'attempts to guess it.')
      done = True
    
print()
print()

print('I think I can do it smarter ... ')
print('Let me try binary search ... ')

# binary search

done = False
low = 0
high = 100
guess_step = 0
attempts = 0

while not done:
    guess = round((low + high)/2)
    answer = input('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
    attempts = attempts + 1 

    if answer.lower() == 's':
        high = guess
    
    if answer.lower() == 'l':
        low = guess
    
    if answer.lower() == 'y':
      print('Bingo, I got it.')
      print('I took ', attempts, 'attempts to guess it.')
      done = True
    
print()
print()


