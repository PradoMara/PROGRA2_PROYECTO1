class VerificarStock:
    def __init__(self, ingredientes_stock):
        self.ingredientes_stock = ingredientes_stock

    def verificar(self, menu):
        faltantes = []
        for ingrediente, cantidad_necesaria in menu.items():
            cantidad_disponible = self.obtener_cantidad_disponible(ingrediente)
            if cantidad_disponible < cantidad_necesaria:
                faltantes.append((ingrediente, cantidad_necesaria - cantidad_disponible))
        return faltantes

    def obtener_cantidad_disponible(self, ingrediente):
        for nombre_ingrediente, cantidad in self.ingredientes_stock:
            if nombre_ingrediente == ingrediente:
                return cantidad
        return 0


