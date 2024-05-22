# Exercise 9

h = int(input('enter a value for hours between 0 and 12: '))
m = int(input('enter a value for minutes between 0 and 60: '))
s = int(input('enter a value for seconds between 0 and 60: '))

h %= 12
m %= 60
s %= 60

rotations_hours = h * 30
rotations_minutes = m * 0.5
rotations_seconds = s *  (1/120)

total_rots = rotations_hours + rotations_minutes + rotations_seconds

print(total_rots)
