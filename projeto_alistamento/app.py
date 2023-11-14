from time import sleep

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def alistamento():
    while True:
        var_choice = str(input('Deseja descobri se precisa se alistar? (Sim/Não): ')).strip().lower()

        if var_choice == 'sim':
            var_ano = int(input('Informe o ano de seu nascimento: '))
            var_ano_atual = 2023

            var_idade = var_ano_atual - var_ano
            var_ano_falt = 18 - var_idade

            if var_idade < 18:
                print(f'Você tem {var_idade} ano(s), ainda falta(m) {var_ano_falt} ano(s)!')
                print()
            elif var_idade == 18:
                print(f'Você tem {var_idade} ano(s), está na hora de alistar-se!')
                print()
            elif var_idade > 18:
                print(f'Você tem {var_idade} ano(s), já passou a hora de alistar-se!')
                print()
            else:
                print('\33[1;33m Error002: unexpected_value!\33[m')
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':
    alistamento()
