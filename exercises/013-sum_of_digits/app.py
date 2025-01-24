# # Complete the function "digits_sum" so that it prints the sum of a three-digit number
# def digits_sum(num):
#   aux = int(str(num)[0])
#   aux1 = int(str(num)[1])
#   aux2 = int(str(num)[2])
#   return (aux + aux1 + aux2)


# # Invoke the function with any three-digit number
# print(digits_sum(123))



# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  aux = 0
  for n in str(num):
    aux = aux + int(n)
  return aux


# Invoke the function with any three-digit number
print(digits_sum(123))