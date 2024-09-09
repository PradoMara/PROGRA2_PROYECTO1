import customtkinter as ctk
from clases.clickTarjeta import tarjetaClick

def crear_tarjeta(menu, tarjetas_frame, pedido):
    # Determinar la posición de la nueva tarjeta
    num_tarjetas = len(pedido.get_children())
    fila = num_tarjetas // 2
    columna = num_tarjetas % 2

    # Crear la tarjeta con un tamaño fijo
    tarjeta = ctk.CTkFrame(tarjetas_frame, corner_radius=10, border_width=1, border_color="#4CAF50", width=150, height=150, fg_color="transparent")
    tarjeta.grid(row=fila, column=columna, padx=15, pady=15, sticky="nsew")

    # Asegurarse de que cada celda se configure correctamente para expandirse
    tarjetas_frame.grid_rowconfigure(fila, weight=1)
    tarjetas_frame.grid_columnconfigure(columna, weight=1)

    tarjeta.bind("<Button-1>", lambda event, m=menu: tarjetaClick(event, m))
    # Hacer que la tarjeta sea completamente clickeable 

    # Cambiar el color del borde cuando el mouse pasa sobre la tarjeta
    tarjeta.bind("<Enter>", lambda event: tarjeta.configure(border_color="#FF0000"))  # Cambia a rojo al pasar el mouse
    tarjeta.bind("<Leave>", lambda event: tarjeta.configure(border_color="#4CAF50"))  # Vuelve al verde al salir

    # Verifica si hay una imagen asociada con el menú
    if menu["icono_menu"]:
        # Crear y empaquetar el CTkLabel con la imagen, sin texto y con fondo transparente
        imagen_label = ctk.CTkLabel(tarjeta, image=menu["icono_menu"], width=64, height=64, text="", fg_color="transparent")
        imagen_label.pack(anchor="center", pady=5, padx=10)
        imagen_label.bind("<Button-1>", lambda event, m=menu: tarjetaClick(event, m))

        # Agregar un Label debajo de la imagen para mostrar el nombre del menú
        texto_label = ctk.CTkLabel(tarjeta, text=f"{menu['nombre']}", text_color="black", font=("Helvetica", 12, "bold"), fg_color="transparent")
        texto_label.pack(anchor="center", pady=1)
        texto_label.bind("<Button-1>", lambda event, m=menu: tarjetaClick(event, m))

    else:
        print(f"No se pudo cargar la imagen para el menú '{menu['nombre']}'")