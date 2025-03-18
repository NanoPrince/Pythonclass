#Guessing the correct random number correctly
#Generate a random number
#Prompt the user to enter a number
    #if the number is < the random number
        #print "Too low"
    #elif the number  is > the random number
        #print "Too high"
    #else
        #print congratulations you gueessed the right random number this time!
import random

rand_num_to_guess = random.randint(1,100)

while True:
    try:
        user_guess_num = int(input('Please enter a number between 1 and 100: '))

        if user_guess_num < rand_num_to_guess:
            print('Too low!')
        elif user_guess_num > rand_num_to_guess:
            print('Too high!')
        else:
            print(f'Congratulations, you guessed the {rand_num_to_guess} right this time!')
            break
    except ValueError:
        print('please enter a valid number')
        
################################ My code ########################################################3
import random
rand_num_to_guess = random.randint(1,100)
user_guess_num = 0
while user_guess_num != rand_num_to_guess:
  try:
      user_guess_num = int(input('Please enter a number between 1 and 100: '))
      
      
      if user_guess_num < rand_num_to_guess:
                  print('Number is too low!')
      elif user_guess_num > rand_num_to_guess:
                  print('Number is too high!')
      else:
            print(f'Congratulations!, you guessed the {rand_num_to_guess} right this time!')
            break
  except ValueError:
     print('Please enter a valid number')

































