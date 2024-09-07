from clases.validacion import Validacion

class IngresarIngrediente():
    
    def __init__(self):
        pass

    
    def ingresarIngrediente(self, entradaCantidad, entradaNombre, tablaAgregados):
        validado = Validacion()
        numero = entradaCantidad.get()

        if validado.validarNumero(numero):
            ingrediente_seleccionado = entradaNombre.get()
            if ingrediente_seleccionado:
                tablaAgregados.insert("end", f"{ingrediente_seleccionado}: {numero}\n")
            else:
                print("Por favor, selecciona un ingrediente.")
        else:
            print("Por favor, ingresa una cantidad válida.")

