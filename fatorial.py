import  math
import time

val = input('\n\ndigite um numero inteiro não negativo: ')

while type(val) != int:

    try:

        val = int(val)
        if val > 0:
            break
        else:
           val= input('\n\ndigite um valor válido\n\n') 

    except ValueError:

        val= input('\n\ndigite um valor válido\n\n')

try:

    print(f'\n\n {val}! é {math.factorial(val)} ')

    time.sleep(10)

except:
    print('erro inesperado, feche o programa e tente de novo')
    input('digite qualquer tecla + enter ou apenas enter pra encerrar: ')