import pygame
import cores
import entidades

class Plataforma(entidades.Entidade):
	#Atributos
	def __init__(self, largura, altura, x, y, imagem, cor, escalaX, escalaY):
		entidades.Entidade.__init__(self, largura, altura, x, y, imagem, cor, escalaX, escalaY)

	#Metodos
