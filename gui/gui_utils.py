import pygame
from utils.constants import *
from utils.time_functions import *
from gui.Rectangle import Rectangle

'''
    Draws control buttons in clockwise order (up, right, down, left, center).
    Returns dictionary with the buttons identified by their names.
'''
def draw_control_buttons(button_names: list[str], button_width: int, button_height: int, gap: int, window_width: int, window_height: int):
    
    control_buttons = {}
    current_time = pygame.time.get_ticks()
    delays = get_delays()
    
    # Btn Up
    control_buttons[button_names[0]] = Rectangle(RED, (window_width/2-button_width/2, window_height/2-(button_height*3/2+gap), button_width, button_height), current_time, delays[0])
    # Btn Right
    control_buttons[button_names[1]] = Rectangle(RED, (window_width/2+(button_width/2+gap), window_height/2-button_height/2, button_width, button_height), current_time, delays[1])
    # Btn Down
    control_buttons[button_names[2]] = Rectangle(RED, (window_width/2-button_width/2, window_height/2+(button_height/2+gap), button_width, button_height), current_time, delays[2])
    # Btn Left
    control_buttons[button_names[3]] = Rectangle(RED, (window_width/2-(button_width*3/2+gap), window_height/2-button_height/2, button_width, button_height), current_time, delays[3])
    # Btn Center
    control_buttons[button_names[4]] = Rectangle(RED, (window_width/2-button_width/2, window_height/2-button_height/2, button_width, button_height), current_time, delays[4])

    return control_buttons


def draw_game_grid(window: pygame.Surface, line_width: int, margin: int):
    window_h = window.get_height()
    game_size = window_h - (2 * margin)
    # Vertical lines
    pygame.draw.line(window, WHITE, (margin + game_size // 3, margin), (margin + game_size // 3, window_h - margin), line_width)
    pygame.draw.line(window, WHITE, (margin + (game_size // 3) * 2, margin), (margin + (game_size // 3) * 2, window_h - margin), line_width)
    # Horizontal lines
    pygame.draw.line(window, WHITE, (margin, margin + game_size // 3), (window_h - margin, margin + game_size // 3), line_width)
    pygame.draw.line(window, WHITE, (margin, margin + (game_size // 3) * 2), (window_h - margin, margin + (game_size // 3) * 2), line_width)


def draw_board(board: list[list[int]], window: pygame.Surface, x_img: pygame.Surface, o_img: pygame.Surface, margin: int):
    window_h = window.get_height()
    game_size = window_h - (2 * margin)
    for y in range(3):
        for x in range(3):
            picker = lambda xx,oo: xx if board[y][x] == -1 else oo if board[y][x] == +1 else pygame.Surface((0, 0))
            window.blit(picker(x_img, o_img), (x * (game_size // 3) + margin + (game_size // 9), y * (game_size // 3) + margin + (game_size // 9)))

def highlight_tile(window: pygame.Surface, row: int, col: int, margin, color=None):
    window_h = window.get_height()
    game_size = window_h - (2 * margin)
    x = col * (game_size // 3) + margin
    y = row * (game_size // 3) + margin
    if color == None:
        window.blit(pygame.image.load('./resources/arrow.png'), (x, y))
    else:
        pygame.draw.rect(window, color, pygame.Rect(x, y, 60, 60))

def end_message(window: pygame.Surface, message: str):
    font = pygame.font.SysFont('arial', 25)
    text = font.render(message, True, YELLOW)
    new_text_rect = text.get_rect()
    new_text_rect.topleft = (0, 0)
    window.blit(text, new_text_rect)