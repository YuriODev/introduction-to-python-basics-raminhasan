# Exercise 4

user_input = input("Enter a four digit number: ")

if len(user_input) < 4:
  N = 4 - len(user_input)
  
  user_input = user_input.zfill(N + len(user_input))

reversed = user_input[::-1]

if reversed == user_input:
  print(1)

else:
  print(0)
