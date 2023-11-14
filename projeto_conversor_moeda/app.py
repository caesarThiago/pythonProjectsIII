import functions
from time import sleep


def sair():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

var_choice = 'sim'
    
while var_choice.lower() == 'sim':

    var_choice = str(input('Deseja utilizar o conversor de moedas? (Sim/Não): ')).strip().lower()

    if var_choice == 'sim':
        var_choice = str(input('Escolha a conversão: (BRL/USD) (USD/BRL) (EUR/USD) (USD/EUR): ')).strip().lower()

        if var_choice == 'brl/usd':
            var_valor = float(input('Digite o valor (em BRL): '))
            var_valor_convertido = functions.brlUSD(var_valor)
            print(f'O valor R${var_valor:.2f} em dolar(es) é ${var_valor_convertido:.2f}')
            sleep(3)
            var_choice = str(input('Deseja converter outra moeda? (Sim/Não): ')).lower()
        elif var_choice == 'usd/brl':
            var_valor = float(input('Digite o valor (em USD): '))
            var_valor_convertido = functions.usdBRL(var_valor)
            print(f'O valor ${var_valor:.2f} em real(is) é R${var_valor_convertido:.2f}')
            sleep(3)
            var_choice = str(input('Deseja converter outra moeda? (Sim/Não): ')).lower()
        elif var_choice == 'eur/usd':
            var_valor = float(input('Digite o valor (em EUR): '))
            var_valor_convertido = functions.eurUSD(var_valor)
            print(f'O valor €{var_valor:.2f} em dolar(es) é ${var_valor_convertido:.2f}')
            sleep(3)
            var_choice = str(input('Deseja converter outra moeda? (Sim/Não): ')).lower()
        elif var_choice == 'usd/eur':
            var_valor = float(input('Digite o valor (em USD): '))
            var_valor_convertido = functions.usdEUR(var_valor)
            print(f'O valor ${var_valor:.2f} em euro(s) é €{var_valor_convertido:.2f}')
            sleep(3)
            var_choice = str(input('Deseja converter outra moeda? (Sim/Não): ')).lower()
        else:
            print('\33[1;33m Error002: unexpected_choice!\33[m')
        
        if var_choice.lower() == 'não':
            sair()

    elif var_choice == 'não':
        sair()
    else:
        print('\33[1;33m Error001: invalid_choice!\33[m')