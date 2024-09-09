import customtkinter as ctk
from tkinter import messagebox

class EliminarIngrediente:
    def __init__(self, treeview):
        self.treeview = treeview
        self.selected_row = None

    def seleccionar_fila(self):
        selected_item = self.treeview.selection()  # Obtiene el ítem seleccionado en el Treeview
        if selected_item:
            self.selected_row = selected_item[0]
        else:
            self.selected_row = None  # En caso de no haber ítem seleccionado

    def eliminar_dato(self):
        try:
            if self.selected_row:
                self.treeview.delete(self.selected_row)
                self.selected_row = None  # Limpiar la selección después de eliminar
            else:
                # Crear un cuadro de advertencia usando Tkinter
                messagebox.showwarning("Advertencia", "Por favor, selecciona un ingrediente para eliminar.")
        except Exception as e:
            print(f"No se pudo eliminar la fila: {e}")