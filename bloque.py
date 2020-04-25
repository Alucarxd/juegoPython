import pygame
import sys
import random

#CONSTANTES
ANCHO = 800
ALTO = 600
color_negro = (0,0,0)

s = 50

# ENEMIGO 
enemigo = pygame.image.load("img/hehe.png")
enemigo = pygame.transform.scale(enemigo, (s,s))


# JUGADOR
jugador_pos = [ ANCHO/ 2, ALTO - s * 2]

# ENEMIGOS
eSize = 50
enemigo_pos = [random.randint(0, ANCHO- eSize),0]


# VENTANA
ventana = pygame.display.set_mode((ANCHO,ALTO))


game_over = False
clock = pygame.time.Clock()

# FUNCIONES 
def dectectar_colision(jugador_pos,enemigo_pos):
    jx = jugador_pos[0]
    jy = jugador_pos[1]
    ex = enemigo_pos[0]
    ey = enemigo_pos[1]

    if (ex >= jx and ex <(jx + s)) or (jx >= ex and jx < (ex + eSize)):
        if (ey >= jy and ey <(jy + s)) or (jx >= ey and jx < (ey + eSize)):
            return True
    return False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            x = jugador_pos[0]
            if event.key == pygame.K_LEFT:
                x -= s
            if event.key == pygame.K_RIGHT:
                x += s

            jugador_pos[0] = x

    ventana.fill(color_negro)

    if enemigo_pos[1] >= 0 and enemigo_pos[1] < ALTO:
        enemigo_pos[1] += 20
    else:
        enemigo_pos[0] = random.randint(0, ANCHO - eSize)
        enemigo_pos[1] = 0

    # COLISIONES
    if dectectar_colision(jugador_pos,enemigo_pos):
        game_over = True


    # ENEMIGO 
    ventana.blit(enemigo,(enemigo_pos[0],enemigo_pos[1],eSize,eSize))

    # JUGADOR 
    imagen = pygame.image.load("img/comecome.png")
    ventana.blit(imagen,(jugador_pos[0],jugador_pos[1],s,s))

    clock.tick(20)
    pygame.display.update()