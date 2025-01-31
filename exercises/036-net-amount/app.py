# Your code here
def net_amount(string):
    aux = string.split(' ')
    net = 0
    for x in range(1, len(aux)):
        if (aux[x].isdigit() and aux[int(x)-1] == 'D'): 
            net += int(aux[x])
        elif (aux[x].isdigit() and aux[int(x)-1] == 'W'): 
            net -= int(aux[x])
    return net


print(net_amount("D 300 D 300 W 200 D 100"))
