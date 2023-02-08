import pygame
# Inicializar a pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Tiulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load("transbordador-espacial.png")
jugador_x = 368
jugador_y = 536
jugador_x_camnbio = 0


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((205, 144, 228))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_camnbio = -20
            if evento.key == pygame.K_RIGHT:
                jugador_x_camnbio = 20
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_camnbio = 0
        jugador_x += jugador_x_camnbio
    jugador(jugador_x, jugador_y)

    pygame.display.update()
