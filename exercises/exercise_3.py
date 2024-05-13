# Exercise 3

n = int(input('enter a number of seconds: '))
m = True

hours = n // 3600
minutes = (n % 3600) // 60
seconds = (n % 3600) % 60

if seconds < 10:
  seconds = f"0{seconds}"
  
if minutes < 10:
  minutes = f"0{minutes}"

print(f"{n} equates to {hours}:{minutes}:{seconds}")
