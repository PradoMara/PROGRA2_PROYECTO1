from clases.validacion import Validacion

class IngresarIngrediente():
    
    def __init__(self):
        self.validado = Validacion()

    
    def ingresarIngrediente(self, entradaCantidad, entradaNombre, tablaAgregados):

        cantidad = entradaCantidad.get()
        

        if self.validado.validarNumero(cantidad):
            ingrediente_seleccionado = entradaNombre.get()
            if ingrediente_seleccionado:
                tablaAgregados.insert("end", f"{ingrediente_seleccionado}: {cantidad}\n")
            else:
                print("Por favor, selecciona un ingrediente.")
        else:
            print("Por favor, ingresa una cantidad válida.")

