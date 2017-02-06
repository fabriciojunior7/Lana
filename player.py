import pygame
import cores
import entidades

class Lana(entidades.Entidade):
	#Atributos
	def __init__(self, largura, altura, x, y, imagem, escala):
		entidades.Entidade.__init__(self, largura, altura, x, y, imagem, escala)