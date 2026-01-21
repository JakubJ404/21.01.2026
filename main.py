print ("Aby korzystać z kalkulatora, wprowadź dwie liczby a następnie podaj operację, jaką chcesz wykonać")








a = float(input('podaj A: '))
b = float(input('podaj B: '))
operacja = input('podaj operacje: ')

if operacja == '+':
    print(f'{a} + {b} = {a+b}')
elif operacja == '-':
    print(f'{a} - {b} = {a - b}' )
elif operacja == '*':
    print(f'{a} * {b} = {a*b}')
elif operacja == '/':
    if b == 0:
        print('Nie mozna dzielic przez 0')
    else:
        print(f'{a} / {b} = {a/b}')
        
    
    
