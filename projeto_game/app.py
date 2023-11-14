import random
from time import sleep

def exit():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

def playerMachine():
    list_att = []
    list_def = []
    list_exp = []

    for x in range(1):  
        random_att = random.randint(1, 10)
        list_att.append(random_att)

        random_def = random.randint(1, 10)
        list_def.append(random_def)

        random_exp = random.randint(1, 10) 
        list_exp.append(random_exp)

    var_soma = list_att + list_def + list_exp
    return var_soma

def playerGame():
    while True:
        var_choice = str(input('Deseja jogar contra o PC? (Sim/Não): ')).lower().strip()

        if var_choice == 'sim':
            var_att = int(input('Digite os pontos de ataque (entre 1 e 10): '))
            var_def = int(input('Digite os pontos de defesa (entre 1 e 10): '))
            var_exp = int(input('Digite os pontos de experiência (entre 1 e 10): '))

            resultado_machine = playerMachine()
            var_player_point = var_def + var_att + var_exp
            var_machine_point = sum(resultado_machine)

            if var_player_point > var_machine_point:
                var_pontos_sup = var_player_point - var_machine_point
                print(f'Você ganhou da máquina! Por {var_pontos_sup} pontos')
                sleep(2)
            elif var_machine_point > var_player_point:
                var_pontos_sup = var_machine_point - var_player_point
                print(f'Você perdeu para a máquina! Por {var_pontos_sup} pontos')
                sleep(2)
            else:
                print(f'Você empatou com a máquina!')
        elif var_choice == 'não':
            exit()
            break
        else:
            print('\33[1;33m Error001: invalid_choice!\33[m')
if __name__ == '__main__':
    playerGame()