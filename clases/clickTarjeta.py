import customtkinter as ctk

#codigo de ayuda para desarrollar el evento que se debe gatillar, cuando se presiona cada targeta(Menu)
def tarjetaClick(self, event, menu):
        # Verificar si hay suficientes ingredientes en el stock para preparar el menú
        if self.stock.lista_ingredientes==[]:
            suficiente_stock=False
        for ingrediente_necesario in menu.ingredientes:
            for ingrediente_stock in self.stock.lista_ingredientes:
                if ingrediente_necesario.nombre == ingrediente_stock.nombre:
                    if int(ingrediente_stock.cantidad) < int(ingrediente_necesario.cantidad):
                        suficiente_stock = False
                        break
            if not suficiente_stock:
                break
                
        if suficiente_stock:
            # Descontar los ingredientes del stock
            for ingrediente_necesario in menu.ingredientes:
                for ingrediente_stock in self.stock.lista_ingredientes:
                    if ingrediente_necesario.nombre == ingrediente_stock.nombre:
                        ingrediente_stock.cantidad = str(int(ingrediente_stock.cantidad) - int(ingrediente_necesario.cantidad))
            
            # Agregar el menú al pedido
            self.pedido.agregar_menu(menu)
            
            # Actualizar el Treeview
            self.actualizar_treeview_pedido()

            # Actualizar el total del pedido
            total = self.pedido.calcular_total()
            self.label_total.configure(text=f"Total: ${total:.2f}")
        else:
            # Mostrar un mensaje indicando que no hay suficientes ingredientes usando CTkMessagebox
            ctk.Messagebox(title="Stock Insuficiente", message=f"No hay suficientes ingredientes para preparar el menú '{menu.nombre}'.", icon="warning")
