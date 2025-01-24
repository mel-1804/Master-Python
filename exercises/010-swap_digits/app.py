# # Complete the function to return the swapped digits of a given two-digit integer
# def swap_digits(num):
#   # Your code here
#   aux = str(num)
#   aux1 = list(aux)
#   aux2 = [aux1[1], aux1[0]]
#   aux3 = "".join(aux2)
#   aux4 = int(aux3)
#   return aux4
   
# # Invoke the function with any two-digit integer as its argument
# print(swap_digits(30))




# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  aux = str(num)[1] + str(num)[0]
  
  return int(aux)
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))