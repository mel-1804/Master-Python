# # Your code here
# def divisible_binary(nums):
#     aux = nums.split(',')
#     aux1 = map(lambda x: int(x, 2), aux)
#     aux2 = list(aux1)
#     aux3 = list(filter(lambda x: x % 5 == 0, aux2))
#     aux4 = map(lambda x: bin(x)[2:], aux3)
   
#     return list(aux4)

# print(divisible_binary("0100,0011,1010,1001,1111"))


# Your code here
def divisible_binary(nums):
    result = []
    list_bins = [x for x in nums.split(',')]
    for list_bin in list_bins:
        if (int(list_bin, 2)) % 5 == 0:
            result.append(list_bin)

    return ','.join(result)

print(divisible_binary("0100,0011,1010,1001,1111"))

