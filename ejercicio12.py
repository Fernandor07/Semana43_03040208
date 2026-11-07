print("Ejercicio 12: Alta de productos con folio")
print("Nombre: Escribe aquí tu nombre completo")
print("Matrícula: Escribe aquí tu matrícula")
print()

# ¿Cuántos productos vamos a dar de alta?
cuantos = int(input("¿Cuántos productos vas a dar de alta? "))

# Aquí sumaremos el valor de todo el inventario
valor_total = 0

# "Para cada" número del 1 al total de productos...
for numero in range(1, cuantos + 1):
    # Creamos el folio: str() convierte el número en texto para poder juntarlo
    folio = "SNK" + str(numero)

    print()
    print("📝 Producto con folio", folio)
    nombre = input("Nombre: ")

    # Pedimos el precio y lo validamos: mientras sea 0 o menos, se repite
    precio = int(input("Precio: $"))
    while precio <= 0:
        print("❌ El precio debe ser mayor que 0")
        precio = int(input("Precio: $"))

    piezas = int(input("Piezas en bodega: "))

    # Calculamos cuánto vale este producto en bodega
    valor = precio * piezas
    valor_total = valor_total + valor

    # Mostramos la ficha
    print("✅ Alta exitosa")
    print("   Folio:", folio, "· Nombre:", nombre)
    print("   Precio: $", precio, "· Piezas:", piezas, "· Valor: $", valor)

# Ya terminamos todas las altas
print()
print("===== RESUMEN DEL INVENTARIO =====")
print("Productos dados de alta:", cuantos)
print("💰 Valor total del inventario: $", valor_total)
