import pygame
import sys
import os

pygame.init()
WIDTH, HEIGHT = 1440, 900
FPS = 60


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((1, 1))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move_hero(self, direction):
        if direction == 'up':
            self.pos = (self.pos[0], self.pos[1] - 1)
            self.rect = self.image.get_rect().move(
                tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)
        elif direction == 'down':
            self.pos = (self.pos[0], self.pos[1] + 1)
            self.rect = self.image.get_rect().move(
                tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)
        elif direction == 'left':
            self.pos = (self.pos[0] - 1, self.pos[1])
            self.rect = self.image.get_rect().move(
                tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)
        elif direction == 'right':
            self.pos = (self.pos[0] + 1, self.pos[1])
            self.rect = self.image.get_rect().move(
                tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, field_size):
        self.field_size = field_size
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.field_size[0] + 1) * obj.rect.width

        if obj.rect.x >= (self.field_size[0]) * obj.rect.width:
            obj.rect.x += -obj.rect.width * (1 + self.field_size[0])
            obj.rect.y += self.dy

        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.field_size[1] + 1) * obj.rect.height
        if obj.rect.y >= (self.field_size[1]) * obj.rect.height:
            obj.rect.y += -obj.rect.height * (1 + self.field_size[1])

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = WIDTH // 2 - (target.rect.x + target.rect.w // 2)
        self.dy = HEIGHT // 2 - (target.rect.y + target.rect.h // 2)


tile_width, tile_height = 45, 45

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tile_images = {}
