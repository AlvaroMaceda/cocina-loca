import pygame

patata = pygame.image.load("imagenes/patata.png").convert_alpha()
patata = pygame.transform.scale(patata, (325, 400))

class Patata(pygame.sprite.Sprite):
  def __init__(self):
