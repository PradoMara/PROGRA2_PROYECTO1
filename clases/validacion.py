import customtkinter as ctk
from tkinter import messagebox

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
            messagebox.showwarning("Advertencia", "Ingresa un numero entero positivo.")
            return False


