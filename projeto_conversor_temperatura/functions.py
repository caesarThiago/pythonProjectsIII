def celsiusFahrenheit (temperatura_celsius): 
    var_temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
    return var_temperatura_fahrenheit

def fahrenheitCelsius(temperatura_fahrenheit): 
    var_temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9
    return var_temperatura_celsius

def celsiusKelvin(temperatura_celsius): 
    var_temperatura_kelvin = temperatura_celsius + 273.15
    return var_temperatura_kelvin

def kelvinCelsius(temperatura_kelvin): 
    var_temperatura_celsius = temperatura_kelvin - 273.15
    return var_temperatura_celsius

def fahrenheitKelvin(temperatura_fahrenheit): 
    var_temperatura_kelvin = (temperatura_fahrenheit - 32) * 5/9 + 273.15
    return var_temperatura_kelvin

def kelvinFahrenheit(temperatura_kelvin): 
    var_temperatura_fahrenheit = (temperatura_kelvin - 273.15) * 9/5 + 32
    return var_temperatura_fahrenheit

