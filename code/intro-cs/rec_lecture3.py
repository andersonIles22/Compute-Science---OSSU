####################################################################################
# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

# Insert code below
name=input('Write your name: ')
nameLenght=len(name)
print(nameLenght-5)

####################################################################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.

test_string = "We want to remove the nth character from this string"
n = 8

# Insert code below
print(f'Old string: {test_string}')
partOneString=test_string[0:n]
partTwoString=test_string[n+1:len(test_string)]
print(f'New string: {partOneString}{partTwoString}')

####################################################################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.

my_string = "This is"  

# Insert code below
stringLength=len(my_string)
if(stringLength>10 or stringLength<5):
    print(True)
else:
    print(False)

####################################################################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string

my_string = "How many times is the letter ee in this string?"

# Insert code below
count=0
for i in my_string:
    if(i=='e'):
        count+=1
print(f'{count} times')