print("Ejercicio 4: La caja registradora de la cafetería")
print("Nombre: Escribe aquí tu nombre completo")
print("Matrícula: Escribe aquí tu matrícula")
print()

# Empezamos con el total y los productos en 0
total = 0
productos = 0

# Al inicio todavía NO terminamos de registrar
termine = False

# Mientras NO hayamos terminado, se repite
while termine == False:
    print("===== Nuevo producto =====")
    nombre = input("Producto (escribe fin para cobrar): ")

    # ¿Escribió "fin"?
    if nombre == "fin":
        termine = True
    else:
        # Pedimos el precio y la cantidad (los convertimos a número)
        precio = int(input("Precio de " + nombre + ": $"))
        cantidad = int(input("¿Cuántos quiere? "))

        # Calculamos el subtotal de este producto
        subtotal = precio * cantidad

        # Lo sumamos al total y contamos los productos
        total = total + subtotal
        productos = productos + cantidad

        print("🧾", cantidad, nombre, "= $", subtotal)
        print("💰 Llevas $", total)

# Ya fuera del while: mostramos el ticket
print()
print("========== TICKET ==========")
print("Productos:", productos)
print("Total: $", total)

# ¿El total es de 200 o más?
if total >= 200:
    total = total - 20
    print("🎉 Descuento de $20 aplicado")
    print("Total con descuento: $", total)

# Pedimos con cuánto paga
pago = int(input("¿Con cuánto pagas? $"))

# Mientras el pago sea MENOR que el total, no alcanza
while pago < total:
    print("❌ No alcanza. Faltan $", total - pago)
    pago = int(input("¿Con cuánto pagas? $"))

# Ya alcanzó: calculamos el cambio
cambio = pago - total
print("✅ Pago recibido. Tu cambio es: $", cambio)
print("☕ ¡Gracias por tu compra!")
