import customtkinter as ctk
from tkinter import messagebox

class eliminarIngrediente():

    def __init__(self):
        pass
    
    def SeleccionarFila():
        global selected_row
        selected_item = Tabla.focus()  # Obtiene el ítem seleccionado en la tabla 
        if selected_item:
            selected_row = selected_item
        else:
            selected_row = None  # En caso de no haber ítem seleccionado

    def EliminarDato():
        # Definir la función para eliminar una fila
        global selected_row
        try:
            if selected_row:
                Tabla.delete(selected_row)
                selected_row = None  # Limpiar la selección después de eliminar
            else:
                # Crear un cuadro de advertencia usando Tkinter
                messagebox.showwarning("Advertencia", "Por favor, selecciona una fila para eliminar.")
        except Exception as e:
            print(f"No se pudo eliminar la fila: {e}")
        pass