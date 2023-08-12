import pygame
import random

def Game():
    pygame.init()

    class Laser(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load("imagenes/laser.png").convert(), (105, 105))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
        
        def update(self):
            self.rect.y -= 2
            
    class Enemigo(pygame.sprite.Sprite):
        def __init__(self,medida):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load("imagenes/enemigo.png").convert(), (115, 115))
            self.rect = self.image.get_rect()
            self.image.set_colorkey((0,0,0))
            self.rect.centerx = random.randint(0, medida[0])
            self.rect.centery = -50 

        def update(self):
            self.rect.y += 1

    pos_x = 300
    pos_y = 800
    x_speed = 0
    y_speed = 0
    medida = (500,700)
    color = (0, 0, 43)
    var = True
    time_inicial = 0
    espera_time = 1000

    sonido_fondo = pygame.mixer.Sound("fondo.mp3")
    pygame.mixer.Sound.play(sonido_fondo, -1)

    nave = pygame.image.load("imagenes/nave.png")
    nave_tra = pygame.transform.scale(nave, (150, 150))
    ven_go = pygame.display.set_mode(medida)
    pygame.display.set_caption("juego")

    sprites = pygame.sprite.Group()
    lasers = pygame.sprite.Group()

    while var:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -1
                if event.key == pygame.K_RIGHT:
                    x_speed = 1
                if event.key == pygame.K_DOWN:
                    y_speed = 1
                if event.key == pygame.K_UP:
                    y_speed = -1
                if event.key == pygame.K_SPACE:
                    current_time = pygame.time.get_ticks()
                    if current_time - time_inicial >= espera_time:
                        time_inicial = current_time
                        laser = Laser(pos_x + 70, pos_y - 10 )
                        sprites.add(laser)
                        lasers.add(laser)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = 0
                if event.key == pygame.K_DOWN:
                    y_speed = 0
                if event.key == pygame.K_UP:
                    y_speed = 0

        if pos_x < 0:
            pos_x = 0
        if pos_x > medida[0] - 150:
            pos_x = medida[0] - 150
        if pos_y < 0:
            pos_y = 0
        if pos_y > medida[1] - 150:
            pos_y = medida[1] - 150

        ven_go.fill(color)
        ven_go.blit(nave_tra, (pos_x, pos_y))
        pos_x += x_speed
        pos_y += y_speed

        lasers.update()
        lasers.draw(ven_go)
        

        if random.randint(0,800 ) < 1:
            enemigo = Enemigo(medida)
            sprites.add(enemigo)
            
        sprites.update()
        sprites.draw(ven_go)

        pygame.display.update()

    pygame.quit()
