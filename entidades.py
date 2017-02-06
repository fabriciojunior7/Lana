import pygame
import cores

class Entidade(pygame.sprite.Sprite):
	#Atributos
	def __init__(self, largura, altura, x, y, imagem, escala):
		pygame.sprite.Sprite.__init__(self)
		self.largura = largura
		self.altura = altura
		self.x = x
		self.y = y
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		self.imagem = pygame.image.load(imagem)
		self.imagem = pygame.transform.scale(self.imagem, (escala, escala))

	#Metodos
	def desenha(self, tela):
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		pygame.draw.rect(tela, cores.vermelho, self.corpo)
		tela.blit(self.imagem, (self.x, self.y))