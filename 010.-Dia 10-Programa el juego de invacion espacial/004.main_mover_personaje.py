import pygame


#inicializando pygame
pygame.init()

#Estableciendo el tamaño de la pantalla y mostrarla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasión Espacial")

icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 536

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


#Programando loop para que la pantalla no desaparezca
se_ejecuta = True

# Bucle principal del juego (game loop)
# Este bucle se ejecuta continuamente hasta que se cierra el juego
while se_ejecuta:

    jugador_x += 0.1
    # Obtener todos los eventos de pygame desde la última iteración
    # pygame.event.get() devuelve una lista de eventos ocurridos
    for evento in pygame.event.get():

        # Verificar si el evento actual es de tipo QUIT
        # QUIT ocurre cuando se hace click en el botón cerrar de la ventana
        if evento.type == pygame.QUIT:
            # Cambiar la variable a False para salir del bucle
            se_ejecuta = False

    # RGB
    pantalla.fill((205,144,228))
    #invocando funcion que añade al jugador
    jugador(jugador_x,jugador_y)
    pygame.display.update()
# Nota: Al salir del bucle, pygame.quit() sería recomendable llamarlo
# para desinicializar correctamente los módulos de pygame