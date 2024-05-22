# Exercise 6

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

divisibility = 'yes' * (a % b == 0) or 'no' * (a % b != 0)
