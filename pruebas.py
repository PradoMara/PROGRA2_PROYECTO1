import customtkinter as ctk
from PIL import Image
from clases.ingresarIngredientes import ingresarIngrediente
from clases.eliminarIngrediente import eliminarIngrediente
from clases.generarMenu import generarMenu
from clases.crearTarjeta import crear_tarjeta
from clases.generarBoleta import generarBoleta



app = ctk.CTk()
app.title("Gestión de ingredientes y pedidos")
app.geometry("800x600")

frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

pestañas = ctk.CTkTabview(frame)
pestañas.pack(fill="both", expand=True)

pestañaIngredientes = pestañas.add("Ingreso de Ingredientes")
pestañaPedidos = pestañas.add("Pedidos")

#--------------------------------------PESTAÑA INGRESO INGREDIENTES---------------------------------------------------#

# label ingrediente
etiquetaNombre = ctk.CTkLabel(pestañaIngredientes, text="Nombre del Ingrediente:")
etiquetaNombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
# entrada ingrediente
entradaNombre = ctk.CTkEntry(pestañaIngredientes)
entradaNombre.grid(row=0, column=1, padx=10, pady=10)
# label cantidad
etiquetaCantidad = ctk.CTkLabel(pestañaIngredientes, text="Cantidad:")
etiquetaCantidad.grid(row=1, column=0, padx=10, pady=10, sticky="w")
# entrada cantidad
entradaCantidad = ctk.CTkEntry(pestañaIngredientes)
entradaCantidad.grid(row=1, column=1, padx=10, pady=10)
# botón ingresar
botonIngresarr = ctk.CTkButton(pestañaIngredientes, text="Ingresar Ingrediente", command=lambda: ingresarIngrediente())
botonIngresarr.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# tabla de ingredientes agregados
tablaAgregados= ctk.CTkTextbox(pestañaIngredientes, width=400, height=200)
tablaAgregados.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

# botón eliminar ingredientes
botonEliminar = ctk.CTkButton(pestañaIngredientes, text="Eliminar Ingrediente", command=lambda: eliminarIngrediente())
botonEliminar.grid(row=3, column=2, padx=10, pady=10)

# botón generar menú
botonGenerarMenu = ctk.CTkButton(frame, text="Generar Menú", width=300, command=lambda: generarMenu())
botonGenerarMenu.pack(pady=10)

#----------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------PESTAÑA PEDIDOS-------------------------------------------------------#


tarjetas_frame = ctk.CTkFrame(pestañaPedidos)
tarjetas_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Ejemplo de cómo agregar tarjetas (menu sería una instancia de una clase que contenga la información del menú)
menus = [
    {"nombre": "Papas Fritas", "precio": 500, "icono_menu": "imgs/papas.png"},
    {"nombre": "Completo", "precio": 1800, "icono_menu": "imgs/completo.png"},
    {"nombre": "Pepsi", "precio": 1100, "icono_menu": "imgs/pepsi.png"},
    {"nombre": "Hamburguesa", "precio": 3500, "icono_menu": "imgs/hamburguesa.png"},
]

# Crear un diccionario para almacenar las imágenes
imagenes_menus = {}

for menu in menus:
    # Aquí deberías cargar la imagen desde el archivo real
    icono_menu = ctk.CTkImage(file=menu["icono_menu"])
    menu["icono_menu"] = icono_menu  # Asigna la imagen al menú
    crear_tarjeta(menu)  # Crea la tarjeta para el menú

# Treeview para mostrar el pedido
pedido_treeview = ctk.CTkTreeview(pestañaPedidos, columns=("Nombre del Menú", "Cantidad", "Precio Unitario"), show="headings")
pedido_treeview.heading("Nombre del Menú", text="Nombre del Menú")
pedido_treeview.heading("Cantidad", text="Cantidad")
pedido_treeview.heading("Precio Unitario", text="Precio Unitario")
pedido_treeview.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Etiqueta para mostrar el total del pedido
label_total = ctk.CTkLabel(pestañaPedidos, text="Total: $0.00", font=("Helvetica", 16, "bold"))
label_total.grid(row=2, column=0, padx=10, pady=10, sticky="e")

# Botón para generar boleta
botonGenerarBoleta = ctk.CTkButton(pestañaPedidos, text="Generar Boleta", command=lambda: generarBoleta())
botonGenerarBoleta.grid(row=3, column=0, padx=10, pady=10, sticky="e")

#----------------------------------------------------------------------------------------------------------------------#

app.mainloop()
