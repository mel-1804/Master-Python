# Complete the function to return how many hours and minutes are displayed on the 24h digital clock
def digital_clock(n):
  hours = n//60
  if hours > 23:
    hours = hours - 24*(hours//24)
    
  minutes = n % 60
  
  return (hours, minutes)

# Invoke the function with any integer (minutes after midnight)
print(digital_clock(183))
