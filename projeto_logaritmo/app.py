import math
from time import sleep

def logNumber (numero, base):
    var_log = math.log(numero, base)
    return var_log

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def log():
    while True: 
        var_choice = str(input('Deseja descobrir o logaritmo de um número? (Sim/Não): ')).strip().lower()

        if var_choice == 'sim': 
            var_num = int(input('Digite um número inteiro: '))
            var_base = int(input('Digite a base: '))

            var_log = logNumber(var_num, var_base)

            print(f'O logaritmo de {var_num} na base {var_base} é {var_log:.2f}')

        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':
    log()