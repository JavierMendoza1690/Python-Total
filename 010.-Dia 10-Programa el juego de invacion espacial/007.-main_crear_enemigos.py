import pygame
import random


#inicializando pygame
pygame.init()

#Estableciendo el tamaño de la pantalla y mostrarla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasión Espacial")

icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Variables delJugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0

# Variables del Enemigo
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0,736)
enemigo_y = random.randint(50,200)
enemigo_x_cambio = 0


# Funcion Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion Enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


#Programando loop para que la pantalla no desaparezca
se_ejecuta = True


# Bucle principal del juego (game loop)
# Este bucle se ejecuta continuamente hasta que se cierra el juego
while se_ejecuta:


    # Obtener todos los eventos de pygame desde la última iteración
    # pygame.event.get() devuelve una lista de eventos ocurridos
    for evento in pygame.event.get():

        # Verificar si el evento actual es de tipo QUIT
        # QUIT ocurre cuando se hace click en el botón cerrar de la ventana
        if evento.type == pygame.QUIT:
            # Cambiar la variable a False para salir del bucle
            se_ejecuta = False


        # Evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.1

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # RGB
    pantalla.fill((205,144,228))

    #Modificar la ubicacion del jugador
    jugador_x += jugador_x_cambio

    #mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x=0
    elif jugador_x >= (800-64):
        jugador_x = 800-64

    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # Actualizar
    pygame.display.update()

# Nota: Al salir del bucle, pygame.quit() sería recomendable llamarlo
# para desinicializar correctamente los módulos de pygame