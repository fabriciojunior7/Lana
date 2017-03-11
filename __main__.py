import pygame, sys
import cores
import player, paredes

def jogo():

	#Variaveis Globais
	pygame.init()
	informacaoTela = pygame.display.Info()
	largura = informacaoTela.current_w
	altura = informacaoTela.current_h
	tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
	pygame.display.set_caption("Lana - The Game")
	relogio = pygame.time.Clock()
	framesPorSegundo = 60
	tempo = 1.0

	#Objetos
	lana = player.Lana(500, 50, 50, 50, cores.vermelho)
	walls = []
	numWalls = 10
	for i in range(numWalls):
		walls.append(paredes.Parede((i+1)*75, (i+1)*50, 75, 20, cores.cinza))
	

	def atualizarTela():
		#Rodar
		relogio.tick(framesPorSegundo)
		pygame.display.update()
		lana.atualizarPosicao(largura, altura, tempo)
		#Colisoes com a Parede
		for w in walls:
			if(lana.base.colliderect(w.topo)):
				lana.colidiuBase(w.y)
				break
			else:
				lana.colidindo = False
		for w in walls:
			if(lana.topo.colliderect(w.base)):
				lana.colidiuTopo(w.y + w.altura + w.alturaTB)

			if(lana.direita.colliderect(w.esquerda)):
				lana.colidiuDireita(w.x, w.largura)
			elif(lana.esquerda.colliderect(w.direita)):
				lana.colidiuEsquerda(w.x)
		#Desenhar
		tela.fill(cores.branco)
		for w in walls:
			w.desenhaEntidade(tela)
		lana.desenhaEntidade(tela)

	while(True):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			#Botao Pressionado
			if(event.type == pygame.KEYDOWN):
				#Temporizador
				if(event.key == pygame.K_MINUS):
					tempo /= 2.0
				if(event.key == pygame.K_EQUALS):
					tempo *= 2.0
				#Outros
				if(event.key == pygame.K_F5):
					jogo()
				if(event.key == pygame.K_ESCAPE):
					pygame.quit()
					sys.exit()
				lana.botaoPressionado(event.key)
			#Botao Solto
			if(event.type == pygame.KEYUP):
				lana.botaoSolto(event.key)




		#Rodar
		atualizarTela()


jogo()
