import time
n= int(input('digite um número natural'))
i=0
while i<= n:
    j=n
    while j>=i:
        print(j,end="")
        j-=1
    i+=1
    print('')