# Complete the function to return the first digit to the right of the decimal point
def first_digit(num):
  aux = str(num)
  aux1 = aux.split(".")
  aux2 = (aux1)[-1]
  aux3 = str(aux2)
  aux4 = (aux3)[0]

  return aux4
    


# Invoke the function with a positive real number. ex. 34.33
print(first_digit(193.58))
