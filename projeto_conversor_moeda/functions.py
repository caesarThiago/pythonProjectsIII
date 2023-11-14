from forex_python.converter import CurrencyRates

def brlUSD(valor_em_brl):
    c = CurrencyRates()
    conversor_valor = c.convert("BRL", "USD", valor_em_brl)
    return conversor_valor

def usdBRL(valor_em_usd):
    c = CurrencyRates()
    conversor_valor = c.convert("USD", "BRL", valor_em_usd)
    return conversor_valor

def eurUSD(valor_em_eur):
    c = CurrencyRates()
    conversor_valor = c.convert("EUR", "USD", valor_em_eur)
    return conversor_valor

def usdEUR(valor_em_usd):
    c = CurrencyRates()
    conversor_valor = c.convert("USD", "EUR", valor_em_usd)
    return conversor_valor
