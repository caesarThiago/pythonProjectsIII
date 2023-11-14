from time import sleep

def forcaMagnetica (q, v, B, sen0):
    forca_magnetica = q * v * B * sen0 
    return forca_magnetica

def forca_Magnetica():
    while True:
        var_choice = str(input('Deseja descobrir a força magnética de um objeto? (Sim/Não): ')).strip().lower()

        if var_choice == 'sim':
            var_q = float(input('Digite o valor do módulo da carga elétrica: '))
            var_v = float(input('Digite o valor da velocidade da carga elétrica: '))
            var_B = float(input('Digite o valor do campo magnético: '))
            var_sen = float(input('Digite o valor de sen 0 (tetha): '))

            var_forca_magnetica = forcaMagnetica(var_q, var_v, var_B, var_sen)

            print(f'O resultado da força magnética foi de {var_forca_magnetica} N.')

        elif var_choice == 'não':
            print('Ok, saindo...')
            sleep(5)
            print('Programa encerrado!')
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':
    forca_Magnetica()