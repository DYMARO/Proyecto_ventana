import pygame
import sys

ancho= 300
alto= 500
pygame.init()
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("proyecto")
while True:
    ventana.fill([10,150,20])

    for evento in pygame.event.get():
        print (evento)
        if evento.type==pygame.QUIT:
            sys.exit()


    pygame.display.update()