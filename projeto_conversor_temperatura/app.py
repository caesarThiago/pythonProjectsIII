from time import sleep
import functions

def sair():
    print('Ok, saindo...')
    sleep(5)
    print('Programa encerrado!')

var_choice = 'sim'

while var_choice.lower() == 'sim':

    var_choice = input('Deseja converter unidades de temperatura? (Sim/Não): ').strip()

    if var_choice.lower() == 'sim': 
        var_choice = str(input('Qual unidade de temperatura?\n(Celsius para Fahrenheit - 1)\n(Fahrenheit para Celsius - 2)\n(Celsius para Kelvin - 3)\n(Kelvin para Celsius - 4)\n(Fahrenheit para Kelvin - 5)\n(Kelvin para Fahrenheit - 6)\nDigite aqui: ')).strip()

        if var_choice.lower() == 'celsius para fahrenheit' or var_choice.lower() == '1': 
            var_celsius = int(input('Digite a temperatura (em celsius): '))

            var_fahrenheit = functions.celsiusFahrenheit(var_celsius)

            print(f'{var_celsius}ºC é equivalente a {var_fahrenheit:.2f}ºF')

            var_choice = str(input('Deseja converter outra unidade de temperatura? (Sim/Não): '))
        elif var_choice.lower() == 'fahrenheit para celsius' or var_choice.lower() == '2': 
            var_fahrenheit = int(input('Digite a temperatura (em fahrenheit): '))

            var_celsius = functions.fahrenheitCelsius(var_fahrenheit)

            print(f'{var_fahrenheit}ºF é equivalente a {var_celsius:.2f}ºC')
                        
            var_choice = str(input('Deseja converter outra unidade de temperatura? (Sim/Não): '))
        elif var_choice.lower() == 'celsius para kelvin' or var_choice.lower() == '3': 
            var_celsius = int(input('Digite a temperatura (em celsius): '))

            var_kelvin = functions.celsiusKelvin(var_celsius)

            print(f'{var_celsius}ºC é equivalente a {var_kelvin}K')

            var_choice = str(input('Deseja converter outra unidade de temperatura? (Sim/Não): '))
        elif var_choice.lower() == 'kelvin para celsius' or var_choice.lower() == '4': 
            var_kelvin = int(input('Digite a temperatura (em kelvin): '))

            var_celsius = functions.kelvinCelsius(var_kelvin)

            print(f'{var_kelvin}K é equivalente a {var_celsius:.2f}ºC')

            var_choice = str(input('Deseja converter outra unidade de temperatura? (Sim/Não): '))
        elif var_choice.lower() == 'fahrenheit para kelvin' or var_choice.lower() == '5':
            var_fahrenheit = int(input('Digite a temperatura (em fahrenheit): '))

            var_kelvin = functions.fahrenheitKelvin(var_fahrenheit)

            print(f'{var_fahrenheit}ºF é equivalente a {var_kelvin:.2f}K')

            var_choice = str(input('Deseja converter outra unidade de temperatura? (Sim/Não): '))
        elif var_choice.lower() == 'kelvin para fahrenheit' or var_choice.lower() == '6': 
            var_kelvin = int(input('Digite a temperatura (em kelvin): '))

            var_fahrenheit = functions.kelvinFahrenheit(var_kelvin)

            print(f'{var_kelvin}K é equivalente a {var_fahrenheit:.2f}ºF')

            var_choice = str(input('Deseja converter outra unidade de temperatura? (Sim/Não): '))
        else:
            print('\33[1;33mError003: unexpected_value!\33[m')
        
        if var_choice.lower() == 'não':
            sair()
    elif var_choice.lower() == 'não': 
        sair()
    else: 
        print('\33[1;33mError001: invalid_value! or null_value!\33[m')