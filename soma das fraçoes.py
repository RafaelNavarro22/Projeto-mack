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
# encerra a validação do valor

s = 0
for val in range(1,val+1):
     s += (2*val-1) / val
print(s)
time.sleep(10)
    
