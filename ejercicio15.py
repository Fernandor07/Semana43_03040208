print("Ejercicio 15: Bajas en el inventario")
print("Nombre: Fernando Raúl de la Fuente Gomez")
print("Matrícula: Al03040208")

# El inventario inicial
inventario = ["Air Max", "Jordan 1", "Converse", "Samba", "New Balance 550"]

while True:
    # Mostramos el inventario numerado
    print()
    print("===== INVENTARIO =====")
    for i in range(len(inventario)):
        print(i + 1, ".", inventario[i])

    numero = int(input("Número del producto a eliminar (0 para terminar): "))

    # ¿Escribió 0?
    if numero == 0:
        break
    # ¿El número es menor que 1?
    elif numero < 0:
        print("❌ Ese número no existe")
    # ¿El número es mayor que la cantidad de productos?
    elif numero > len(inventario):
        print("❌ Ese número no existe")
    else:
        # El número sí existe. Recuerda: casillero = número - 1
        elegido = inventario[numero - 1]
        confirmar = input("¿Seguro que quieres eliminar " + elegido + "? (s/n): ")

        if confirmar == "s":
            # Borramos lo que hay en ese casillero
            del inventario[numero - 1]
            print("🗑️", elegido, "fue eliminado")
        else:
            print("👍 Baja cancelada")

    # ¿El inventario quedó vacío?
    if len(inventario) == 0:
        print("📭 El inventario quedó vacío")
        break

# Ya salimos del while
print()
print("Quedaron", len(inventario), "productos en el inventario")
