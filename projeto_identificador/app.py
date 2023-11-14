
def idEmployee(id_emp):
    for i in range(1, id_emp):
        if id_emp >= 1 and id_emp <= 10:
            if id_emp >= 1 and id_emp <= 3:
                print('Você é um segurança!')
                break
            elif id_emp >= 4 and id_emp <= 7:
                print('Você é um zelador')
                break
            else:
                print('Você é um funcionário importante!')
                break
        else:
            print('Você não é um funcionário!')
            break

var_choice = int(input('Digite o número do seu ID: '))

idEmployee(var_choice)