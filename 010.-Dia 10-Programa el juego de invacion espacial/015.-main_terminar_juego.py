import pygame
import random
import math
from pygame import mixer


#inicializando pygame
pygame.init()

#Estableciendo el tamaño de la pantalla y mostrarla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.02)
mixer.music.play(-1)

# Variables delJugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Variables del Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5 

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# Variables de la bala

img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.8
bala_visible = False

#Puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf',32)
texto_x = 10
texto_y = 10

# texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf',40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (200, 250))

#funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255,255,255))
    pantalla.blit(texto, (x,y))

# Funcion Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion Enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Funcion Disparar Bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x  + 16, y + 10))

# Funcion Detectar Colisiones
def hay_colision(x_1, y_1, x_2, y_2):

    operacion_1 = x_1-x_2
    operacion_2 = y_1-y_2

    distancia = math.sqrt(math.pow(operacion_1,2) + math.pow(operacion_2,2))

    if distancia < 27:
        return True
    else:
        return False


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
                jugador_x_cambio = -0.4
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.4
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.set_volume(0.1)
                sonido_bala.play()

                if bala_visible == False:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)

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




    #Modificar la ubicacion del enemigo
    for e in range (cantidad_enemigos):

        #fin del juego
        if enemigo_y[e] > 400 and enemigo_y[e] <2000:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        #mantener dentro de bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e]=0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= (800-64):
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('golpe.mp3')
            sonido_colision.set_volume(0.1)
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1

            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(2200  , 2500)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio



    jugador(jugador_x,jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar
    pygame.display.update()

# Nota: Al salir del bucle, pygame.quit() sería recomendable llamarlo
# para desinicializar correctamente los módulos de pygame