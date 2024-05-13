# Exercise 8

array = []

for i in range(3):
  item = int(input("Enter a number: "))
  array.append(item)

array.sort()

for x in range(3):
  print(array[x])
