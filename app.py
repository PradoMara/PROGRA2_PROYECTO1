import customtkinter as ctk
from tkinter import ttk 
from PIL import Image
from clases.agregarPedido import agregar_al_pedido
from clases.clickTarjeta import tarjetaClick
from clases.ingresarIngredientes import IngresarIngrediente
from clases.eliminarIngrediente import eliminarIngrediente
from clases.generarMenu import generarMenu
from clases.crearTarjeta import crear_tarjeta
from clases.generarBoleta import generarBoleta

#-----------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------- Instancia de la aplicación -----------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------#

ingresoIng = IngresarIngrediente()


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
#Ingredientes disponibles en el combobox
ingredienteDisp = ["Papas", "Bebida", "Vienesas", "Pan de Completo", "Tomate", "Palta", "Pan de Hamburguesa", "Lamina de Queso", "Churrasco de Carne"]

# label ingrediente
etiquetaNombre = ctk.CTkLabel(pestañaIngredientes, text="Nombre del Ingrediente:")
etiquetaNombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
# entrada ingrediente
entradaNombre = ctk.CTkComboBox(pestañaIngredientes, values=ingredienteDisp)
entradaNombre.grid(row=0, column=1, padx=10, pady=10)
# label cantidad
etiquetaCantidad = ctk.CTkLabel(pestañaIngredientes, text="Cantidad:")
etiquetaCantidad.grid(row=1, column=0, padx=10, pady=10, sticky="w")
# entrada cantidad
entradaCantidad = ctk.CTkEntry(pestañaIngredientes)
entradaCantidad.grid(row=1, column=1, padx=10, pady=10)
# botón ingresar
botonIngresarr = ctk.CTkButton(pestañaIngredientes, text="Ingresar Ingrediente", command=lambda: ingresoIng.ingresarIngrediente(entradaCantidad, entradaNombre, tablaAgregados))   
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

# Definición de tu marco y Treeview
tarjetas_frame = ctk.CTkFrame(pestañaPedidos)
tarjetas_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Define el Treeview usando ttk.Treeview
pedido_treeview = ttk.Treeview(pestañaPedidos, columns=("Nombre del Menú", "Cantidad", "Precio Unitario"), show="headings")
pedido_treeview.heading("Nombre del Menú", text="Nombre del Menú")
pedido_treeview.heading("Cantidad", text="Cantidad")
pedido_treeview.heading("Precio Unitario", text="Precio Unitario")
pedido_treeview.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Asegúrate de que la pestañaPedidos se expanda correctamente
pestañaPedidos.grid_rowconfigure(0, weight=1)
pestañaPedidos.grid_columnconfigure(0, weight=1)
pestañaPedidos.grid_rowconfigure(1, weight=1)
pestañaPedidos.grid_columnconfigure(1, weight=1)


# Crear las tarjetas de menú
menu = [
    {"nombre": "Hamburguesa", "precio": 3500, "icono_menu": "imgs/hamburguesa.png"},
    {"nombre": "Pepsi", "precio": 1100, "icono_menu": "imgs/pepsi.png"},
    {"nombre": "Completos", "precio": 1800, "icono_menu": "imgs/completos.png"},
    {"nombre": "Papas", "precio": 500, "icono_menu": "imgs/papas.png"},
]

# Crear un diccionario para almacenar las imágenes
imagenes_menus = []

for item in menu:
    imagen = Image.open(item["icono_menu"])
    icono_menu = ctk.CTkImage(dark_image=imagen, size=(64, 64))
    item_copy = item.copy()
    item_copy["icono_menu"] = icono_menu
    boton_tarjeta = ctk.CTkButton(tarjetas_frame, image=icono_menu, text=item["nombre"], 
                                  compound="top", 
                                  command=lambda nombre=item["nombre"], precio=item["precio"]: 
                                  agregar_al_pedido(nombre, precio, pedido_treeview, label_total))
    boton_tarjeta.pack(side="left", padx=10, pady=10)


# etiqueta para mostrar el precio total
label_total = ctk.CTkLabel(pestañaPedidos, text="Total: $0.00", font=("Helvetica", 16, "bold"))
label_total.grid(row=2, column=0, padx=10, pady=10, sticky="e")

# botongenerar boleta
botonGenerarBoleta = ctk.CTkButton(pestañaPedidos, text="Generar Boleta", command=lambda: generarBoleta())
botonGenerarBoleta.grid(row=3, column=0, padx=10, pady=10, sticky="e")

#----------------------------------------------------------------------------------------------------------------------#

app.mainloop()
