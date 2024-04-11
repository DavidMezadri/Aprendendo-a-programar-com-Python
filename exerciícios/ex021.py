#reproduzir mp3
import pygame
pygame.init()
pygame.mixer.music.load('twirling.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()