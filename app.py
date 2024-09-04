import customtkinter as ctk
from clases.ingresarIngredientes import ingresarIngrediente
from clases.eliminarIngrediente import eliminarIngrediente
from clases.generarMenu import generarMenu


app = ctk.CTk()
app.title("Gestión de ingredientes y pedidos")
app.geometry("800x600")


frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

pestañas = ctk.CTkTabview(frame)
pestañas.pack(fill="both", expand=True)

pestañaIngredientes = pestañas.add("Ingreso de Ingredientes")
pestañaPedidos = pestañas.add("Pedidos")

#label ingrediente
etiquetaNombre = ctk.CTkLabel(pestañaIngredientes, text="Nombre del Ingrediente:")
etiquetaNombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#entrada ingrediente
entradaNombre = ctk.CTkEntry(pestañaIngredientes)
entradaNombre.grid(row=0, column=1, padx=10, pady=10)
#label ingrediente
etiquetaCantidad = ctk.CTkLabel(pestañaIngredientes, text="Cantidad:")
etiquetaCantidad.grid(row=1, column=0, padx=10, pady=10, sticky="w")
#entrada cantidad
entradaCantidad = ctk.CTkEntry(pestañaIngredientes)
entradaCantidad.grid(row=1, column=1, padx=10, pady=10)
#boton ingresar
botonIngresarr = ctk.CTkButton(pestañaIngredientes, text="Ingresar Ingrediente", command=lambda: ingresarIngrediente())
botonIngresarr.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# tabla de ingredientes agregados
tablaAgregados= ctk.CTkTextbox(pestañaIngredientes, width=400, height=200)
tablaAgregados.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

# boton eliminar ingredientes
botonEliminar = ctk.CTkButton(pestañaIngredientes, text="Eliminar Ingrediente", command=lambda: eliminarIngrediente())
botonEliminar.grid(row=3, column=2, padx=10, pady=10)

# boton generar menu
botonGenerarMenu = ctk.CTkButton(frame, text="Generar Menú", width=300, command=lambda: generarMenu())
botonGenerarMenu.pack(pady=10)




app.mainloop()
