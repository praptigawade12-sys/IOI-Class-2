def numofbits(n):
    onces = 0
    zeros = 0

    while(n):
        if (n&1==1):
            onces+=1
        else:
            zeros+=1
        
        n>>=1
    print("\n\nOnes: ",onces,"\nZeros:",zeros)

number = int(input("Enter the number: "))
numofbits(number)