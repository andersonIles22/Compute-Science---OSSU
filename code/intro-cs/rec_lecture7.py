import math
####################################################################################
# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

userInput=float(input('Write a integer positive: '))
epsilon=0.01
high=userInput
low=0
guess=(high+low)/2.0
attemp=0
    
while abs(guess**4-userInput)>=epsilon:
    if guess**4>userInput:
        high=guess
    else:
        low=guess
    guess=(high+low)/2.0
    attemp+=1
print(f'The forth root of {userInput} is {guess}, in just {attemp} attempts')

####################################################################################
# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range. 

def isNumberFalls(num,maxRange,minRange):
    return num>minRange and num<maxRange
print(isNumberFalls(10,15,8))        

####################################################################################

# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

userNum=float(input('Write an integer positive to calculate the forth root: '))
userEpsilon=0.01
increment=0.00001
num_gueess=0
iterations=0

if userNum<0:
    print(f'The {userNum} is not an integer  positive')
else:
    while (userNum-num_gueess**4)>=userEpsilon and num_gueess**4<=userInput:
        num_gueess+=increment
        iterations+=1
    print(f'The forth root of {userNum} is {num_gueess}, in just {iterations} iterations')