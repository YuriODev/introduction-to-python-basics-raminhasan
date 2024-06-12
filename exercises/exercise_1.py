# Exercise 1

user_input = input('enter a fice digit number: ')

three_digit_sum = int(user_input[0]) + int(user_input[2]) + int(user_input[4])
two_digit_sum = int(user_input[1]) + int(user_input[3])

sums = str(three_digit_sum) + str(two_digit_sum)

print(sums)
