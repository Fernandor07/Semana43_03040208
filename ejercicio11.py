print("Ejercicio 11: Buscador de la tienda de sneakers")
print("Nombre: Escribe aquí tu nombre completo")
print("Matrícula: Escribe aquí tu matrícula")
print()

# El inventario de la tienda
inventario = ["Air Max", "Jordan 1", "Converse", "Samba", "New Balance 550"]

# Contadores
busquedas = 0
encontrados = 0

# El buscador se repite hasta que el cliente escriba "salir"
while True:
    print()
    buscado = input("🔍 ¿Qué modelo buscas? (escribe salir para terminar): ")

    # ¿Escribió "salir"?
    if buscado == "salir":
        break

    # Contamos esta búsqueda
    busquedas = busquedas + 1

    # "Para cada" modelo del inventario...
    for modelo in inventario:
        # ¿Este modelo es IGUAL al que busca?
        if modelo == buscado:
            print("✅ ¡Sí tenemos", modelo, "!")
            encontrados = encontrados + 1
            # Ya lo encontramos: dejamos de buscar
            break
    else:
        # Solo entra aquí si el for terminó SIN break (no lo encontró)
        print("❌ No tenemos", buscado)
        print("👟 Te recomendamos estos modelos:")
        for modelo in inventario:
            print("   •", modelo)

# Ya salió del buscador: mostramos el resumen
print()
print("===== RESUMEN =====")
print("Búsquedas:", busquedas)
print("Encontrados:", encontrados)
print("👋 ¡Gracias por visitar la tienda!")
