import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('canonindmajor.mp3')
pygame.mixer.music.play()
pygame.event.wait()
