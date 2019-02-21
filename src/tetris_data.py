#!/usr/bin/env python3
import pygame
import random
import copy

from src.constants import *
from src.matrix_cell import *
from src.block import *

class TetrisData:
    def __init__(self, score, width=12, height=22, hidden_walls=True):
        self.width = width
        self.height = height
        self.hidden_walls = hidden_walls
        self.field = [[MatrixCell(0) for x in range(self.width)] for x in range(self.height)]
        self.score = score
        self.delete_line = -1
        self.make_tetris_walls()


    def make_tetris_walls(self):
        for y, row in enumerate(self.field):
            for x, column in enumerate(row):
                if x==0 or x==self.width-1 or y==self.height-1 or y==0:
                    self.field[y][x].value = 1
                    self.field[y][x].moveble = False
                    self.field[y][x].hidden = self.hidden_walls
                    self.field[y][x].colour = (192,192,192)


    def remove_lines_update_matrix(self):
        for y in range(self.delete_line, 1, -1):
            for x in range(1, self.width - 1):
                self.field[y][x].value = self.field[y - 1][x].value
                self.field[y][x].colour = self.field[y - 1][x].colour
                self.field[y][x].moveble = self.field[y - 1][x].moveble

        for x in self.field[1]:
            x.value = 0
            x.colour = (0, 0, 0)
            x.moveble = True

        self.delete_line = -1


    def test_for_line_delete_condition(self):
        full_line = [x.value for x in [MatrixCell(1) for x in range(self.width)]]
        for index_of_line in range(1, self.height - 1):
            if [ (x.value if not x.moveble else 0) for x in self.field[index_of_line] ] == full_line:
                self.delete_line = index_of_line

        if self.delete_line != -1:
            pygame.event.post(pygame.event.Event(DELETE_LINE_EVENT))


    def try_to_move_the_block(self, block, direction="down"):
        collision_block = copy.deepcopy(block)
        collision_block.abs_x += (1 if direction=="right" else -1 if direction=="left" else 0)
        collision_block.abs_y += (1 if direction=="down" else -1 if direction=="up" else 0)

        if self.wont_collide(collision_block):
            for y, row in enumerate(block.structure):
                for x, column in enumerate(row):
                    if self.field[block.abs_y + y][block.abs_x + x].moveble:
                        self.field[block.abs_y + y][block.abs_x + x].value = block.structure[y][x]
            block.abs_x = collision_block.abs_x
            block.abs_y = collision_block.abs_y
            return block
        else:
            if direction=="down":
                self.make_current_block_permanent(block)
                return self.generate_new_block()
            return block


    def block_rotate_clock_wise(self, block):
        new_row = []
        final_block = []
        for x in range(block.size):
            for y in range(block.size - 1, -1, -1):
                new_row.append(block.structure[y][x])
            final_block.append(new_row)
            new_row = []

        new_block = Block(final_block, block.abs_x, block.abs_y, block.colour)

        if self.wont_collide(new_block):
            return new_block
        else:
            return block


    def make_current_block_permanent(self, block):
        for y, row in enumerate(block.structure):
            for x, column in enumerate(row):
                if (block.structure[y][x] == 1) and \
                        ( (block.abs_y + y) <= (self.height - 1) ) and \
                        ( (0 <= (block.abs_x + x)) <= (self.width - 1) ) and \
                        (self.field[block.abs_y + y][block.abs_x + x].value == 1):
                    self.field[block.abs_y + y][block.abs_x + x].moveble = False
                    self.field[block.abs_y + y][block.abs_x + x].colour = block.colour


    def wont_collide(self, block):
        for y, row in enumerate(block.structure):
            for x, column in enumerate(row):
                if (block.abs_y + y) <= (self.height - 1) and \
                        0 <= (block.abs_x + x) <= (self.width - 1) and \
                        self.field[block.abs_y + y][block.abs_x + x].value==1 and \
                        not self.field[block.abs_y + y][block.abs_x + x].moveble and \
                        block.structure[y][x]==1:
                    return False
        return True


    def update_tetris_matrix_with(self, block):
        for y, row in enumerate(self.field):
            for x, column in enumerate(row):
                if self.field[y][x].moveble:
                    self.field[y][x].value = 0

        for y, row in enumerate(block.structure):
            for x, column in enumerate(row):
                if block.structure[y][x] == 1 and self.field[block.abs_y + y][block.abs_x + x].moveble:
                    self.field[block.abs_y + y][block.abs_x + x].value = block.structure[y][x]
                    self.field[block.abs_y + y][block.abs_x + x].colour = block.colour


    def generate_new_block(self):
        new_block = Block(BLOCKS[random.randrange(len(BLOCKS) - 1)], 4, 1, COLOURS[random.randrange(len(COLOURS) - 1)])
        game_over = self.test_for_game_over(new_block)
        return None if game_over else new_block


    def test_for_game_over(self, block):
        return not self.wont_collide(block)


    def draw_tetris_field(self, screen):
        if DISPLAY_WITH_PYGAME:
            matrix_start = 1 if self.hidden_walls else 0
            matrix_end = 1 if self.hidden_walls else 0
            for y in range(matrix_start, self.height - matrix_end):
                for x in range(matrix_start, self.width - matrix_end):
                    pygame.draw.rect(screen, GRID_COLOR, pygame.Rect(BASE_START_X + (x * BASE_BLOCK_SIZE), BASE_START_Y + (y * BASE_BLOCK_SIZE), BASE_BLOCK_SIZE, BASE_BLOCK_SIZE), 1)


    def draw_tetris_blocks(self, screen):
        if DISPLAY_WITH_PYGAME:
            for y in range(self.height):
                for x in range(self.width):
                    if self.field[y][x].value == 1 and not self.field[y][x].hidden:
                        pygame.draw.rect(screen, self.field[y][x].colour, pygame.Rect(BASE_START_X + (x * BASE_BLOCK_SIZE), BASE_START_Y + (y * BASE_BLOCK_SIZE), BASE_BLOCK_SIZE, BASE_BLOCK_SIZE))


    def draw_tetris_field_by_matrix(self):
        for row in self.field:
            result = [x.value for x in row]
            print(result)
        print("")


    def draw_tetris_score(self, screen):
        draw_text = pygame.font.SysFont("comicsansms", 30).render("SCORE: {}".format(self.score), True, (255,255,255))
        screen.blit(draw_text, (160, 665))
