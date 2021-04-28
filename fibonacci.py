
import time

n = input('\n\ndigite um numero inteiro: ')

while type(n) != int:
    try:

        n = int(n)
        break
    except ValueError:

        n= input('\n\ndigite um valor válido\n\n')##fim da validaçao

u=1
p=1

if (n==1) or (n==2):
    print("1")
else:
    print('1\n1')
    for count in range(2,n):

        t = u + p

        p = u
        u = t

        count += 1

        print(t)
time.sleep(10)
