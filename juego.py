import pygame
import os

POSICION_VENTANA = (250,200)
TAMAÑO_VENTANA = (1500, 675)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % POSICION_VENTANA


# Inicialización de Pygame
pygame.init()

# Inicialización de la superficie de dibujo
ventana = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("Ejemplo 1")

capa_fondo=pygame.Surface(TAMAÑO_VENTANA, pygame.SRCALPHA)
capa_clientes=pygame.Surface(TAMAÑO_VENTANA, pygame.SRCALPHA)
capa_cocina=pygame.Surface(TAMAÑO_VENTANA, pygame.SRCALPHA)
capa_ingredientes=pygame.Surface(TAMAÑO_VENTANA, pygame.SRCALPHA)

fondo = pygame.image.load("fondo.png").convert_alpha()
fondo = pygame.transform.scale(fondo, TAMAÑO_VENTANA)
capa_fondo.blit(fondo, (0,0))

cocina = pygame.image.load("cocina.png").convert_alpha()
cocina = pygame.transform.scale(cocina, TAMAÑO_VENTANA)
capa_cocina.blit(cocina, (0, 0))

patata = pygame.image.load("patata.png").convert_alpha()
patata = pygame.transform.scale(patata, (325, 400))

# Bucle principal del juego
jugando = True

x_patata=0

while jugando:
    # Comprobamos los eventos
    #Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False


    capa_clientes.fill((0,0,0,0))
    capa_clientes.blit(patata, (x_patata,0))
    x_patata=x_patata+10

    # Pintar las capas
    ventana.blit(capa_fondo, (0, 0))
    ventana.blit(capa_clientes, (0, 0))
    ventana.blit(capa_cocina, (0, 0))
    ventana.blit(capa_ingredientes, (0, 0))

    pygame.display.flip()

    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(30)

pygame.quit()
