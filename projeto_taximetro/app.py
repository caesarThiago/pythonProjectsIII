from time import sleep


def calculadoraTaximetro(distancia, valor_km):
    var_total = distancia * valor_km
    return var_total

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def calculadora_taximetro():
    while True:
        var_choice = str(input('Deseja calcular o valor total do taximetro? (Sim/Não): ')).strip().lower()

        if var_choice == 'sim':
            var_distancia = float(input('Digite a distância que deseja percorrer (em quilometros): '))
            var_valor = float(input('Digite o valor a cada quilometro: '))

            var_total = calculadoraTaximetro(var_distancia, var_valor)

            print(f'O valor total do percursso foi de R${var_total:.2f}')
            print()
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice! \33[m')

if __name__ == '__main__':
    calculadora_taximetro()