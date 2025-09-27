import random


class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre


class Pokemon:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.vida_max = random.randint(150, 400)
        self.vida_actual = self.vida_max

    def recuperar(self):
        self.vida_actual = self.vida_max




entrenador1 = None
pokemon1 = None
entrenador2 = None
pokemon2 = None

ganadas = 0
perdidas = 0



def crearEntrenadorPokemon(num: int):
    global entrenador1, entrenador2, pokemon1, pokemon2
    nombre_entrenador = input(f"Nombre del entrenador {num}: ")
    nombre_pokemon = input(f"Nombre del Pokémon de {nombre_entrenador}: ")

    if num == 1:
        entrenador1 = Entrenador(nombre_entrenador)
        pokemon1 = Pokemon(nombre_pokemon)
        print("\n=== Tu Pokémon ha sido creado ===")
        print(f"Entrenador: {entrenador1.nombre}")
        print(f"Pokémon: {pokemon1.nombre}")
        print(f"Ataque máximo: {pokemon1.max_ataque}")
        print(f"Vida máxima: {pokemon1.vida_max}\n")
    else:
        entrenador2 = Entrenador(nombre_entrenador)
        pokemon2 = Pokemon(nombre_pokemon)
        print("\n=== Rival creado ===")
        print(f"Entrenador: {entrenador2.nombre}")
        print(f"Pokémon: {pokemon2.nombre}")
        print(f"Ataque máximo: {pokemon2.max_ataque}")
        print(f"Vida máxima: {pokemon2.vida_max}\n")


def valorDeAtaque(num: int) -> int:
    if num == 1:
        return random.randint(0, pokemon1.max_ataque)
    else:
        return random.randint(0, pokemon2.max_ataque)


def defender(num: int, ataque: int) -> int:
    # Dado de 1 a 6: si sale 6, el ataque se esquiva
    dado = random.randint(1, 6)
    if dado == 6:
        print("El pokemon esquivo el ataque")
        ataque = 0

    if num == 1:
        pokemon1.vida_actual -= ataque
        return pokemon1.vida_actual
    else:
        pokemon2.vida_actual -= ataque
        return pokemon2.vida_actual




print("=== Bienvenido a PhytonMon ===")
crearEntrenadorPokemon(1)  

while True:
    opcion = input("\n¿Desea Pelear (P) o Finalizar (F)? ").upper()

    if opcion == "F":
        print("\n=== Fin del juego ===")
        print(f"Entrenador: {entrenador1.nombre}")
        print(f"Pokémon: {pokemon1.nombre}")
        print(f"Ataque máximo: {pokemon1.max_ataque}")
        print(f"Vida máxima: {pokemon1.vida_max}")
        print(f"Encuentros ganados: {ganadas}")
        print(f"Encuentros perdidos: {perdidas}")
        break

    elif opcion == "P":
       
        pokemon1.recuperar()

       
        crearEntrenadorPokemon(2)
        pokemon2.recuperar()

        print("\n=== Inicia el combate ===")
        turno = 1  

        while pokemon1.vida_actual > 0 and pokemon2.vida_actual > 0:
            if turno == 1:
                ataque = valorDeAtaque(1)
                defender(2, ataque)
                print(f"\n{pokemon1.nombre} ataca con {ataque}")
                print(f"{pokemon2.nombre} tiene ahora {max(0, pokemon2.vida_actual)} de vida")
                turno = 2
            else:
                ataque = valorDeAtaque(2)
                defender(1, ataque)
                print(f"\n{pokemon2.nombre} ataca con {ataque}")
                print(f"{pokemon1.nombre} tiene ahora {max(0, pokemon1.vida_actual)} de vida")
                turno = 1

        if pokemon1.vida_actual > 0:
            print(f"\n {entrenador1.nombre} y su Pokémon {pokemon1.nombre} ganan, Sumas 1 punto a tu marcador total")
            ganadas += 1
        else:
            print(f"\n {entrenador2.nombre} y su Pokémon {pokemon2.nombre} ganan, Sumas 1 derrota a tu registro")
            perdidas += 1

    else:
        print("Opción inválida. Intenta de nuevo.")
