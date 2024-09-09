import customtkinter as ctk
from tkinter import messagebox

class eliminarMenu:
    def __init__(self, treeview, label_total):
        self.treeview = treeview
        self.label_total = label_total
        self.selected_row = None

    def seleccionar_fila(self):
        selected_item = self.treeview.selection()  # Obtiene el ítem seleccionado en el Treeview
        if selected_item:
            self.selected_row = selected_item[0]
        else:
            self.selected_row = None  # En caso de no haber ítem seleccionado

    def eliminar_menu(self):
        try:
            if self.selected_row:
                # Obtener el valor del precio de la fila seleccionada antes de eliminar
                item_values = self.treeview.item(self.selected_row, "values")
                precio = float(item_values[2])
                cantidad = int(item_values[1])
                subtotal = precio * cantidad

                # Eliminar la fila seleccionada
                self.treeview.delete(self.selected_row)
                self.selected_row = None  # Limpiar la selección después de eliminar

                # Actualizar el total restando el subtotal de la fila eliminada
                total_actual = float(self.label_total.cget("text").split("$")[1])
                nuevo_total = total_actual - subtotal
                self.label_total.configure(text=f"Total: ${nuevo_total:.2f}")
            else:
                # Crear un cuadro de advertencia usando Tkinter
                messagebox.showwarning("Advertencia", "Por favor, selecciona un menu para que sea eliminado.")
        except Exception as e:
            print(f"No se pudo eliminar la fila: {e}")