
class Validacion():
    def __init__(self):
        pass
    
    def validarNumero(self, numero):
        try:
            numero = int(numero)
            if numero > 0:
                return True
            else:
                return False
        except ValueError:
            return False