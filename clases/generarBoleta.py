import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

class generarBoleta:
    def __init__(self):
        # Inicializa los datos dentro de la clase
        self.datos = [
            ("Papas Fritas", 2, 500.00, 1000.00), 
            ("Completo", 2, 1800.00, 3600.00), 
            ("Pepsi", 3, 1100.00, 3300.00), 
            ("Hamburguesa", 2, 3500.00, 7000.00)
        ]
        self.carpeta_boletas = "Boletas"

        # Crear la carpeta "Boletas" si no existe
        if not os.path.exists(self.carpeta_boletas):
            os.makedirs(self.carpeta_boletas)

    def crear_pdf(self, nombre_archivo):
        # Generar la ruta completa para el PDF
        ruta_pdf = os.path.join(self.carpeta_boletas, nombre_archivo)

        FechaActual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Crear el archivo PDF
        c = canvas.Canvas(ruta_pdf, pagesize=A4)
        c.drawString(100, 800, "Boleta Restaurante")
        c.drawString(100, 785, "Razón Social del Negocio")
        c.drawString(100, 770, "RUT: 12345678-9")
        c.drawString(100, 755, "Dirección: Calle Falsa 123")
        c.drawString(100, 740, "Teléfono: +56 9 1234 5678")
        c.drawString(400, 800, f"Fecha: {FechaActual}")

        # Encabezados de la tabla
        x, y = 100, 700
        c.drawString(x, y, "Nombre")
        c.drawString(x + 100, y, "Cantidad")
        c.drawString(x + 200, y, "Precio Unitario")
        c.drawString(x + 300, y, "Subtotal")
        y -= 20

        # Agregar los datos de la tabla
        for item in self.datos:
            c.drawString(x, y, item[0])
            c.drawString(x + 100, y, str(item[1]))
            c.drawString(x + 200, y, f"${item[2]:,.2f}")
            c.drawString(x + 300, y, f"${item[3]:,.2f}")
            y -= 20

        # Calcular y mostrar subtotales
        subtotal = sum(item[3] for item in self.datos)
        iva = subtotal * 0.19
        total = subtotal + iva

        c.drawString(100, y - 20, f"Subtotal: ${subtotal:,.2f}")
        c.drawString(100, y - 40, f"IVA (19%): ${iva:,.2f}")
        c.drawString(100, y - 60, f"Total: ${total:,.2f}")

        c.drawString(100, y - 100, "Gracias por su compra. Para cualquier consulta, llamenos al +56 9 1234 5678.")
        c.drawString(100, y - 120, "Los productos adquiridos no tienen garantía.")

        c.save()
        print(f"Su Boleta fue guardada en: {ruta_pdf}")

    def generaBoleta(self):
        # Método que será llamado por el botón para generar la boleta
        self.crear_pdf("boleta.pdf")