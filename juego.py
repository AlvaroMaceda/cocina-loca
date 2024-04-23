import pygame

# Inicialización de Pygame
pygame.init()

# Inicialización de la superficie de dibujo
ventana = pygame.display.set_mode((1500,675))
pygame.display.set_caption("Ejemplo 1")

fondo = pygame.image.load("pantallazo-1.png").convert_alpha()
fondo = pygame.transform.scale(fondo, (1500, 675))

patata = pygame.image.load("patata.png").convert_alpha()
patata = pygame.transform.scale(patata, (325, 400))

ventana.fill((255, 255, 255))
ventana.blit(patata, (0, 0))
ventana.blit(fondo, (0, 0))

# Bucle principal del juego
jugando = True
while jugando:
    # Comprobamos los eventos
    #Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Se pinta la ventana con un color

    # Esto borra los posibles elementos que teníamos anteriormente
    # ventana.fill((255, 255, 255))

    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()

    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()
