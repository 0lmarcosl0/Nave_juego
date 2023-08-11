import pygame

def Game():
    pos_x = 300
    pos_y = 800
    x_speed = 0
    y_speed = 0
    medida = (650, 420)
    color = (0, 0, 43)
    posicion = (200, 200)
    var = True
    pygame.init()
    nave = pygame.image.load("imagenes/nave.png")
    nave_tra = pygame.transform.scale(nave, (200, 200))
    ven_go = pygame.display.set_mode(medida)
    pygame.display.set_caption("juego")

    while var:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
        ven_go.fill(color)
        ven_go.blit(nave_tra, (pos_x, pos_y))
        pos_x += x_speed
        pygame.display.update()

    pygame.quit()

Game()