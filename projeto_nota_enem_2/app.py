from time import sleep
import functions

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def enemNota():
    while True:
        var_choice = str(input('Deseja descobrir a sua nota do enem? (Sim/Não): ')).strip().lower()

        if var_choice == 'sim':
            var_cht = int(input('Digite a sua nota de Ciências Humanas e suas Tecnologias: '))
            var_cnt = int(input('Digite a sua nota de Ciências da Natureza e suas Tecnologias: '))
            var_lct = int(input('Digite a sua nota de Linguaguens, Códigos e suas Tecnologias: '))
            var_mat = int(input('Digite a sua nota de Matemática: '))
            var_red = int(input('Digite a sua nota de Redação: '))

            var_nota_enem = functions.mediaEnem(var_cht, var_cnt, var_lct, var_mat, var_red)

            if var_nota_enem >= 600:
                print(f'A sua nota foi de \33[0;32m{var_nota_enem}\33[m, Parabens!')
            elif var_nota_enem < 600:
                print(f'A sua nota foi de \33[0;31m{var_nota_enem}\33[m, Melhore na próxima!')
            else:
                print('\33[1;33m Error002: unexpected_value!\33')
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':
    enemNota()