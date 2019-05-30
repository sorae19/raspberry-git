i=2
number=int(input())
while i<=number/i:
    while number%i==0:
        number=number/i
        print(i)
    i+=1
print(number)
