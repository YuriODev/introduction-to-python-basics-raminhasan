# Exercise 8

item_one = input("Enter a number: ")
item_two = input("Enter a number: ")
item_three = input("Enter a number: ")

min = item_one * (item_one <= item_two and item_one <= item_three) + item_two * (item_two <= item_one and item_two <= item_three) + item_three * (item_three <= item_one and item_three <= item_two)
mid = item_one * ((item_one >= item_two and item_one <= item_three) + (item_one >= item_three and item_one <= item_two)) + item_two * ((item_two >= item_one and item_two <= item_three) + (item_two >= item_three and item_two <= item_three)) + item_three * ((item_three >= item_two and item_three <= item_one) + (item_three >= item_one and item_three <= item_two))
max = item_one * (item_one >= item_two and item_one >= item_three) + item_two * (item_two >= item_one and item_two >= item_three) + item_three * (item_three >= item_one and item_three >= item_two)

print(f'{min}\n{mid}\n{max}')
