print("Ejercicio 7: Boletos para el concierto")
print("Nombre: Escribe aquí tu nombre completo")
print("Matrícula: Escribe aquí tu matrícula")
print()

# Pedimos el artista y cuántos boletos quiere
artista = input("¿De quién es el concierto? ")
cantidad = int(input("¿Cuántos boletos quieres? "))

# range(1, cantidad + 1): de 1 hasta cantidad
# (le sumamos 1 porque range se detiene ANTES del último número)
for boleto in range(1, cantidad + 1):
    # Pedimos el nombre de quien va a usar este boleto
    asistente = input("Nombre del asistente " + str(boleto) + ": ")

    # Mostramos el boleto
    print("🎟️ Boleto", boleto, "de", cantidad)
    print("   🎤", artista, "· Asistente:", asistente)

# Esto se ejecuta cuando el for ya dio todas sus vueltas
print("✅ Se generaron", cantidad, "boletos. ¡Disfruten el concierto!")
