def calcular(expressao):
    try:
        resultado = eval(expressao)
        return str(resultado)
    except:
        return 'Erro'
