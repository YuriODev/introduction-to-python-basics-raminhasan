# Exercise 9

h = int(input('enter a value for hours between 0 and 12: '))
m = int(input('enter a value for minutes between 0 and 60: '))
s = int(input('enter a value for seconds between 0 and 60: '))

rotations_hours = h * 30
rotations_minutes = m * 6
rotations_seconds = s *  (1/120)

print(rotations_hours)
print(rotations_minutes)
print(rotations_seconds)

total_rots = rotations_hours + rotations_minutes + rotations_seconds

print(total_rots)
