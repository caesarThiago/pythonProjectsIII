import math

def razaoPg(a1, a2):
    var_razao = a1 / a2 
    return var_razao

def somaTermos(a1, q, n): 
    if q > 1 and q != 0: 
        var_soma_termos = a1 * (math.pow(q, n) - 1) / (q - 1)
        return var_soma_termos
    elif q < 1 and q != 0:
        var_soma_termos = a1 * (1 - math.pow(q, n)) / (1 - q)
        return var_soma_termos
    else:
        print('\33[1;33m Error003: unexpected_value!\33[m')

def termoMedio(a1, an):
    var_termo_medio = math.sqrt(a1 * an)
    return var_termo_medio