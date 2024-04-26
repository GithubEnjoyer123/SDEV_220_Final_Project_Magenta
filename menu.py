import pygame, sys
from button import Button
from menu import *
import subprocess
from pygame import mixer

# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("assets/theme.mp3") 
  
# Setting the volume 
mixer.music.set_volume(0.2) 
  
# Start playing the song 
mixer.music.play() 

pygame.init()

SCREEN = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

# color variables
black = (0, 0, 0)
white = (255, 255, 255)
col_spd = 1

col_dir_breathe = [1, 1, 1]
col_dir_breathe = [1, -1, -1]
def_col_breathe = [221, 218, 191]
def_col_breathe = [100,0,100]
def_col_breathe = [100,100,0]

minimum = 0
maximum = 200

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

""" def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(320, 230), 
                            text_input="BACK", font=get_font(25), base_color=( 100, 100, 150 ), hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update() """
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(20).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(360, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(360, 230), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def col_change_breathe(color: list, direction: list) -> None:
    """
    This function changes an RGB list in a way that we achieve nice breathing effect.
    :param color: List of RGB values.
    :param direction: List of color change direction values (-1, 0, or 1).
    :return: None
    """
    for i in range(3):
        color[i] += col_spd * direction[i]
        if color[i] >= maximum or color[i] <= minimum:
            direction[i] *= -1
        if color[i] >= maximum:
            color[i] = maximum
        elif color[i] <= minimum:
            color[i] = minimum


def draw_text(text: str, size: int, col: list, x: int, y: int) -> None:
    """
    A simple function for displaying text strings on the game screen.
    :param text: The string to display.
    :param size: Size of the text.
    :param col: Color of the text.
    :param x: X coordinate of the text.
    :param y: Y coordinate of the text.
    :return: None
    """
    font_object = pygame.font.Font("assets/font.ttf", 45)
    text_surface = font_object.render(text, False, col)
    text_rect = text_surface.get_rect(center=(x, y))
    SCREEN.blit(text_surface, text_rect)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        """ MENU_TEXT = get_font(33).render("ULTIMATE Tic-Tac-Toe", True, ( 221, 218, 191 ))
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 40)) """

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(360, 250), 
                            text_input="PLAY", font=get_font(30), base_color=( 221, 218, 191 ), hovering_color="Green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(360, 400), 
                            text_input="OPTIONS", font=get_font(30), base_color=( 221, 218, 191 ), hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(360, 550), 
                            text_input="QUIT", font=get_font(30), base_color=( 221, 218, 191 ), hovering_color="Green")

        """ SCREEN.blit(MENU_TEXT, MENU_RECT) """

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    subprocess.run(["python", "main.py"])
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        # color update
        col_change_breathe(def_col_breathe, col_dir_breathe)
        col_change_breathe(def_col_breathe, col_dir_breathe)

        # text displaying
        draw_text("ULTIMATE", 40, def_col_breathe, 360, 40)
        draw_text("Tic - Tac - Toe", 40, def_col_breathe, 360, 100)

        pygame.display.update()

main_menu()