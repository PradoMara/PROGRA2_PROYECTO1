import customtkinter as ctk
from tkinter import ttk 
from PIL import Image
from clases.agregarPedido import *
from clases.clickTarjeta import tarjetaClick
from clases.ingresarIngredientes import IngresarIngrediente
from clases.eliminarIngrediente import EliminarIngrediente
from clases.generarMenu import GenerarMenu
from clases.crearTarjeta import crear_tarjeta
from clases.generarBoleta import generarBoleta
from clases.eliminarMenu import eliminarMenu
from clases.verificarStock import VerificarStock
from clases.validacion    import Validacion

#-----------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------- Instancia de la aplicación -----------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------#

menu = [
    {"nombre": "Hamburguesa", "precio": 3500, "icono_menu": "imgs/hamburguesa.png"},
    {"nombre": "Pepsi", "precio": 1100, "icono_menu": "imgs/pepsi.png"},
    {"nombre": "Completos", "precio": 1800, "icono_menu": "imgs/completos.png"},
    {"nombre": "Papas fritas", "precio": 500, "icono_menu": "imgs/papas.png"},
]

ingredientes_stock = []
# Configuración de la apariencia y tema
ctk.set_appearance_mode("dark")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

ingresoIng  = IngresarIngrediente(ingredientes_stock)
verificador = VerificarStock(ingredientes_stock)


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
ingredienteDisp = ["Papas" , "Bebida"  , "Vienesas" , "Pan de Completo", "Tomate", "Palta", "Pan de Hamburguesa", "Lamina de Queso", "Churrasco de Carne"]

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
botonIngresarr = ctk.CTkButton(pestañaIngredientes, text="Ingresar Ingrediente", command=lambda:ingresoIng.ingresarIngrediente(entradaCantidad, entradaNombre, tablaAgregados))   
botonIngresarr.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Configura el Treeview en lugar del CTkTextbox
tablaAgregados = ttk.Treeview(pestañaIngredientes, columns=("Nombre", "Cantidad"), show="headings")
tablaAgregados.heading("Nombre", text="Nombre del Ingrediente")
tablaAgregados.heading("Cantidad", text="Cantidad")
tablaAgregados.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

# botón eliminar ingredientes
Eliminar = EliminarIngrediente(tablaAgregados)
botonEliminar = ctk.CTkButton(pestañaIngredientes, text="Eliminar Ingrediente", command=lambda: (Eliminar.seleccionar_fila(), Eliminar.eliminar_dato()))
botonEliminar.grid(row=3, column=2, padx=10, pady=10)

#----------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------PESTAÑA PEDIDOS-------------------------------------------------------#

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

# Crear una lista  para almacenar las imágenes
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

# Definir los menús y sus ingredientes requeridos
menus = {
    "Papas fritas": {"Papas": 5},
    "Pepsi": {"Bebida": 1},
    "Completo": {
        "Vienesas": 1,
        "Pan de Completo": 1,
        "Tomate": 1,
        "Palta": 1,
    },
    "Hamburguesa": {
        "Pan de Hamburguesa": 1,
        "Lamina de Queso": 1,
        "Churrasco de Carne": 1,
    }
}


# etiqueta para mostrar el precio total
label_total = ctk.CTkLabel(pestañaPedidos, text="Total: $0.00", font=("Helvetica", 16, "bold"))
label_total.grid(row=2, column=0, padx=10, pady=10, sticky="e")

# Función que se ejecuta cuando se presiona "Generar Menú"

generador = None
def generar_menu():
    global ingredientes_stock
    ingredientes_stock = ingresoIng.obtenerIngredientesStock()
    verificador = VerificarStock(ingredientes_stock)

    generador = GenerarMenu(pedido_treeview, label_total, ingredientes_stock)
    generador.generar(menus, verificador)
    print("Ingredientes Stock:", ingredientes_stock)
    

# Botón para generar menú
botonGenerarMenu = ctk.CTkButton(pestañaIngredientes, text="Generar Menú", command=generar_menu)
botonGenerarMenu.grid(pady=10)

#Boton para eliminaar algo del menu
EliminarMenu = eliminarMenu(pedido_treeview, label_total, generador)
botonEliminarMenu = ctk.CTkButton(pestañaPedidos, text="Eliminar Menu", command=lambda: (EliminarMenu.seleccionar_fila(), EliminarMenu.eliminar_menu()))
botonEliminarMenu.grid(row=3, column=0, padx=180, pady=10, sticky="e")

# botongenerar boleta
Boleta = generarBoleta(pedido_treeview)
botonGenerarBoleta = ctk.CTkButton(pestañaPedidos, text="Generar Boleta", command=Boleta.generar_boleta_evento)
botonGenerarBoleta.grid(row=3, column=0, padx=10, pady=10, sticky="e")

#----------------------------------------------------------------------------------------------------------------------#

app.mainloop()
