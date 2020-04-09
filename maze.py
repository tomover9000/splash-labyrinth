#!/usr/bin/env python3

import pygame as py
import random
from pygame.locals import *

BLOCK_SIZE = 20
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

def display(self, widht, height):
    py.display.set_mode((widht * BLOCK_SIZE, height * BLOCK_SIZE))
    window.fill(BLACK)
