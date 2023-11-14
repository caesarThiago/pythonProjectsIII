
from time import sleep

def contagemRegressiva(num):
    for i in range(num, 0, -1):
        print(i)
        sleep(1)
    print('Fim!')

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def simulator():
    while True:
        var_choice = str(input('Deseja fazer uma contagem regressiva? (Sim/Não): '))

        if var_choice == 'sim':
            var_num = int(input('Digite o número da contagem: '))

            contagemRegressiva(var_num)
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':
    simulator()