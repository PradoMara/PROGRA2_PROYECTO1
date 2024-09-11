def agregar_al_pedido(nombre, precio, pedido_treeview, label_total):
    # Actualizar el Treeview con el nuevo pedido
    for item in pedido_treeview.get_children():
        item_values = pedido_treeview.item(item, "values")
        if item_values[0] == nombre:
            cantidad_actual = int(item_values[1])
            nueva_cantidad = cantidad_actual + 1
            pedido_treeview.item(item, values=(nombre, nueva_cantidad, precio))
            break
    else:
        pedido_treeview.insert("", "end", values=(nombre, 1, precio))

    # Obtener el total actual y actualizarlo
    try:
        # Eliminar las comas del texto antes de convertirlo a float
        total_texto = label_total.cget("text").split("$")[1].replace(",", "").strip()
        total_actual = float(total_texto)
    except ValueError:
        total_actual = 0.0  # En caso de que la conversión falle, empezar con 0.0

    nuevo_total = total_actual + precio
    label_total.configure(text=f"Total: ${nuevo_total:.2f}")


