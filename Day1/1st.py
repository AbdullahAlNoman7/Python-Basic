# 1:Write a program to accept two numbers from the user and calculate multiplication
"""
def userInput():
    user1 = int(input("Enter Number1: "))
    user2 = int(input("Enter Number2: "))

    return user1 * user2


obj_userInput = userInput()
print(f"The output is {obj_userInput}")
"""
"""
# 2 Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for i in range(1,11):
    x_sum = previous_num + i
    print("Current number", i , "previous number", previous_num," Sum of", x_sum)
    previous_num = i

"""
"""
# Print First 10 natural numbers using while loop
n = 1
while n <= 10:
    print(n)
    n = n + 1

# Write a program to print multiplication table of a given number

num = 2
for i in range(1, 10):
    result = i * num
    print(result)
"""
# Write a program to display only those numbers from a list that satisfy the following conditions
#
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item > 500:
        break
    elif item >150:
        continue
    elif item % 5 == 0:
        print(item)