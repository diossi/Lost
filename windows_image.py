import pygame
import sys
import os

WIDTH, HEIGHT = 1440, 900
FPS = 60
pygame.init()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkeys=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkeys is not None:
        for colorkey in colorkeys:
            if colorkey == -1:
                colorkey = image.get_at((1, 1))
            image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen(screen, clock):
    intro_text = ["Играть",
                  "Инструкция",
                  "Авторы"]

    fon = pygame.transform.scale(load_image('start_window.jpg'), (WIDTH, HEIGHT))
    coords_text = []
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 80)
    text_coord = 220
    for line in intro_text:
        string_rendered = font.render(line, True, 'white', pygame.Color((153, 92, 51)))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 720 - intro_rect.width // 2
        text_coord += intro_rect.height
        coords_text.append((intro_rect.x, intro_rect.y, intro_rect.width, intro_rect.height))
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if coords_text[0][0] + coords_text[0][2] > x > coords_text[0][0] and \
                            coords_text[0][1] + coords_text[0][3] > y > coords_text[0][1]:
                        return
                    elif coords_text[1][0] + coords_text[1][2] > x > coords_text[1][0] and \
                            coords_text[1][1] + coords_text[1][3] > y > coords_text[1][1]:
                        manual(screen, clock)
                        return
                    elif coords_text[2][0] + coords_text[2][2] > x > coords_text[2][0] and \
                            coords_text[2][1] + coords_text[2][3] > y > coords_text[2][1]:
                        authors(screen, clock)
                        return
        pygame.display.flip()
        clock.tick(FPS)


def manual(screen, clock):
    intro_text = ["Не читерить, не багоюзить, не оскорблять нпс, вести себя адекватно",
                  "Пщушгкпришгукерпшг куроепшгркегшщ пргкешгрпгшкерш",
                  "По ходу разработки игры мы доделаем инструкцию :3"]

    fon = pygame.transform.scale(load_image('start_window.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 150
    for line in intro_text:
        string_rendered = font.render(line, True, 'white', pygame.Color((153, 92, 51)))
        intro_rect = string_rendered.get_rect()
        text_coord += 15
        intro_rect.top = text_coord
        intro_rect.x = 20
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    font = pygame.font.Font(None, 80)
    string_rendered = font.render('Назад', True, 'white', pygame.Color((153, 92, 51)))
    intro_rect = string_rendered.get_rect()
    intro_rect.x, intro_rect.y = 1200, 30
    screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if intro_rect.x < x < intro_rect.x + intro_rect.width and \
                            intro_rect.y < y < intro_rect.y + intro_rect.height:
                        start_screen(screen, clock)
                        return
        pygame.display.flip()
        clock.tick(FPS)


def authors(screen, clock):
    intro_text = ["Цырулев А.А.",
                  "Валиев Д.И."]

    fon = pygame.transform.scale(load_image('start_window.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    text_coord = 300
    for line in intro_text:
        string_rendered = font.render(line, True, 'white', pygame.Color((153, 92, 51)))
        intro_rect = string_rendered.get_rect()
        text_coord += 15
        intro_rect.top = text_coord
        intro_rect.x = 720 - intro_rect.width // 2
        text_coord += intro_rect.height
        string_rendered.set_alpha(100)
        screen.blit(string_rendered, intro_rect)
    font = pygame.font.Font(None, 80)
    string_rendered = font.render('Назад', True, 'white', pygame.Color((153, 92, 51)))
    intro_rect = string_rendered.get_rect()
    intro_rect.x, intro_rect.y = 1200, 30
    screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if intro_rect.x < x < intro_rect.x + intro_rect.width and \
                            intro_rect.y < y < intro_rect.y + intro_rect.height:
                        start_screen(screen, clock)
                        return
        pygame.display.flip()
        clock.tick(FPS)


def window_with_text(screen, clock):
    screen.fill('black')
    number_text = 0
    plot_text = [["Будем доделывать", "Сюжет"],
                 ['2', 'АААААА'],
                 ['3', 'АААААА'],
                 ['4', 'АААААА'],
                 ['5', '123АА']]

    fon = pygame.transform.scale(load_image('window_with_text.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[0] < 720 and number_text != 0:
                        number_text -= 1
                    elif event.pos[0] >= 720:
                        number_text += 1
                    if number_text + 1 > len(plot_text):
                        return
        screen.blit(fon, (0, 0))
        text_coord = 300
        for line in plot_text[number_text]:
            string_rendered = font.render(line, True, (51, 51, 51), (204, 204, 204))
            plot_rect = string_rendered.get_rect()
            text_coord += 15
            plot_rect.top = text_coord
            plot_rect.x = 720 - plot_rect.width // 2
            text_coord += plot_rect.height
            screen.blit(string_rendered, plot_rect)
        pygame.display.flip()
        clock.tick(FPS)
