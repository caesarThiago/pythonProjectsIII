from time import sleep


def impostoCarro(valor_original): 
    var_valor_atual = valor_original * 1.393
    return var_valor_atual

def code():
    while True:
        var_choice = str(input('Deseja descobrir quanto de imposto foi taxado em seu carro? (Sim/Não): ')).strip().lower()

        if var_choice == 'sim':
            var_valor = float(input("Digite o valor original do carro: "))

            var_total = impostoCarro(var_valor)

            print(f'O valor do carro com o imposto de 39.3% é de R${var_total:.2f}')
            sleep(5)
        elif var_choice == 'não':
            print('Ok, saindo!')
            sleep(5)
            print('Programa encerrado!')
            break
        else:
            print('Error001: invalid_choice!')

if __name__ == '__main__':
    code()