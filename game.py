import pygame

def Game():
	medida = (650,420)
	color = (0,0,43)
	posicion = (200,200)
	var = True
	
	ven_go = pygame.display.set_mode(medida)
	pygame.display.set_caption("juego")
	vent_go.fill(color)
	
	while var:
		for event in pygame.event.get():
			if event.type == pygame.QUIT():
				var = False
		pygame.display.update()
	pygame.quit()