import random
from time import sleep

var_choice = 'Sim'

while var_choice.lower() == 'sim':

    def randomNumber(numero):
        numero = random.randint(1, 100)
        return numero

    var_choice = input('Deseja jogar adivinhe o número? (Sim/Não): ').strip().lower()
            
    if var_choice == 'sim':
        print('Ok, vamos brincar!')
        var_choice = int(input('Digite um número inteiro de 1 a 100: '))
                
        num = randomNumber(var_choice)
        
        if var_choice == num:
            print('Parabéns, você acertou!')
            var_choice = str(input('Deseja continuar? (Sim/Não): ')).lower()
        elif var_choice != num:
            print(f'Você errou! O número correto era {num}.')
            var_choice = str(input('Deseja continuar? (Sim/Não): ')).lower()
        else:
            print('Error002: invalid_number!')
            
        print('Ok, saindo!')
        sleep(5)
        print('Programa encerrado!')
    elif var_choice == 'não':
        print('Ok, saindo!')
        sleep(5)
        print('Programa encerrado!')
    else:
        print('Error001: invalid_choice!')