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
    control_buttons[button_names[4]] = Rectangle(WHITE, (window_width/2-button_width/2, window_height/2-button_height/2, button_width, button_height), current_time, delays[4])

    return control_buttons
