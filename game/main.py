import random

def eleccion_computadora():
    """Obtiene una opción aleatoria para que la computadora la utilice."""
    opciones = ["piedra", "papel", "tijera"]  
    return random.choice(opciones)

def eleccion_usuario():
    """Obtiene la opción que el jugador utilizará."""
    opciones = ["piedra", "papel", "tijera"]  
    while True:
        usuario = input("Selecciona lo que quieres jugar esta ronda: Piedra, papel o tijera.\n").lower()
        if usuario in opciones:
            return usuario
        else:
            print("¡Opción inválida! Por favor, selecciona piedra, papel o tijera.")

def determinar_ganador(usuario, computadora):
    """Determina el ganador de la ronda."""
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "Usuario"
    else:
        return "Computadora"

def ejecutar_juego():
    """Inicia y maneja el juego de principio a fin."""
    rondas = 3
    usuario_gana = 0
    computadora_gana = 0

    print("*" * 15)
    print("El juego comenzará ahora.")
    print("*" * 15)

    while rondas > 0:
        computadora = eleccion_computadora()
        usuario = eleccion_usuario()
        resultado = determinar_ganador(usuario, computadora)
        print(f"{usuario} vs {computadora}, ")

        if resultado == "Empate":
            print("¡Empate en esta ronda!")
        elif resultado == "Usuario":
            usuario_gana += 1
            print("¡Ganaste esta ronda!")
        else:
            computadora_gana += 1
            print("¡La computadora ganó esta ronda!")

        rondas -= 1

    if usuario_gana == computadora_gana:
        print("¡Es un empate!")
    elif usuario_gana > computadora_gana:
        print(f"¡Ganaste! {usuario_gana} ronda(s) contra {computadora_gana} de la computadora.")
    else:
        print(f"La computadora ganó. {computadora_gana} ronda(s) contra {usuario_gana} tuyas.")

    continuar = input("¿Quieres jugar de nuevo? (s/n): ")
    if continuar.lower() == "s":
        ejecutar_juego()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

ejecutar_juego()
