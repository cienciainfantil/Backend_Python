def mayuscula(texto):
    return texto.upper()

def decoradorMayuscula(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@decoradorMayuscula
def mensaje(texto):
    return 'texto: '+texto

print(mensaje('Hola con decorador'))


