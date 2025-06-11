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
fondo = pygame.image.load('fondo.jpg')

# Variables delJugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Variables del Enemigo
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0,736)
enemigo_y = random.randint(50,200)
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50

# Variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.8
bala_visible = False


# Funcion Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion Enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# Funcion Disparar Bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x  + 16, y + 10))


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
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                disparar_bala(jugador_x,bala_y)

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Imagen de fondo
    pantalla.blit(fondo,(0,0))

    #Modificar la ubicacion del jugador
    jugador_x += jugador_x_cambio

    #mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x=0
    elif jugador_x >= (800-64):
        jugador_x = 800-64

    # movimiento bala
    if bala_visible:
        disparar_bala(jugador_x, bala_y)
        bala_y -= bala_y_cambio


    #Modificar la ubicacion del enemigo
    enemigo_x += enemigo_x_cambio

    #mantener dentro de bordes al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio=0.3
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= (800-64):
        enemigo_x_cambio = -0.3
        enemigo_y += enemigo_y_cambio


    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # Actualizar
    pygame.display.update()

# Nota: Al salir del bucle, pygame.quit() sería recomendable llamarlo
# para desinicializar correctamente los módulos de pygame