# Exercise 2

n = int(input('enter a number: '))

if n % 2 == 1:
  next_even = n + 1
  print(f'the next even number after {n} is {next_even}')

else:
  next_even = n + 2
  print(f'the next even number after {n} is {next_even}')
