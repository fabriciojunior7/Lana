import pygame
import cores
import entidades

class Lana(entidades.Entidade):
	#Atributos
	def __init__(self, largura, altura, x, y, imagem, cor, escalaX, escalaY):
		entidades.Entidade.__init__(self, largura, altura, x, y, imagem, cor, escalaX, escalaY)
		self.velocidadeX = 2.0
		self.velocidadeY = 0.0
		self.maximaVelocidadeY = 5
		self.gravidade = 0.1
		self.LRQueda = [False, False, False]
		self.colidindo = False
		self.colisaoX = ""
		self.colisaoY = ""
		self.pulando = True

	#Metodos
	def atualizarPosicao(self):
		#Movimentacao Eixo X
		if(self.LRQueda[0] == True):
			self.x -= self.velocidadeX
		elif(self.LRQueda[1] == True):
			self.x += self.velocidadeX
		#Movimentacao Eixo Y
		if(self.colidindo == False):kkk
			if(self.velocidadeY < self.maximaVelocidadeY):
				self.velocidadeY += self.gravidade
			self.y += self.velocidadeY
		else:
			if(self.pulando == True):
				self.y = self.colisaoY - self.escalaY + 1
				self.velocidadeY = 0
				self.pulando = False
			

	def colidiu(self, c, y):
		self.colidindo = c
		if(self.colidindo == True):
			self.colisaoY = y
		else:
			self.colisaoY = ""


	#Botao Precionado
	def botaoPressionado(self, key):
		#Movimentacao Eixo X
		if(key == pygame.K_a):
			self.LRQueda[0] = True
		elif(key == pygame.K_d):
			self.LRQueda[1] = True
		#Movimentacao Eixo Y
		if(key == pygame.K_w):
			#self.y -= 10
			self.velocidadeY = -5
			self.pulando = True

	#Botao Solto
	def botaoSolto(self, key):
		if(key == pygame.K_a):
			self.LRQueda[0] = False
		elif(key == pygame.K_d):
			self.LRQueda[1] = False

