# Exercise 6

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

divisibility = 'YES' * (a % b == 0) + 'NO' * (a % b > 0)
print(divisibility)
