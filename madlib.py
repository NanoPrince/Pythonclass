#Lets create string that say: subscribe to python engineers bootcamp
#my_answer = 'python engineers bootcamp' 
# lets few way we concatenate the string with the vairable
#input() # it means this function CALLABLE

#print("subscribe to " + my_answer) #concatenation
#print("subscribe to "+  str.format( my_answer)) #string format method
#print(f"subscribe to {my_answer}") #F-string usage

dash1 = input("first word: ") # exclusive club
dash2 = input("second word: ")# life time
dash3 = input("third word: ")# interactive
dash4 = input("last word: ")# your friends

madlib = f"Being part of python engineers {dash1}  is such an opportunity of a {dash2}.\nOur class session is very {dash3}, and engaging with practical examples. Tell {dash4} about the good news!"

#print the madlib statement
print(madlib)