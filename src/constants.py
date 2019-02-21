#!/usr/bin/env python3
import pygame

TEST_DOT_BLOCK = [
    [1]
]

SQUARE_BLOCK = [
    [1 , 1],
    [1 , 1]
]

TRIANGLE_BLOCK = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 0, 0]
]

Z_BLOCK = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 0]
]

S_BLOCK = [
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 0]
]

BACK_L_BLOCK = [
    [1, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
]

L_BLOCK = [
    [0, 0, 0],
    [1, 1, 1],
    [1, 0, 0]
]

LONG_BLOCK = [
    [0, 0, 0, 0],
    [1 ,1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

BLOCKS = [
    SQUARE_BLOCK,
    TRIANGLE_BLOCK,
    LONG_BLOCK,
    S_BLOCK,
    Z_BLOCK,
    L_BLOCK,
    BACK_L_BLOCK
]

BASE_START_X = 15
BASE_START_Y = 15
BASE_BLOCK_SIZE = 30

GRID_COLOR = (50, 50, 50)
ORANGE_BLOCK_COLOR = (255, 100, 0)
RED_BLOCK_COLOR = (255, 0, 0)
BLUE_BLOCK_COLOR = (20, 20, 255)
GREEN_BLOCK_COLOR = (0, 255, 0)
YELLOW_BLOCK_COLOR = (255, 255, 0)
MAGENTA_BLOCK_COLOR = (255, 0, 255)
CYAN_BLOCK_COLOR = (0, 255, 255)

COLOURS = [
    RED_BLOCK_COLOR,
    BLUE_BLOCK_COLOR,
    GREEN_BLOCK_COLOR,
    YELLOW_BLOCK_COLOR,
    MAGENTA_BLOCK_COLOR,
    CYAN_BLOCK_COLOR
]

DISPLAY_WITH_PYGAME = True
PYGAME_WINDOW_HEIGHT = 690
PYGAME_WINDOW_WIDTH = 390

MOVE_BLOCK_EVENT = pygame.USEREVENT + 1
DELETE_LINE_EVENT = pygame.USEREVENT + 2

MOVE_BLOCK_SPEED = 250
