from time import sleep

def numImpares(numero_inicial, numero_final):
    numeros_impares = []
    for x in range(numero_inicial, numero_final + 1):
        if x % 2 == 1:
            numeros_impares.append(x)
    return numeros_impares

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def impares():
    while True: 
        var_choice = str(input('Deseja descobrir todos os números impares determinados por um início e fim? (Sim/Não): ')).strip().lower()

        if var_choice == 'sim':
            var_num_init = int(input('Digite um número inicial inteiro (impar): '))
            var_num_end = int(input('Digite um número final inteiro (impar): '))

            if var_num_end % 2 == 1 and var_num_init % 2 == 1 and var_num_init != 0 and var_num_end != 0:
                numeros_impares = numImpares(var_num_init, var_num_end)
                print(numeros_impares)
            else:
                print('\33[1;33m Error002: invalid_number! \33[m')
        elif var_choice == 'não': 
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice! \33[m')

if __name__ == '__main__':
    impares()
