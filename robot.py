import pygame

# Define los colores que se van a usar
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Inicia Pygame
pygame.init()

# Configura la pantalla
TAMANO_PANTALLA = [700, 500]
pantalla = pygame.display.set_mode(TAMANO_PANTALLA)
pygame.display.set_caption("Robot animado")

# Define las variables de posición del robot
pos_x = 50
pos_y = 50

# Define las variables de movimiento del robot
vel_x = 5
vel_y = 5

# Define las dimensiones del robot
ancho_robot = 50
alto_robot = 50

# Define la velocidad de la animación
velocidad_animacion = 10

# Define las imágenes del robot
imagen1 = pygame.image.load("robot1.png") 
imagen2 = pygame.image.load("robot1.png")
imagen3 = pygame.image.load("robot1.png")

# Define el reloj
reloj = pygame.time.Clock()

# Loop principal del juego
juego_terminado = False
while not juego_terminado:
    # Maneja los eventos del juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True

    # Actualiza la posición del robot
    pos_x += vel_x
    pos_y += vel_y

    # Revisa si el robot ha alcanzado los límites de la pantalla
    if pos_x > TAMANO_PANTALLA[0] - ancho_robot or pos_x < 0:
        vel_x = -vel_x
    if pos_y > TAMANO_PANTALLA[1] - alto_robot or pos_y < 0:
        vel_y = -vel_y

    # Limpia la pantalla
    pantalla.fill(BLANCO)

    # Dibuja el robot en la pantalla
    if pygame.time.get_ticks() % (velocidad_animacion * 3) < velocidad_animacion:
        pantalla.blit(imagen1, (pos_x, pos_y))
    elif pygame.time.get_ticks() % (velocidad_animacion * 3) < velocidad_animacion * 2:
        pantalla.blit(imagen2, (pos_x, pos_y))
    else:
        pantalla.blit(imagen3, (pos_x, pos_y))

    # Actualiza la pantalla
    pygame.display.flip()

    # Establece la velocidad del juego
    reloj.tick(60)

# Cierra Pygame
pygame.quit()