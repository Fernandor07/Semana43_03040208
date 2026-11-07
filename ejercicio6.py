print("Ejercicio 6: Validar los datos de una alta")
print("Nombre: Escribe aquí tu nombre completo")
print("Matrícula: Escribe aquí tu matrícula")
print()

# 1. Nombre: mientras esté vacío, lo volvemos a pedir
nombre = input("Nombre del producto: ")
while nombre == "":
    print("❌ El nombre no puede estar vacío")
    nombre = input("Nombre del producto: ")

# 2. Precio: mientras sea 0 o menos, lo volvemos a pedir
precio = int(input("Precio: $"))
while precio <= 0:
    print("❌ El precio debe ser mayor que 0")
    precio = int(input("Precio: $"))

# 3. Piezas: mientras sean menos de 0, las volvemos a pedir
piezas = int(input("Piezas en bodega: "))
while piezas < 0:
    print("❌ Las piezas no pueden ser negativas")
    piezas = int(input("Piezas en bodega: "))

# 4. Categoría: al inicio todavía NO es válida
categoria = ""
categoria_valida = False

while categoria_valida == False:
    print("Categorías: 1. Tenis  2. Ropa  3. Accesorios")
    opcion = input("Elige la categoría: ")

    if opcion == "1":
        categoria = "Tenis"
        categoria_valida = True
    elif opcion == "2":
        categoria = "Ropa"
        categoria_valida = True
    elif opcion == "3":
        categoria = "Accesorios"
        categoria_valida = True
    else:
        print("❌ Esa categoría no existe")

# 5. Mostramos la ficha
print()
print("===== FICHA DEL PRODUCTO =====")
print("Nombre:", nombre)
print("Precio: $", precio)
print("Piezas:", piezas)
print("Categoría:", categoria)

# 6. Confirmación: al inicio la respuesta todavía NO es válida
respuesta_valida = False

while respuesta_valida == False:
    guardar = input("¿Guardar? (s/n): ")

    if guardar == "s":
        print("✅ Producto guardado")
        respuesta_valida = True
    elif guardar == "n":
        print("🚫 Alta cancelada")
        respuesta_valida = True
    else:
        print("❌ Escribe solo s o n")
