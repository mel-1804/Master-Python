# # Complete the function to return the tens digit of a given integer
# def tens_digit(num):
#   aux = str(num)[-2]
#   return int(aux)


# # Invoke the function with any integer
# print(tens_digit(1323))



# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  aux = str(num//10)[-1]
  return int(aux)


# Invoke the function with any integer
print(tens_digit(1323))
