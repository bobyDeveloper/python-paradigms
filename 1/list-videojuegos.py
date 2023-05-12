import random

# Lista de juegos de aventuras
aventuras = ["The Legend of Zelda: Breath of the Wild", "Uncharted 4: A Thief's End", "Assassin's Creed Valhalla", "Horizon Zero Dawn"]

# Lista de juegos de acción
accion = ["Grand Theft Auto V", "Call of Duty: Warzone", "DOOM Eternal", "Mortal Kombat 11"]

# Lista de juegos de deportes
deportes = ["FIFA 21", "NBA 2K21", "Madden NFL 21", "MLB The Show 21"]

# Imprimir un juego aleatorio de cada lista
print("Juego de aventuras: ", random.choice(aventuras))
print("Juego de acción: ", random.choice(accion))
print("Juego de deportes: ", random.choice(deportes))

