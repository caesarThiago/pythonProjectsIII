
def correnteElétrica(carga_eletrica, intervalo_tempo):
    corrente_eletrica = carga_eletrica / intervalo_tempo
    return corrente_eletrica

def potencialEletrico(carga_eletrica, distancia):
    potencial_eletrico = (9*10**9 * carga_eletrica) / distancia
    return potencial_eletrico

def campoEletrico(carga_eletrica, distancia):
    campo_eletrico = (9*10**9 * carga_eletrica) / distancia **2
    return campo_eletrico

def energiaEletricaConsumida(potencia, tempo):
    energia_eletrica_consumida = potencia * tempo
    return energia_eletrica_consumida
