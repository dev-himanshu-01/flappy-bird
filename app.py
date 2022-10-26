from ast import main
import random
import sys
from unicodedata import name

import pygame
from pygame.locals import *

# GLOBAL VARIABLES FOR THE GAMES
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUND_Y = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUND = {}
PLAYER = 'assets/img/bird.png'
BACKGROUND = 'assets/img/background.jpg'
PIPE = 'assets/img/pipe.png'


def welcomeScreen():
    # SHOWS WELCOME IMAGES ON THE SCREEN

    playerX = int(SCREENWIDTH/5)
    playerY = int(SCREENHEIGHT - GAME_SPRITES["player"].get_height())/2

    messageX = int(SCREENWIDTH - GAME_SPRITES["message"].get_height())/2
    messageY = int(SCREENHEIGHT * 0.13)

    baseX = 0

    while True:
        for event in pygame.event.get():
            # print("🫳", event)
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # ADD MORE HERE
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key=K_SPACE or event.key == K_UP):
                print("Lawde!!")
                return
            else:

                # MAIN FXN FROM WHERE THE GAME STARTS
if __name__ == "__main__":

    pygame.init()

    FPSCLOCK = pygame.time.Clock()

    pygame.display.set_caption("FLAPPY BIRD BY HIMANSHU")

    GAME_SPRITES["number"] = (
        pygame.image.load("assets/img/0.png").convert_alpha(),
        pygame.image.load("assets/img/1.png").convert_alpha(),
        pygame.image.load("assets/img/2.png").convert_alpha(),
        pygame.image.load("assets/img/3.png").convert_alpha(),
        pygame.image.load("assets/img/4.png").convert_alpha(),
        pygame.image.load("assets/img/5.png").convert_alpha(),
        pygame.image.load("assets/img/6.png").convert_alpha(),
        pygame.image.load("assets/img/7.png").convert_alpha(),
        pygame.image.load("assets/img/8.png").convert_alpha(),
        pygame.image.load("assets/img/9.png").convert_alpha(),
    )

    GAME_SPRITES["message"] = pygame.image.load(
        "assets/img/message.png").convert_alpha()

    GAME_SPRITES["base"] = pygame.image.load(
        "assets/img/base.png").convert_alpha()

    GAME_SPRITES["pipe"] = (

        pygame.image.load(PIPE).convert_alpha(),
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180)

    )

    # GAME SOUNDS
    GAME_SOUND["die"] = pygame.mixer.Sound("assets/audio/die.wav")
    GAME_SOUND["hit"] = pygame.mixer.Sound("assets/audio/hit.wav")
    GAME_SOUND["point"] = pygame.mixer.Sound("assets/audio/point.wav")
    GAME_SOUND["swoosh"] = pygame.mixer.Sound("assets/audio/swoosh.wav")
    GAME_SOUND["wing"] = pygame.mixer.Sound("assets/audio/wing.wav")

    GAME_SPRITES["background"] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES["player"] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()
        # mainGame()
