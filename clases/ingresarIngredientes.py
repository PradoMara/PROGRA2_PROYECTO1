from clases.validacion import Validacion
from tkinter import messagebox

class IngresarIngrediente:
    def __init__(self, ingredientes_stock):
        self.ingredientes_stock = ingredientes_stock
        self.validado = Validacion()

    def ingresarIngrediente(self, entradaCantidad, entradaNombre, tablaAgregados):
        cantidad = entradaCantidad.get()

        if self.validado.validarNumero(cantidad):
            ingrediente_seleccionado = entradaNombre.get()
            if ingrediente_seleccionado:
                # Verificar si el ingrediente ya está en el stock
                for i, (nombre, cantidad_existente) in enumerate(self.ingredientes_stock):
                    if nombre == ingrediente_seleccionado:
                        # Si ya existe, sumar la cantidad nueva
                        nueva_cantidad = cantidad_existente + int(cantidad)
                        self.ingredientes_stock[i] = (nombre, nueva_cantidad)
                        break
                else:
                    # Si no existe, agregar el ingrediente al stock
                    self.ingredientes_stock.append((ingrediente_seleccionado, int(cantidad)))

                # Actualizar o agregar en la tabla
                for item in tablaAgregados.get_children():
                    item_values = tablaAgregados.item(item, "values")
                    if item_values[0] == ingrediente_seleccionado:
                        # Si el ingrediente ya existe en la tabla, sumar la nueva cantidad
                        nueva_cantidad = int(item_values[1]) + int(cantidad)
                        tablaAgregados.item(item, values=(ingrediente_seleccionado, nueva_cantidad))
                        break
                else:
                    # Si el ingrediente no existe en la tabla, agregar una nueva fila
                    tablaAgregados.insert("", "end", values=(ingrediente_seleccionado, cantidad))
            else:
                messagebox.showwarning("Advertencia", "Por favor, ingrese un ingrediente.")
        else:
            messagebox.showwarning("Advertencia", "El número ingresado debe ser positivo.")

    def obtenerIngredientesStock(self):
        # Implementación de la función para obtener los ingredientes del stock
        return self.ingredientes_stock

