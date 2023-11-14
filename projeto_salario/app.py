from time import sleep


def aumentoSalarial (salario, taxa_aumento):
    var_aumento = salario * (1 + taxa_aumento/100)
    return var_aumento

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def salarioCalculator():
        while True: 
            var_choice = str(input('Deseja descobrir o valor do total do aumento salarial? (Sim/Não): ')).strip().lower()

            if var_choice == 'sim':
                var_salario = float(input('Digite o seu salário: '))
                var_taxa = float(input('Digite a taxa de aumento: '))

                var_aumento = aumentoSalarial(var_salario, var_taxa)

                print(f'O valor total com o aumento salarial de {var_taxa}% é de R${var_aumento:.2f}')
                print()
            elif var_choice == 'não':
                exit()
                break
            else:
                print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':
    salarioCalculator()