def total_set_bits(n):
    count = 0
    while(n):
        if (n&1 == 1):
            count += 1
        n >>= 1
    
    return count

num = int(input("Enter the number: "))
print("Total set bits = ", total_set_bits(num))