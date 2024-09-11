import customtkinter as ctk
from tkinter import messagebox

class GenerarMenu:
    def __init__(self, pedido_treeview, label_total, ingredientes_stock):
        self.pedido_treeview = pedido_treeview
        self.label_total = label_total
        self.ingredientes_stock = ingredientes_stock

    def generar(self, menus, verificador):
        total = 0.0
        for nombre_menu, ingredientes in menus.items():
            # Verificar cuántas unidades se pueden hacer con los ingredientes disponibles
            cantidades_posibles = []
            for ingrediente, cantidad_requerida in ingredientes.items():
                cantidad_actual = self.obtener_ingrediente(ingrediente)
                if cantidad_actual > 0:
                    # Calcular cuántas unidades completas del menú se pueden hacer
                    cantidades_posibles.append(cantidad_actual // cantidad_requerida)
                else:
                    cantidades_posibles.append(0)

            # Calcular la cantidad mínima de unidades que se pueden hacer
            unidades_menu = min(cantidades_posibles)

            if unidades_menu > 0:
                # Agregar la cantidad de unidades del menú generadas
                self.agregar_itm_pedido(nombre_menu, unidades_menu, self.obtener_precio(nombre_menu))

                # Consumir ingredientes para las unidades generadas
                self.consumir_ingredientes(ingredientes, unidades_menu)

                # Calcular el total a pagar
                total += self.obtener_precio(nombre_menu) * unidades_menu
                self.actualizar_total(total)
            else:
                # Si faltan ingredientes para generar al menos una unidad
                faltantes = verificador.verificar(ingredientes)
                mensaje = f"Faltan ingredientes para {nombre_menu}: \n" + "\n".join([f"{ing} (Faltan {cant})" for ing, cant in faltantes])
                print(mensaje)

    def agregar_itm_pedido(self, nombre, cantidad, precio_unitario):
        self.pedido_treeview.insert("", "end", values=(nombre, cantidad, precio_unitario))

    def obtener_precio(self, menu):
        precios = {
            "Papas fritas": 500,
            "Pepsi": 1100,
            "Completo": 1800,
            "Hamburguesa": 3500
        }
        return precios.get(menu, 0)
    
    def obtener_ingrediente(self, ingrediente):
        # Buscar el ingrediente en el stock
        for ing, cantidad in self.ingredientes_stock:
            if ing == ingrediente:
                return cantidad
        return 0

    def consumir_ingredientes(self, menu, unidades_menu):
        """Consume los ingredientes del stock en función de las unidades del menú generadas."""
        for ingrediente, cantidad_requerida in menu.items():
            for i, (nombre_ingrediente, cantidad_actual) in enumerate(self.ingredientes_stock):
                if nombre_ingrediente == ingrediente:
                    # Restar la cantidad de ingredientes consumidos por las unidades generadas
                    nueva_cantidad = cantidad_actual + (cantidad_requerida * unidades_menu)
                    self.ingredientes_stock[i] = (nombre_ingrediente, nueva_cantidad)
                    break

    def devolver_ingredientes(self, menu, unidades_menu):
        """Devuelve los ingredientes al stock en función de las unidades del menú eliminadas."""
        for ingrediente, cantidad_requerida in menu.items():
            for i, (nombre_ingrediente, cantidad_actual) in enumerate(self.ingredientes_stock):
                if nombre_ingrediente == ingrediente:
                    # Sumar la cantidad de ingredientes consumidos por las unidades eliminadas
                    nueva_cantidad = cantidad_actual - (cantidad_requerida * unidades_menu)
                    self.ingredientes_stock[i] = (nombre_ingrediente, nueva_cantidad)
                    break

    def actualizar_total(self, total):
        """Actualiza el total formateado en la etiqueta."""
        self.label_total.configure(text=f"Total: ${total:.2f}")
