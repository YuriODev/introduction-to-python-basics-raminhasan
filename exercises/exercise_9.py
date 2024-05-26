# Exercise 9

running = True

while running:
  h = int(input('enter a value for hours between 0 and 12: '))
  m = int(input('enter a value for minutes between 0 and 60: '))
  s = int(input('enter a value for seconds between 0 and 60: '))

  if 0 <= h <= 12 and 0 <= m <= 60 and 0 <= s <= 60:
    running = False
    break

  else:
    pass

minute_fraction_hour = m / 6
second_fraction_hour = s / 3600

rotations_hours = h * 30
rotations_minutes = minute_fraction_hour * 6
rotations_seconds = second_fraction_hour *  (1/120)

print(rotations_hours)
print(rotations_minutes)
print(rotations_seconds)

total_rots = rotations_hours + rotations_minutes + rotations_seconds

print(total_rots)
