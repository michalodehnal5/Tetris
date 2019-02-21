#!/usr/bin/env python3

from src.constants import *
from src.block import *
from src.matrix_cell import *
from src.tetris_data import *

def main():
    pygame.display.init()
    pygame.font.init()
    pygame.time.set_timer(MOVE_BLOCK_EVENT, MOVE_BLOCK_SPEED)
    screen = pygame.display.set_mode((PYGAME_WINDOW_WIDTH, PYGAME_WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    tetris = TetrisData(0)
    block = tetris.generate_new_block()

    running = True
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOVE_BLOCK_EVENT:
            block = tetris.try_to_move_the_block(block, "down")

        if event.type == DELETE_LINE_EVENT:
            tetris.remove_lines_update_matrix()
            tetris.score += 1

        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if pressed[pygame.K_SPACE]:
                block = tetris.block_rotate_clock_wise(block)
            if pressed[pygame.K_UP]:
                block = tetris.try_to_move_the_block(block, "up")
            if pressed[pygame.K_DOWN]:
                block = tetris.try_to_move_the_block(block, "down")
            if pressed[pygame.K_LEFT]:
                block = tetris.try_to_move_the_block(block, "left")
            if pressed[pygame.K_RIGHT]:
                block = tetris.try_to_move_the_block(block, "right")

        if block == None:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        tetris.update_tetris_matrix_with(block)
        tetris.test_for_line_delete_condition()
        tetris.draw_tetris_field_by_matrix()

        screen.fill((0, 0, 0))
        tetris.draw_tetris_blocks(screen)
        tetris.draw_tetris_field(screen)
        tetris.draw_tetris_score(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
    pygame.quit()
