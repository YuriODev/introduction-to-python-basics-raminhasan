# Exercise 11
# Your solution comes here

s = int(input())

denom500 = s // 500
denom100 = (s % 500) // 100
denom10 = ((s % 500) % 100) // 10
denom5 = (((s % 500) % 100) % 10 ) // 5
denom2 = ((((s % 500) % 100) % 10 ) % 5) // 2
denom1 = ((((s % 500) % 100) % 10 ) % 5) % 2

print(f'{denom500} (500), {denom100} (100), {denom10} (10), {denom2} (5), {denom2} (2), {denom1} (1)')
