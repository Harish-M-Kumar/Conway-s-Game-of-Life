import time
import pygame
import numpy as np

bg_color = (10, 10, 10)
grid_color = (40, 40, 40)
die_next_color = (40, 255, 0)
alive_next_color = '#9966cc'


def update(screen, cells, size, with_progression=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        if cells[row, col] == 0:
            color = bg_color
        else:
            color = alive_next_color

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progression:
                    color = die_next_color
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progression:
                    color = alive_next_color
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progression:
                    color = alive_next_color

        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))
    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((1240, 720))
    cells = np.zeros((72, 124))
    screen.fill(grid_color)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//10, pos[0]//10] = 1
                update(screen, cells, 10)
                pygame.display.update()
        screen.fill(grid_color)

        if running:
            cells = update(screen, cells, 10, with_progression=True)
            pygame.display.update()

        time.sleep(0.001)


if __name__ == "__main__":
    main()
