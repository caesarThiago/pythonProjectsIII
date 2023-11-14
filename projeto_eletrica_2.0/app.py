import functions
from time import sleep

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def calculadoraEletrica():
    while True:
        var_choice = input('Deseja utilizar a calculadora elétrica? (Sim/Não): ').strip().lower()

        if var_choice == 'sim':
            var_option = input('Escolha uma das opções: \n 1 - Corrente Elétrica \n 2 - Potencial elétrico \n 3 - Campo elétrico \n 4 - Energia elétrica consumida \n Escolha: ').lower().strip()

            if var_option == '1':
                var_carga_eletrica = float(input('Digite o valor da carga elétrica (em coloumbs): '))
                var_intervalo_tempo = float(input('Digite o intervalo de tempo (em segundos): '))

                var_corrente_eletrica = functions.correnteElétrica(var_carga_eletrica, var_intervalo_tempo)

                print(f'O valor da corrente elétrica é de {var_corrente_eletrica:.2f} ampere(s)')
            elif var_option == '2':
                var_carga_eletrica = float(input('Digite o valor da carga elétrica (em coloumbs): '))
                var_distancia = float(input('Digite a distância (em metros): '))

                var_potencial_eletrico = functions.potencialEletrico(var_carga_eletrica, var_distancia)

                print(f'O valor do potencial elétrico é de {var_potencial_eletrico:.2f} volt(s)')
            elif var_option == '3':
                var_carga_eletrica = float(input('Digite o valor da carga elétrica (em coloumbs): '))
                var_distancia = float(input('Digite a distância (em metros): '))

                var_campo_eletrico = functions.campoEletrico(var_carga_eletrica, var_distancia)

                print(f'O valor do campo elétrico é de {var_campo_eletrico:.2f} N/C (newtons por coloumbs)')
            elif var_option == '4':
                var_potencia = float(input('Digite o valor da potência (em watts): '))
                var_tempo = float(input('Digite o valor do tempo (em segundos): '))

                var_energia_eletrica_cons = functions.energiaEletricaConsumida(var_potencia, var_tempo)

                print(f'O valor da energia elétrica consumida é de {var_energia_eletrica_cons:.2f} kWh (kilowatts por hora)')
            else:
                print('\33[1;33m Error002: unexpected_choice!\33[m')
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':
    calculadoraEletrica()