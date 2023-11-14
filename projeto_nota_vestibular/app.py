from time import sleep
import functions

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def vestibularNota():
    while True:
        var_choice = str(input('Deseja descobrir a sua nota no vestibular? (Sim/Não): ')).lower().strip()

        if var_choice == 'sim':
            var_ch = int(input('Digite a sua em Ciências Humanas: '))
            var_ex = int(input('Digite a sua nota em Ciências Exatas: '))
            var_cn = int(input('Digite a sua nota em Ciências da Natureza: '))
            var_cl = int(input('Digite a sua nota em Ciências Linguísticas: '))
            var_rd = int(input('Digite a sua em Redação: '))

            var_choice = str(input('Qual área você pretende seguir? (Humanas/Exatas/Naturais/Linguísticas): ')).lower().strip()

            if var_choice == 'humanas':
                var_media = functions.mediaHumanas(var_ch, var_ex, var_cn, var_cl, var_rd)
                if var_media >= 600 and var_ch >= 800:
                    print(f'Sua nota foi de \33[0;32m{var_media}\33[m, Parabéns!')
                elif var_media < 600 and var_ch < 800:
                    print(f'Sua nota foi de \33[0;31m{var_media}\33[m, Melhore na próxima!')
                else:
                    print('\33[1;33m Error002: unexpected_choice!\33[m')
            elif var_choice == 'exatas': 
                var_media = functions.mediaExatas(var_ch, var_ex, var_cn, var_cl, var_rd)
                if var_media >= 600 and var_ex >= 800:
                    print(f'Sua nota foi de \33[0;32m{var_media}\33[m, Parabéns!')
                elif var_media < 600 and var_ex < 800:
                    print(f'Sua nota foi de \33[0;31m{var_media}\33[m, Melhore na próxima!')
                else:
                    print('\33[1;33m Error002: unexpected_choice!\33[m')
            elif var_choice == 'naturais':
                var_media = functions.mediaNatureza(var_ch, var_ex, var_cn, var_cl, var_rd)
                if var_media >= 600 and var_cn >= 800:
                    print(f'Sua nota foi de \33[0;32m{var_media}\33[m, Parabéns!')
                elif var_media < 600 and var_cn < 800:
                    print(f'Sua nota foi de \33[0;31m{var_media}\33[m, Melhore na próxima!')
                else:
                    print('\33[1;33m Error002: unexpected_choice!\33[m')
            elif var_choice == 'linguisticas':
                var_media = functions.mediaLinguistica(var_ch, var_ex, var_cn, var_cl, var_rd)
                if var_media >= 600 and var_cl >= 800:
                    print(f'Sua nota foi de \33[0;32m{var_media}\33[m, Parabéns!')
                elif var_media < 600 and var_cl < 800:
                    print(f'Sua nota foi de \33[0;31m{var_media}\33[m, Melhore na próxima!')
                else:
                    print('\33[1;33m Error002: unexpected_choice!\33[m')
            else:
                print('\33[1;33m Error002: unexpected_choice!\33[m')
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')

if __name__ == '__main__':
    vestibularNota()