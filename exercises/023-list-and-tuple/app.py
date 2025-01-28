# Your code here
def list_and_tuple(*ns):
    new_list = [str(n) for n in ns]
    new_tuple = tuple(new_list)
   
        
    return (new_list, new_tuple)



print (list_and_tuple(34,67,55,33,12,98))