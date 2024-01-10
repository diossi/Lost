import pygame

from windows_image import *
from maps import *
from pers import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

start_screen(screen, clock)
window_with_text(screen, clock)
board = Board(screen, clock, 40, 40, top=0, left=0)
camera = Camera((40, 40))
tick = 0
txt_map = []
with open('data/map.txt', 'r') as f:
    for line in f.readlines():
        str = ''
        for sim in line:
            if sim == '0':
                str += '0'
            elif sim == 'X':
                str += 'X'
        txt_map.append(list(str))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP \
                    and player.pos[1] != 0 \
                    and txt_map[player.pos[1] - 1][player.pos[0]] != 'X':
                player.move_hero('up')
            elif event.key == pygame.K_DOWN \
                    and player.pos[1] != 39 \
                    and txt_map[player.pos[1] + 1][player.pos[0]] != 'X':
                player.move_hero('down')
            elif event.key == pygame.K_LEFT \
                    and player.pos[0] != 0 \
                    and txt_map[player.pos[1]][player.pos[0] - 1] != 'X':
                player.move_hero('left')
            elif event.key == pygame.K_RIGHT \
                    and player.pos[0] != 39 \
                    and txt_map[player.pos[1]][player.pos[0] + 1] != 'X':
                player.move_hero('right')

    screen.fill((113, 221, 238))

    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)

    background_group.draw(screen)
    player_group.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()
pygame.quit()

