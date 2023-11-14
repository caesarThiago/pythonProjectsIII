import math
from time import sleep

def Hipotenusa(cateto_oposto, cateto_adjacente):
    hipotenusa = math.sqrt(math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2))
    return hipotenusa 

def hipotenusaSimulator():
    while True:
        var_choice = str(input('Deseja descobrir a hipotenusa de um triângulo retângulo? (Sim/Não): ')).strip().lower()

        if var_choice == 'sim':
            var_cat_opt = float(input('Digite o cateto oposto (em centímetros): '))
            var_cat_adj = float(input('Digite o cateto adjacente (em centímetros): '))

            var_hipotenusa = Hipotenusa(var_cat_opt, var_cat_adj)

            print(f'A hipotenusa resultante é {var_hipotenusa:.2f} cm.')
        elif var_choice == 'não':
            print('Ok, saindo...')
            sleep(5)
            print('Programa encerrado!')
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':    
    hipotenusaSimulator()