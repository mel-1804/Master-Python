# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):
    aux = d*1000*n
    aux1 = c*n
    aux2 = (aux + aux1)
    aux3 = aux2 //1000
    aux4 = aux2 % 1000
    return (aux3, aux4)


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(10,15,2))
