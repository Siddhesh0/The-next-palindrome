             # The NEXT PALINDROME
"""
The palindrome is a string when reversed is equal to unreversed
eg. 616, 2112, mom, dad, kanak
You have to take the input from the user. You have to find the next palindrome corresponding to that number.
your first input should be "number of test cases" and then take all cases as an input from the user.
INPUT:
3
451
2133

OUTPUT:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2133 is 2222

taking input from the user

Author: Siddhesh
Date: 21 Nov 2021
Purpose: Practice problem
"""

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n +=1
    return

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    n = int(input("Enter the number of test cases"))
    numbers = []

    for i in range(n):
        number = int(input("Enter the number\n"))
        numbers.append(number)

    for i in range(n):
        print(f'The next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}')
