import pygame, sys

def jogo():
	
	pygame.init()
	largura = 1024
	altura = 768
	tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
	pygame.display.set_caption("Lana")
	relogio = pygame.time.Clock()
	frames = 10

	lana = pygame.image.load("imagens/morango.png")
	lana = pygame.transform.scale(lana, (32, 32))

	while(True):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			if(event.type == pygame.KEYDOWN):
				pygame.quit()
				sys.exit()


		#Rodar
		relogio.tick(frames)
		pygame.display.update()
		#Desenhar
		tela.fill((180, 180, 180))
		tela.blit(lana, (100, 100))


jogo()