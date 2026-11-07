print("Ejercicio 10: Tu playlist en el camión")
print("Nombre: Escribe aquí tu nombre completo")
print("Matrícula: Escribe aquí tu matrícula")
print()

# Nuestra playlist
playlist = ["Flowers", "Calm Down", "Ella Baila Sola", "Anti-Hero", "Tití Me Preguntó", "Daylight"]

# Mostramos la playlist numerada
print("===== 🎧 MI PLAYLIST =====")
numero = 1
for cancion in playlist:
    print(numero, ".", cancion)
    numero = numero + 1

# Preguntamos qué saltar y dónde bajarse (escríbelas igual que en la lista)
saltar = input("¿Qué canción quieres saltar? ")
parada = input("¿En qué canción llegas a tu parada? ")

# Contador de canciones escuchadas
escuchadas = 0

# "Para cada" canción de la playlist...
for cancion in playlist:
    # ¿Es la canción que queremos saltar?
    if cancion == saltar:
        print("⏭️ Saltando", cancion)
        # continue: pasa a la siguiente canción sin escuchar esta
        continue

    # Si no la saltamos, la escuchamos
    print("🎵 Escuchando", cancion)
    escuchadas = escuchadas + 1

    # ¿Es la canción en la que llegamos a la parada?
    if cancion == parada:
        print("🚏 ¡Llegaste a tu parada!")
        # break: dejamos de escuchar
        break
else:
    # Solo entra aquí si el for terminó SIN break
    print("🎧 Escuchaste toda la playlist")

print("Canciones escuchadas:", escuchadas)
