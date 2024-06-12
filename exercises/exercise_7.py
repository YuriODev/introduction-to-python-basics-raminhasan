# Exercise 7

user_input = input("Enter a four digit number: ")

if len(user_input) <= 4:
  N = 4 - len(user_input)
  
  user_input = user_input.zfill(N + len(user_input))

print(user_input)

total = 0

for i in range(4):
  total += int(user_input[i])

print(total)
