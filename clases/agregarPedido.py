class agregarPedido:()
def agregar_al_pedido(nombre, precio, pedido_treeview, label_total):
    for item in pedido_treeview.get_children():
        item_values = pedido_treeview.item(item, "values")
        if item_values[0] == nombre:
            cantidad_actual = int(item_values[1])
            nueva_cantidad = cantidad_actual + 1
            pedido_treeview.item(item, values=(nombre, nueva_cantidad, precio))
            break
    else:
        pedido_treeview.insert("", "end", values=(nombre, 1, precio))
    
    total_actual = float(label_total.cget("text").split("$")[1])
    nuevo_total = total_actual + precio
    label_total.configure(text=f"Total: ${nuevo_total:.2f}")
