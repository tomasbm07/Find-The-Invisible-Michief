import pygame
import random as r
import math as m

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 144


def main():
    run = True
    pygame.init()
    pygame.mixer.init()

    info_object = pygame.display.Info()
    scale = 0.9
    screen = pygame.display.set_mode((int(info_object.current_w * scale), int(info_object.current_h * scale)))

    screen_size = (int(info_object.current_w * scale), int(info_object.current_h * scale))

    clock = pygame.time.Clock()

    michief_img = pygame.image.load("Michief.png")
    img_size = list(michief_img.get_size())

    points = 0

    draw_michief = True

    sound = pygame.mixer.Sound("sound.wav")

    while run:
        pygame.display.set_caption(f"Find the Invisible Michief - Points = {points}")
        clock.tick(FPS)
        screen.fill(WHITE)

        if draw_michief:
            x_gen = r.randint(0, int(info_object.current_w * scale) - img_size[0])
            y_gen = r.randint(0, int(info_object.current_h * scale) - img_size[1])
            draw_michief = False

        idk = pygame.draw.rect(screen, BLACK, [x_gen, y_gen, img_size[0], img_size[1]], 0)

        center = (x_gen + img_size[0] / 2, y_gen + img_size[1] / 2)

        sound.set_volume(1 - (m.dist(center, pygame.mouse.get_pos())) / (screen_size[0]))
        sound.play()
        pygame.time.wait(400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if idk.collidepoint(x, y):
                    draw_michief = True
                    points += 1
                    screen.fill(WHITE)
                    screen.blit(michief_img, (x_gen, y_gen))
                    pygame.display.update()
                    sound.stop()
                    sound.play()
                    pygame.time.wait(2000)

        pygame.display.update()


if __name__ == '__main__':
    main()
