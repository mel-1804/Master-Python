# Complete the function to print the last two digits of an integer greater than 9
def last_two_digits(num):
    aux = str(num)[-2] + str(num)[-1]
    
    return int(aux)

# Invoke the function with any integer greater than 9
print(last_two_digits(123456))
