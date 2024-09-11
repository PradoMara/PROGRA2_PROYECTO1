import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from tkinter import messagebox

class generarBoleta:
    def __init__(self, pedido_treeview):
        self.pedido_treeview = pedido_treeview
        self.carpeta_boletas = "Boletas"

        # Crear la carpeta "Boletas" si no existe
        if not os.path.exists(self.carpeta_boletas):
            os.makedirs(self.carpeta_boletas)

    def obtener_datos_pedido(self):
        # Obtener datos del Treeview de agregarPedido y convertirlos en una lista
        datos = []  # Lista con los datos
        for item in self.pedido_treeview.get_children():
            item_values = self.pedido_treeview.item(item, "values")
            nombre, cantidad, precio = item_values[0], int(item_values[1]), float(item_values[2])
            subtotal = cantidad * precio
            datos.append((nombre, cantidad, precio, subtotal))
        return datos

    def crear_pdf(self, nombre_archivo):
        # Generar la ruta completa para el PDF
        ruta_pdf = os.path.join(self.carpeta_boletas, nombre_archivo)

        # Obtener la fecha y hora actual
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Crear el archivo PDF
        c = canvas.Canvas(ruta_pdf, pagesize=A4)
        c.drawString(100, 800, "Boleta Restaurante")
        c.drawString(100, 785, "Los LonkoPinin")
        c.drawString(100, 770, "RUT: 11222333-4")
        c.drawString(100, 755, "Dirección: Calle Las Mojojo 69")
        c.drawString(100, 740, "Teléfono: +56 9 8765 4321")
        c.drawString(400, 800, f"Fecha: {fecha_actual}")

        # Encabezados de la tabla
        x, y = 100, 700
        c.drawString(x, y, "Nombre")
        c.drawString(x + 100, y, "Cantidad")
        c.drawString(x + 200, y, "Precio Unitario")
        c.drawString(x + 300, y, "Subtotal")
        y -= 20

        # Obtener datos del pedido
        datos = self.obtener_datos_pedido()

        # Agregar los datos de la tabla
        for item in datos:
            c.drawString(x, y, item[0])
            c.drawString(x + 100, y, str(item[1]))
            c.drawString(x + 200, y, f"${item[2]:,.2f}")
            c.drawString(x + 300, y, f"${item[3]:,.2f}")
            y -= 20

        # Calcular y mostrar subtotales
        subtotal = sum(item[3] for item in datos)
        iva = subtotal * 0.19
        total = subtotal + iva

        c.drawString(100, y - 20, f"SubTotal: ${subtotal:,.2f}")
        c.drawString(100, y - 40, f"IVA (19%): ${iva:,.2f}")
        c.drawString(100, y - 60, f"Total: ${total:,.2f}")

        c.drawString(100, y - 100, "Gracias por su compra. Para cualquier consulta, llámenos al +56 9 8765 4321.")
        c.drawString(100, y - 120, "Los productos adquiridos no tienen garantía.")

        c.save()
        print(f"PDF guardado en: {ruta_pdf}")

    def generar_boleta_evento(self):
        # Verifica si hay datos en el Treeview
        if not self.pedido_treeview.get_children():
            messagebox.showwarning(title="Advertencia", message="No hay ningún pedido en el menú. Por favor, ingrese un pedido.")
            return

        # Llama al método para crear el PDF si hay datos
        self.crear_pdf("boleta.pdf")