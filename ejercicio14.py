print("Ejercicio 14: Altas en el inventario")
print("Nombre: Fernando Raúl de la Fuente Gomez")
print("Matrícula: Al03040208")
print()

# Empezamos con el inventario vacío
inventario = []

# Al inicio todavía NO terminamos
termine = False

while termine == False:
    nuevo = input("Producto a agregar (escribe fin para terminar): ")

    # ¿Escribió "fin"?
    if nuevo == "fin":
        termine = True
    # ¿Lo dejó vacío?
    elif nuevo == "":
        print("❌ El producto no puede estar vacío")
    # ¿Ya ESTÁ en el inventario?
    elif nuevo in inventario:
        print("⚠️", nuevo, "ya está en el inventario")
    else:
        # Todo bien: lo agregamos al final de la lista
        inventario.append(nuevo)
        print("✅ Agregado. Llevas", len(inventario), "productos")

# Mostramos el inventario
print()
print("===== INVENTARIO =====")

# ¿La lista quedó vacía?
if len(inventario) == 0:
    print("📭 No agregaste productos")
else:
    for i in range(len(inventario)):
        print(i + 1, ".", inventario[i])
