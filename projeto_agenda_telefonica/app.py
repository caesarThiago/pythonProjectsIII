from time import sleep

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def agendaTel():
    while True:
        var_choice = input('Deseja guardar um número de telefone em sua agenda? (Sim/Não): ').strip().lower()

        if var_choice == 'sim':
            lista_num = []
            while True:
                var_numero = input('Digite o número de telefone que deseja guardar: ')
                lista_num.append(var_numero)
                var_choice = input('Deseja guardar mais algum número? (Sim/Não): ').strip().lower()
                if var_choice != 'sim':
                    break

            var_choice = input('Deseja mostrar o número guardado? (Sim/Não): ').strip().lower()

            if var_choice == 'sim':
                print(f'O(s) número(s) de telefone(s) é(são) {", ".join(lista_num)}')
            elif var_choice == 'não':
                print('Ok, número guardado!')
                break
            else:
                print('\33[1;33m Error002: unexpected_choice!\33[m')
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')  
if __name__ == '__main__':
    agendaTel()