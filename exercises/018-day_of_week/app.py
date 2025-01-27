# # Complete the function to return the number of day of the week for k'th day of year
# def day_of_week(k):
#   week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#   index = (k -1 ) % len(week)
#   return week[index + 4]


# # Invoke function day_of_week with an integer between 1 and 365
# print(day_of_week(2))




# Complete the function to return the number of day of the week for k'th day of year
def day_of_week(k):
  return (k + 3) % 7


# Invoke function day_of_week with an integer between 1 and 365
print(day_of_week(2))
