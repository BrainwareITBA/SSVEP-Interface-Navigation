import sys
import pygame
from datetime import datetime
from utils.constants import *
from gui.gui_utils import *
from gui.Pointer import Pointer

def main(output_file):

    pygame.init()
    window = pygame.display.set_mode((0,0))
    pygame.display.set_caption('Brainware Games')
    pygame.display.set_icon(pygame.image.load('resources/logo.png'))

    btn_w = 100
    btn_h = 100
    gap = 50
    window_w = window.get_width()
    window_h = window.get_height()

    button_names = ["UP", "RIGHT", "DOWN", "LEFT", "SELECT"]
    control_buttons = draw_control_buttons(button_names, btn_w, btn_h, gap, window_w, window_h)

    pointer_w = 27
    pointer_h = 8

    pointer_position = (window_w/2-pointer_w/2, window_h/2-(btn_h*3/2+gap)-2*pointer_h)
    current_time = pygame.time.get_ticks()
    pointer = Pointer(pointer_position, current_time, get_delay(0.125))

    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    text = font.render('ESC to quit, SPACE for start/stop timestamps', True, WHITE)
    text_rect = text.get_rect()
    text_rect.bottomleft = (10, window_h - 10)
    window.blit(text, text_rect)

    count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if count % 2 == 0:
                    s = "Start"
                else:
                    s = "End"
                with open(output_file, 'a') as f:
                    print(f"{s} @ {datetime.now()}", file=f)
                count += 1

        current_time = pygame.time.get_ticks()
        for name in button_names:
            control_buttons[name].update(current_time)
        pointer.update(current_time, window_w, window_h, btn_w, btn_h, gap)
        window.fill(BLACK)
        window.blit(text, text_rect)
        for name in button_names:
            control_buttons[name].draw(window)
        pointer.draw(window)
        pygame.display.update()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        filename = f"output{datetime.now().strftime('-%d%m%Y-%H%M%S')}.txt"
    else:
        filename = sys.argv[1]
    main(filename)