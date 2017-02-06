import pygame, sys
import cores
import player

def jogo():

	#Variaveis Globais
	largura = 1024
	altura = 768
	framesPorSegundo = 60
	tipoDaTela = 0

	pygame.init()
	tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
	pygame.display.set_caption("Lana - The Game")
	relogio = pygame.time.Clock()

	#Objetos
	lana = player.Lana(16, 16, 20, 20, "imagens/lana.png", 64)

	def atualizarTela():
		#Rodar
		relogio.tick(framesPorSegundo)
		pygame.display.update()
		#Desenhar
		tela.fill(cores.branco)
		lana.desenha(tela)

	while(True):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			#FullScreen
			if(event.type == pygame.KEYDOWN):
				if(event.key == pygame.K_F11):
					if(tipoDaTela == 0):
						tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
						tipoDaTela = 1
					elif(tipoDaTela == 1):
						tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
						tipoDaTela = 0




		#Rodar
		atualizarTela()



















jogo()
