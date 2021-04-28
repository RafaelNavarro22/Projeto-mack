import time
contador = 1
while contador == 1 :
   
    n1= int(input('digite seu primeiro número: '))
    n2= int(input('digite seu segundo número: '))
    sin=2
    while sin == 2 :
        op= str(input('escolha sua operaçao\nDigite + para soma\nDigite - para subtração\nDigite * Para multiplicação\nDigite / para divisão\nDigite 0 para fechar a calculadora\n\n\n'))
        if op == '+':
            print(f'a soma dos dois números é {n1 + n2} ')
            sin=0
        if op == '-':
            print(f'a subtraçao dos dois números é {n1-n2}')
            sin = 0
        if op == '*':
            print(f'a multiplicação dos dois números é {n1*n2}')
            sin = 0
        if op == '/':
            print(f'a divisão dos dois números é {n1/n2}')
            sin=0
        if op == '0':
            contador = 0
            sin=0
        if op != '+' and op != '-' and op != '*' and op != '/' and op != '0'  :
            print('operaçao invalida, digite seus números novamente e tente de novo\n\n\n')
            sin=2
else :
    print('obrigado por usar a calculadora do rafael, meu tia é 32150032, espero ter uma boa nota! ')
    time.sleep(10)