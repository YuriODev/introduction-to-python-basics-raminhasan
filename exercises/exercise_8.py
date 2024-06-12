# Exercise 8

a = int(input())
b = int(input())
c = int(input())

min = a * (a <= b and a <= c) + b * (b < a or b < c) + c * (c < a and c < b)
max = a * (a >= b and a >= c) + b * (b > a or b > c) + c * (c > a and c > b)
mid = a + b + c - min - max

print(f'{min}\n{mid}\n{max}')
