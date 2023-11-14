from time import sleep
import functions

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def pgCalculator():
    while True:
        var_choice = str(input('Deseja calcular uma P.G (Progressão Geométrica) (Sim/Não): ')).strip().lower()

        if var_choice == 'sim':
            var_choice = str(input('Você deseja calcular a Razão, Soma dos Termos e Termo Médio: ')).strip().lower()

            if var_choice == 'razão':
                var_a1 = int(input('Digite o primeiro termo: '))
                var_a2 = int(input('Digite o segundo termo: '))

                var_razao = functions.razaoPg(var_a1, var_a2)

                print(f'A razão da P.G é {var_razao}')
            elif var_choice == 'soma dos termos':
                var_a1 = int(input('Digite o primeiro termo: '))
                var_q = int(input('Digite a razão: '))
                var_n = int(input('Digite o número de termo: '))

                var_soma_termos = functions.somaTermos(var_a1, var_q, var_n)

                print(f'A soma dos termos da P.G é {var_soma_termos}')
            elif var_choice == 'termo médio':
                var_a1 = int(input('Digite o primeiro termo: '))
                var_an = int(input('Digite o enésimo termo: '))

                var_termo_medio = functions.termoMedio(var_a1, var_an)

                print(f'O termo médio da P.G é {var_termo_medio:.2f}')
            else:
                print('\33[1;33m Error002: unexpected_choice!\33[m')
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':
    pgCalculator()