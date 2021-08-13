
import sys 
import pygame
import time
import random
from pygame.locals import *
 
pygame.init()
 
fps = 1
fpsClock = pygame.time.Clock()
 
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bichinho Eletronico v1.0 Desenvolvido por Ezequiel Martinez')
 
backgroundImage = pygame.image.load('lcd_display_background.png').convert_alpha()
backgroundImageCrystal = pygame.image.load('lcd_display_crystal.png').convert_alpha()

pixelImage = pygame.image.load('pixel.png').convert_alpha()

bichinho1 = (
('80x0'),
('30x0','2x1','14x0','2x1'),
('30x0','2x1','14x0','2x1'),
('32x0','2x1','10x0','2x1'),
('32x0','2x1','10x0','2x1'),
('32x0','14x1'),
('32x0','14x1'),
('30x0','18x1'),
('30x0','18x1'),
('28x0','4x1','2x0','10x1','2x0','4x1'),
('28x0','4x1','2x0','10x1','2x0','4x1'),
('26x0','26x1'),
('26x0','26x1'),
('26x0','2x1','2x0','18x1','2x0','2x1'),
('26x0','2x1','2x0','18x1','2x0','2x1'),
('26x0','2x1','2x0','2x1','14x0','2x1','2x0','2x1'),
('26x0','2x1','2x0','2x1','14x0','2x1','2x0','2x1'),
('32x0','4x1','6x0','4x1'),
('32x0','4x1','6x0','4x1'),
('80x0'),
('80x1')

)

bichinho2 = (
('80x0'),
('29x0','2x1','14x0','2x1'),
('29x0','2x1','14x0','2x1'),
('31x0','2x1','10x0','2x1'),
('31x0','2x1','10x0','2x1'),
('31x0','14x1'),
('31x0','14x1'),
('29x0','18x1'),
('29x0','18x1'),
('27x0','4x1','2x0','10x1','2x0','4x1'),
('27x0','4x1','2x0','10x1','2x0','4x1'),
('25x0','26x1'),
('25x0','26x1'),
('25x0','2x1','2x0','18x1','2x0','2x1'),
('25x0','2x1','2x0','18x1','2x0','2x1'),
('25x0','2x1','2x0','2x1','14x0','2x1','2x0','2x1'),
('25x0','2x1','2x0','2x1','2x0','2x1','6x0','2x1','2x0','2x1','2x0','2x1'),
('31x0','4x1','6x0','4x1'),
('31x0','2x1','10x0','2x1'),
('80x0'),
('80x1')

)

spriteBichinho = [bichinho1,bichinho2]


