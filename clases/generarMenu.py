# from app import * #NO ES NECESARIO ESTA LINEA, DE LO CONTRARIO DA ERROR


class GenerarMenu():
    def __init__(self, pedido_treeview, label_total):
        self.pedido_treeview = pedido_treeview
        self.label_total = label_total
        self.total = 0.0

    def agregarItm(self, nombre, cantidad, precio_unitario):
        self.pedido_treeview.insert("", "end", values=(nombre, cantidad, precio_unitario))

        # Actualiza el total
        self.total += float(cantidad) * float(precio_unitario)
        self.label_total.configure(text=f"Total: ${self.total:.2f}")

    def limpiarMenu(self):
        # Limpia el Treeview
        for itms in self.pedido_treeview.get_children():
            self.pedido_treeview.delete(itms)

        self.total = 0.0
        self.label_total.configure(text=f"Total: ${self.total:.2f}")

    def generar_Menu(self, menuItms):
        self.limpiarMenu()
        
        for itms in menuItms:
            self.agregarItm(itms["nombre"], itms.get("cantidad", 1), itms["precio"])
