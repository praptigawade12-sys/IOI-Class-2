n = int(input("Enter a number : "))
bits = n.bit_length()
mask = (1 << bits) - 1
r = n^mask
print("Number after toggling :",r)