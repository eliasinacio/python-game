import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('IDGAF.mp3')
pygame.mixer.music.play()
x = input(' Digite algo. ')
pygame.event.wait()
