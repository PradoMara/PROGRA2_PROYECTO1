from clases.validacion import Validacion

class IngresarIngrediente:
    
    def __init__(self):
        self.validado = Validacion()

    def ingresarIngrediente(self, entradaCantidad, entradaNombre, tablaAgregados):

        cantidad = entradaCantidad.get()
        

        if self.validado.validarNumero(cantidad):
            ingrediente_seleccionado = entradaNombre.get()
            if ingrediente_seleccionado: 
                for item in tablaAgregados.get_children():
                    item_values = tablaAgregados.item(item, "values")
                    if item_values[0] == ingrediente_seleccionado:
                        # Si el ingrediente ya existe, sumar la nueva cantidad a la cantidad existente
                        cantidad_existente = int(item_values[1])
                        nueva_cantidad = cantidad_existente + int(cantidad)
                        tablaAgregados.item(item, values=(ingrediente_seleccionado, nueva_cantidad))
                        break
                else:
                    # Si el ingrediente no existe, insertar una nueva fila
                    tablaAgregados.insert("", "end", values=(ingrediente_seleccionado, cantidad))
            else:
                print("Por favor, selecciona un ingrediente.")
        else:
            print("Por favor, ingresa una cantidad válida.")