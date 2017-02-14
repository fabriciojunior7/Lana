import pygame
import cores

class Entidade(pygame.sprite.Sprite):
	#Atributos
	def __init__(self, largura, altura, x, y, imagem, cor, escalaX, escalaY):
		pygame.sprite.Sprite.__init__(self)
		self.largura = largura
		self.altura = altura
		self.escalaX = escalaX
		self.escalaY = escalaY
		self.x = x
		self.y = y
		self.cor = cor
		if(imagem != ""):
			self.imagem = pygame.image.load(imagem)
			if(self.escalaX == 0 and self.escalaY == 0):
				self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
				self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
			else:
				self.corpo = pygame.Rect(self.x, self.y, self.escalaX, self.escalaY)
				self.imagem = pygame.transform.scale(self.imagem, (self.escalaX, self.escalaY))
		else:
			self.imagem = ""
			if(self.escalaX == 0 and self.escalaY == 0):
				self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
			else:
				self.corpo = pygame.Rect(self.x, self.y, self.escalaX, self.escalaY)


	#Metodos
	def desenha(self, tela):
		if(self.escalaX == 0 and self.escalaY == 0):
			self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		else:
			self.corpo = pygame.Rect(self.x, self.y, self.escalaX, self.escalaY)

		pygame.draw.rect(tela, self.cor, self.corpo)
		
		if(self.imagem != ""):
			tela.blit(self.imagem, (self.x, self.y))