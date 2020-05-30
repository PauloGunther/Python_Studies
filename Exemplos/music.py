# ABRIR UM ARQUIVO MP3
import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
