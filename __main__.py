import pygame, sys
import cores
import player, plataformas

def jogo():

	#Variaveis Globais
	#largura = 1024
	#altura = 768
	largura = 900
	altura = 600
	framesPorSegundo = 60
	tipoDaTela = 0

	pygame.init()
	tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
	pygame.display.set_caption("Lana - The Game")
	relogio = pygame.time.Clock()

	#Objetos
	lana = player.Lana(16, 16, 200, 50, "imagens/lana.png", cores.verde, 48, 48)
	plataformasNaFase = [plataformas.Plataforma(150, 10, 200, 250, "", cores.preto, 0, 0)]

	def atualizarTela():
		#Rodar
		relogio.tick(framesPorSegundo)
		pygame.display.update()
		lana.atualizarPosicao()
		for p in plataformasNaFase:
			if(lana.corpo.colliderect(p.corpo)):
				lana.colidiu(True, p.y)
				break
			else:
				lana.colidiu(False, "")
		#Desenhar
		tela.fill(cores.branco)
		for p in plataformasNaFase:
			p.desenha(tela)
		lana.desenha(tela)

	while(True):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			#FullScreen
			if(event.type == pygame.KEYDOWN):
				lana.botaoPressionado(event.key)
				if(event.key == pygame.K_F11):
					if(tipoDaTela == 0):
						tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
						tipoDaTela = 1
					elif(tipoDaTela == 1):
						tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
						tipoDaTela = 0
			if(event.type == pygame.KEYUP):
				lana.botaoSolto(event.key)




		#Rodar
		atualizarTela()



















jogo()
