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
lvl_map = [[0 for x in range(80)] for y in range(40)]
with open('data/map.txt', 'r') as f:
    for line in f.readlines():
        str = ''
        for sim in line:
            if sim == '0':
                str += '0'
            elif sim == 'X':
                str += 'X'
        txt_map.append(list(str))


def update_map(new_map):
    for i in range(len(new_map)):
        for j in range(len(new_map[0])):
            if new_map[i][j] == 'X':
                txt_map[i][j] = 'X'


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
                    and player.pos[0] != 79 \
                    and txt_map[player.pos[1]][player.pos[0] + 1] != 'X':
                player.move_hero('right')
            elif event.key == pygame.K_SPACE:
                lvl_map[player.pos[1]][player.pos[0]] = 'X'

    screen.fill((113, 221, 238))

    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)

    background_group.draw(screen)
    all_sprites.draw(screen)
    pygame.draw.rect(screen, (80, 80, 80), (65, 5, 160, 20))
    pygame.draw.rect(screen, (255, 0, 0), (70, 10, player.hp * 1.5, 10))
    pygame.draw.rect(screen, (80, 80, 80), (65, 25, 120, 20))
    pygame.draw.rect(screen, (0, 0, 255), (70, 30, 110 * (player.mana / player.full_mana), 10))
    pygame.draw.rect(screen, (66, 66, 66), (10, 10, 50, 50))
    player_group.draw(screen)
    screen.blit(icon2, (10, 10))

    pygame.display.flip()
update_map(lvl_map)
for line in lvl_map:
    print(line)
print()
for line in txt_map:
    print(line)
pygame.quit()

