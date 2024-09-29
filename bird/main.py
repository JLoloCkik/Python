import pygame
import neat
import time
import os
import random

WIN_WIDTH = 550
WIN_HEIGHT = 800
FPS = 30

score = 0
generation = 0
population = 0
pygame.font.init()
STAT_FONT = pygame.font.SysFont('Arial', 40)

BirdPath1 = os.path.join('img', 'bird1.png')
BirdPath2 = os.path.join('img', 'bird2.png')
BirdPath3 = os.path.join('img', 'bird3.png')
BasePath = os.path.join('img', 'base.png')
BgPath = os.path.join('img', 'bg.png')
PipePath = os.path.join('img', 'pipe.png')

screen_size = (WIN_WIDTH, WIN_HEIGHT)

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(BirdPath1)),
             pygame.transform.scale2x(pygame.image.load(BirdPath2)),
             pygame.transform.scale2x(pygame.image.load(BirdPath3))]

BASE_IMGS = [pygame.transform.scale2x(pygame.image.load(BasePath))]
PIPE_IMGS = [pygame.transform.scale2x(pygame.image.load(PipePath))]
BG_IMGS = [pygame.transform.scale2x(pygame.image.load(BgPath))]


class Bird:
    IMGS = BIRD_IMGS
    ANIMATION_TIME = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick_count = 0
        self.vel = 0
        self.high = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    # end

    def jump(self):
        self.vel = -9
        self.tick_count = 0
        self.high = self.y

    # end

    def move(self):
        self.tick_count += 1
        delta = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

        if delta >= 16:
            delta = 16
        if delta < 0:
            delta -= 2

        self.y = self.y + delta

    # end

    def draw(self, win):
        self.img_count += 1

        if self.img_count == self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        if self.img_count == (self.ANIMATION_TIME * 2):
            self.img = self.IMGS[1]
        if self.img_count == (self.ANIMATION_TIME * 3):
            self.img = self.IMGS[2]

        win.blit(self.img, (self.x, self.y))

    # end

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    # end


# end

class Pipe:
    GAP = 200
    VEL = 7

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(PIPE_IMGS, False, True)
        self.PIPE_BOTTOM = PIPE_IMGS

        self.passed = False
        self.set_height()

    # end

    def set_height(self):
        self.height = random.randrange(30, 550)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    # end

    def move(self):
        self.x -= self.VEL

    # end

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    # end

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - bird.y)
        bottom_offset = (self.x - bird.x, self.bottom - bird.y)

        t_point = bird_mask.overlap(top_mask, top_offset)
        b_point = bird_mask.overlap(bottom_mask, bottom_offset)

        if t_point or b_point:
            return True
        return False
    # end
# end
