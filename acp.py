def rightmost_set_bit(n):
    c = 1
    while(n):
        if n&1 == 1:
            return c
        else:
            c+=1
            n>>=1
    return c

num = int(input("Enter a number : "))
print("Position of the first set bit: ", rightmost_set_bit(num))