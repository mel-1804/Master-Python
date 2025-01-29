# Your code here
def all_digits_even():
    selected_number = []

    numbers = [x for x in range(1000, 3001)]
    for num in numbers:
        s = str(num)
        if(int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
            selected_number.append(s)


    return ','.join(selected_number)

print(all_digits_even())


#no pude sola
