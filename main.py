import pygame
from config import WIDTH, HEIGHT, FPS
from Field import Field


def main():
    pygame.display.set_caption('Тетрис')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    field = Field(screen)

    running = True
    isTrue = True

    move = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        if isTrue:
            field.create_block()
            isTrue = False
        field.draw_field()
        if move == 10:
            field.move_block()
            move = 0
        else:
            move += 1
        clock.tick(FPS)
        print(clock.get_fps())
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
