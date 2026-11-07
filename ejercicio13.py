print("Ejercicio 13: Mis juegos favoritos")
print("Nombre: Fernando Raúl de la Fuente Gomez")
print("Matrícula: Al03040208")
print()

# Creamos la lista con 5 juegos
juegos = ["Minecraft", "Roblox", "Fortnite", "FIFA", "Among Us"]

# Casillero 0: el primero
print("🥇 Mi juego número 1:", juegos[0])

# Casillero -1: el último
print("🔚 El último de mi lista:", juegos[-1])

# Casillero 2: el tercero (porque empezamos en 0)
print("3️⃣ El tercero:", juegos[2])

# len() cuenta cuántos hay
print("📦 Tengo", len(juegos), "juegos favoritos")

# Mostramos la lista numerada
print()
print("===== MIS FAVORITOS =====")
# range(len(juegos)) nos da los casilleros: 0, 1, 2, 3, 4
for i in range(len(juegos)):
    # Mostramos i + 1 para que la persona vea del 1 al 5
    print(i + 1, ".", juegos[i])

# Pedimos un número del 1 al 5
numero = int(input("Escribe un número del 1 al 5: "))

# La persona cuenta desde 1, pero Python desde 0: por eso le restamos 1
print("🎮 Elegiste:", juegos[numero - 1])