merda1 = (
('80x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('80x0'),
('80x1')

)

merda2 = (
('80x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('80x0'),
('80x1')

)


merda3 = (
('80x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1','1x0','1x0','1x0','1x0','1x0','1x0'),
('80x0'),
('80x1')

)

spriteMerda = [merda1,merda2,merda3]


sono1 = (
('80x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('80x0'),
('80x1')

)


sono2 = (
('80x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('80x0'),
('80x1')

)

spriteSono = [sono1,sono2]

menuItems = (
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),
('80x0'),

('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x1','1x1','1x0','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x1','1x1','1x0','1x0', '1x0','1x1','1x1','1x1','1x0','1x0','1x0','1x1','1x1','1x1','1x0' ,'1x0','1x0','1x0','1x1','1x0','1x0','1x1','1x1','1x1','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x1','1x1','1x0','1x1','1x0','1x1','1x0','1x1','1x0','1x1','1x0','1x1','1x0','1x0','1x1','1x0', '1x1','1x1','1x1','1x0','1x1','1x0','1x1','1x1','1x1','1x1','1x1' ,'1x0','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x1','1x0'),
('1x0','1x0','1x1','1x1','1x1','1x0','1x0','1x1','1x1','1x1','1x1','1x0','1x1','1x0','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x1','1x0', '1x1','1x1','1x1','1x1','1x1','1x0','1x0','1x0','1x0','1x0','1x0' ,'1x0','1x0','1x0','1x1','1x0','1x1','1x1','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x1','1x1','1x1','1x1','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x1','1x1','1x0','1x0', '1x0','1x1','1x1','1x1','1x0','1x0','1x1','1x0','1x1','1x0','1x1' ,'1x0','1x0','1x0','1x1','1x0','1x1','1x1','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x1','1x1','1x1','1x0','1x0','1x1','1x0','1x0','1x1','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x1','1x0', '1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0','1x0' ,'1x0','1x0','1x0','1x1','1x0','1x0','1x1','1x1','1x1','1x0','1x0'),
('1x0','1x1','1x1','1x1','1x1','1x1','1x0','1x1','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x1','1x0', '1x1','1x1','1x1','1x1','1x1','1x0','1x1','1x0','1x1','1x0','1x1' ,'1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x1','1x0','1x0','1x1','1x0','1x1','1x0','1x1','1x0','1x1','1x0','1x1','1x0','1x0','1x1','1x0', '1x1','1x0','1x0','1x0','1x1','1x0','1x0','1x0','1x0','1x0','1x0' ,'1x0','1x1','1x1','1x1','1x1','1x1','1x0','1x0','1x0','1x0','1x0'),
('1x0','1x0','1x1','1x1','1x1','1x0','1x0','1x0','1x1','1x1','1x0','1x0','1x0','1x1','1x0','1x1','1x0','1x0','1x0','1x1','1x1','1x0','1x0', '1x1','1x1','1x1','1x1','1x1','1x0','1x1','1x0','1x1','1x0','1x1' ,'1x0','1x1','1x1','1x1','1x1','1x1','1x0','1x0','1x0','1x0','1x0')
)

a = ( 
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1')
)

b = ( 
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x0')
)

c = ( 
('1x0','1x0','1x1','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x0','1x1','1x1','1x1')
)

d = ( 
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x0')
)

e = ( 
('1x0','1x1','1x1','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x1','1x1','1x1')
)

f = ( 
('1x0','1x1','1x1','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x0','1x0','1x0')
)

g = ( 
('1x0','1x0','1x1','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x0','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0')
)

h = ( 
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1')
)

i = ( 
('1x0','1x1'),
('1x0','1x0'),
('1x0','1x1'),
('1x0','1x1'),
('1x0','1x1')
)


j = ( 
('1x0','1x0','1x0','1x1'),
('1x0','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x1'),
('1x0','1x1','1x0','1x1'),
('1x0','1x0','1x1','1x0')
)

k = ( 
('1x0','1x1','1x1','1x0','1x1'),
('1x0','1x1','1x0','1x1','1x0'),
('1x0','1x1','1x1','1x0','1x0'),
('1x0','1x1','1x0','1x1','1x0'),
('1x0','1x1','1x0','1x1','1x1')
)

l = ( 
('1x0','1x1','1x0','1x0'),
('1x0','1x1','1x0','1x0'),
('1x0','1x1','1x0','1x0'),
('1x0','1x1','1x0','1x0'),
('1x0','1x1','1x1','1x1')
)

m = ( 
('1x0','1x1','1x0','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x0','1x1','1x1'),
('1x0','1x1','1x0','1x1','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x0','1x1')
)

n = ( 
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x0','1x1'),
('1x0','1x1','1x0','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1')
)

o = ( 
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0')
)

p = ( 
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x0','1x0','1x0')
)

q = ( 
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x1','1x0'),
('1x0','1x0','1x1','1x0','1x1')
)

r = ( 
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1')
)

s = ( 
('1x0','1x0','1x1','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x0')
)

t = ( 
('1x0','1x1','1x1','1x1'),
('1x0','1x0','1x1','1x0'),
('1x0','1x0','1x1','1x0'),
('1x0','1x0','1x1','1x0'),
('1x0','1x0','1x1','1x0')
)

u = ( 
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0')
)

v = ( 
('1x0','1x1','1x0','1x1'),
('1x0','1x1','1x0','1x1'),
('1x0','1x1','1x0','1x1'),
('1x0','1x1','1x0','1x1'),
('1x0','1x0','1x1','1x0')
)

w = ( 
('1x0','1x1','1x0','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x1','1x0','1x1'),
('1x0','1x1','1x1','1x0','1x1','1x1')
)

x = ( 
('1x0','1x1','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x0','1x1','1x0'),
('1x0','1x0','1x0','1x1','1x0','1x0'),
('1x0','1x0','1x1','1x0','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x0','1x1')
)

y = ( 
('1x0','1x1','1x0','1x1'),
('1x0','1x1','1x0','1x1'),
('1x0','1x0','1x1','1x0'),
('1x0','1x0','1x1','1x0'),
('1x0','1x0','1x1','1x0')
)

z = ( 
('1x0','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x1','1x1','1x1')
)

doisPontos = ( 
('1x0','1x0'),
('1x0','1x1'),
('1x0','1x0'),
('1x0','1x1'),
('1x0','1x0')
)

um = ( 
('1x0','1x0','1x1'),
('1x0','1x1','1x1'),
('1x0','1x0','1x1'),
('1x0','1x0','1x1'),
('1x0','1x0','1x1')
)
 
dois = ( 
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x1','1x1','1x1')
)
 

tres = ( 
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x0','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x0')
)
 

tres = ( 
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x0')
)
 

quatro = ( 
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x0','1x0','1x1')
)
 

cinco = ( 
('1x0','1x1','1x1','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x1','1x1','1x1','1x0')
)
 

seis = ( 
('1x0','1x0','1x1','1x1','1x1'),
('1x0','1x1','1x0','1x0','1x0'),
('1x0','1x1','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0')
)

sete = ( 
('1x0','1x1','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x0','1x1','1x0'),
('1x0','1x0','1x1','1x0','1x0'),
('1x0','1x0','1x1','1x0','1x0')
)

oito = ( 
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0')
)

nove = ( 
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x1'),
('1x0','1x0','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0')
)

zero = ( 
('1x0','1x0','1x1','1x1','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x0','1x1','1x1','1x0')
)


traco = ( 
('1x0','1x0','1x0'),
('1x0','1x0','1x0'),
('1x0','1x1','1x1'),
('1x0','1x0','1x0'),
('1x0','1x0','1x0')
)

espaco = ( 
('1x0','1x0'),
('1x0','1x0'),
('1x0','1x0'),
('1x0','1x0'),
('1x0','1x0')
)

porcentagem = ( 
('1x0','1x0','1x0','1x0','1x0'),
('1x0','1x1','1x0','1x0','1x1'),
('1x0','1x0','1x0','1x1','1x0'),
('1x0','1x0','1x1','1x0','1x0'),
('1x0','1x1','1x0','1x0','1x1')
)

def bitfy(texto):
	
	linhaTemp = []
	linhaFinal = []
	espacamento = 1
	
	for linha in range(5):
		for letra in texto:

			if letra == 'a':
				linhaTemp.append(a[linha])

			elif letra == 'b':
				linhaTemp.append(b[linha])

			elif letra == 'c':
				linhaTemp.append(c[linha])

			elif letra == 'd':
				linhaTemp.append(d[linha])

			elif letra == 'e':
				linhaTemp.append(e[linha])
				
			elif letra == 'f':
				linhaTemp.append(f[linha])
				
			elif letra == 'g':
				linhaTemp.append(g[linha])
				
			elif letra == 'h':
				linhaTemp.append(h[linha])
				
			elif letra == 'i':
				linhaTemp.append(i[linha])
				
			elif letra == 'j':
				linhaTemp.append(j[linha])
				
			elif letra == 'k':
				linhaTemp.append(k[linha])
				
			elif letra == 'l':
				linhaTemp.append(l[linha])
				
			elif letra == 'm':
				linhaTemp.append(m[linha])
				
			elif letra == 'n':
				linhaTemp.append(n[linha])
				
			elif letra == 'o':
				linhaTemp.append(o[linha])
				
			elif letra == 'p':
				linhaTemp.append(p[linha])
				
			elif letra == 'q':
				linhaTemp.append(q[linha])
				
			elif letra == 'r':
				linhaTemp.append(r[linha])
				
			elif letra == 's':
				linhaTemp.append(s[linha])
				
			elif letra == 't':
				linhaTemp.append(t[linha])

			elif letra == 'u':
				linhaTemp.append(u[linha])

			elif letra == 'v':
				linhaTemp.append(v[linha])

			elif letra == 'w':
				linhaTemp.append(w[linha])

			elif letra == 'x':
				linhaTemp.append(x[linha])

			elif letra == 'y':
				linhaTemp.append(y[linha])

			elif letra == 'z':
				linhaTemp.append(z[linha])

			elif letra == ':':
				linhaTemp.append(doisPontos[linha])

			elif letra == ' ':
				linhaTemp.append(espaco[linha])

			elif letra == '0':
				linhaTemp.append(zero[linha])

			elif letra == '1':
				linhaTemp.append(um[linha])

			elif letra == '2':
				linhaTemp.append(dois[linha])

			elif letra == '3':
				linhaTemp.append(tres[linha])

			elif letra == '4':
				linhaTemp.append(quatro[linha])

			elif letra == '5':
				linhaTemp.append(cinco[linha])

			elif letra == '6':
				linhaTemp.append(seis[linha])

			elif letra == '7':
				linhaTemp.append(sete[linha])

			elif letra == '8':
				linhaTemp.append(oito[linha])
		
			elif letra == '9':
				linhaTemp.append(nove[linha])

			elif letra == '-':
				linhaTemp.append(traco[linha])

			elif letra == '%':
				linhaTemp.append(porcentagem[linha])

		#print ( sum(linhaTemp,()) )
		linhaFinal.append( sum(linhaTemp,() )) 
		linhaTemp = []
	
	return linhaFinal

def getBarraStatus(felicidade,saude,energia,idade,fome):
	baseMap = (
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	)

	espaciamento = ['80x0']

	meuOutroTexto = tuple(bitfy('felicidade: '+str(felicidade)+'%'))
	baseMap += tuple(meuOutroTexto)

	baseMap += tuple(espaciamento)
	meuOutroTexto = bitfy('saude: '+str(saude)+'%')	
	baseMap += tuple(meuOutroTexto)

	baseMap += tuple(espaciamento)
	meuOutroTexto = bitfy('energia: '+str(energia)+'%')	
	baseMap += tuple(meuOutroTexto)

	baseMap += tuple(espaciamento)
	meuOutroTexto = bitfy('idade: '+str(idade))	
	baseMap += tuple(meuOutroTexto)
	
	baseMap += tuple(espaciamento)
	meuOutroTexto = bitfy('fome: '+str(fome)+'%')	
	baseMap += tuple(meuOutroTexto)
	
	return baseMap


def getSplashMessage(text1,text2,text3=''):
	baseMap = (
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	('80x0'),
	)

	espaciamento = ['80x0']

	meuOutroTexto = bitfy(str(text1))
	baseMap += tuple(meuOutroTexto)

	baseMap += tuple(espaciamento)
	meuOutroTexto = bitfy(str(text2))
	baseMap += tuple(meuOutroTexto)
	
	baseMap += tuple(espaciamento)
	meuOutroTexto = bitfy(str(text3))
	baseMap += tuple(meuOutroTexto)
	
	return baseMap

def getHugeMap(pixelLineMap):
	hugeStringLine = ''
	hugeLine = []
	
	for line in pixelLineMap:
		if type(line) is not tuple:

			qty = line[0:line.index('x')]
			value = line[line.index('x')+1]
				
			hugeStringLine = hugeStringLine+ (int(qty)*str(value))
			
		else:
			for part in line:
			
				qty = part[0:part.index('x')]
				value = part[part.index('x')+1]
				
				hugeStringLine = hugeStringLine+ (int(qty)*str(value))
		
		hugeLine.append(hugeStringLine)
		hugeStringLine = ''
	
	#print (hugeLine)
	return hugeLine
	
def drawPixelWithMap(stringHugeMapCollecion):
	vertical = 0
	for stringHugeMap in stringHugeMapCollecion:
		for pixelPosition in range (0,len(stringHugeMap)):
			if int(stringHugeMap[pixelPosition]) > 0:
				screen.blit( pixelImage, (pixelPosition*10 , vertical ))

		vertical += 10

class Sequencer():
	def __init__(self, spriteLen):
		self.spriteLen = spriteLen
		self.seq = 0
	
	def getNextIndex(self):
		if self.seq >= self.spriteLen-1:
			self.seq = 0
		else:
			self.seq += 1

		return self.seq
		
bichinhoSpriteSeq = Sequencer(len(spriteBichinho))
merdaSpriteSeq = Sequencer(len(spriteMerda))
sonoSpriteSeq = Sequencer(len(spriteSono))

screen.blit( backgroundImage, (0 , 0 ))

screen.blit( backgroundImageCrystal, (0 , 0 ))

pygame.display.flip()

ik = 0
vida =0
shitTimeLeft = -1
sleepTimeLeft = -1
baseFactor = ik
while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	screen.blit( backgroundImage, (0 , 0 ))
	print ('timing:',ik)
	
	if ik > 20 and ik < 50:

		drawPixelWithMap(getHugeMap(spriteBichinho[bichinhoSpriteSeq.getNextIndex()]))
		
		drawPixelWithMap(getHugeMap(menuItems))
		drawPixelWithMap(getHugeMap(getBarraStatus(random.randint(0,100),random.randint(0,100),random.randint(0,100),vida,random.randint(0,100))))
		
		if shitTimeLeft > 0:
			drawPixelWithMap(getHugeMap(spriteMerda[merdaSpriteSeq.getNextIndex()]))
			shitTimeLeft -=1

		elif shitTimeLeft < 0:
			shitTimeLeft = 0

		elif ik%10 == 0:
			shitTimeLeft = 5
			
		if sleepTimeLeft > 0:
			drawPixelWithMap(getHugeMap(spriteSono[sonoSpriteSeq.getNextIndex()]))
			sleepTimeLeft -=1

		elif sleepTimeLeft < 0:
			sleepTimeLeft = 0

		elif ik%7 == 0:
			sleepTimeLeft = 5
	
	elif ik >= 50 and ik <= 60:
		#print ('fim do jogo')
		drawPixelWithMap(getHugeMap(getSplashMessage('       fim do jogo','     teste - teste','ezequiel martinez')))
	
	elif ik > 60:
		#print ('saindo')
		pygame.quit()
		sys.exit()
		
	else:
		drawPixelWithMap(getHugeMap(getSplashMessage('    iniciando jogo','     teste - teste','ezequiel martinez')))

	screen.blit( backgroundImageCrystal, (0 , 0 ))
	
	pygame.display.flip()
	fpsClock.tick(fps)

	if ik%60 == 0:
		vida +=1
		
	ik +=1
	

