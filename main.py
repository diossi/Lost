import pygame

from windows_image import *
from maps import *
from pers import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

start_screen(screen, clock)
window_with_text(screen, clock)
board = Board(screen, clock, 40, 40, top=0, left=0)
cur_map = load_image('rpgmap.png')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill('blue')
        screen.blit(cur_map, (0, 0))
        board.render(screen)
        player_group.draw(screen)
        pygame.display.flip()
pygame.quit()

