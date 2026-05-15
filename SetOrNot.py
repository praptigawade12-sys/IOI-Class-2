def set_or_not(number,n):
    if number & (n << (n-1)):
        print("\nSET")
    else:
        print("\nNOT SET")
    
number = int(input("Enter the number: "))
n = int(input("Enter bit number: "))
set_or_not(number,n)