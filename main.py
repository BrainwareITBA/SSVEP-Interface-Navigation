import sys
import pygame
from datetime import datetime
from utils.constants import *
from utils.time_functions import *
from gui.Rectangle import Rectangle


def main(output_file):

    pygame.init()
    window = pygame.display.set_mode((0, 0))
    pygame.display.set_caption('Brainware Games')
    pygame.display.set_icon(pygame.image.load('resources/logo.png'))

    btn_w = 100
    btn_h = 100
    gap = 50
    window_w = window.get_width()
    window_h = window.get_height()

    current_time = pygame.time.get_ticks()
    delays = get_delays()

    rect1 = Rectangle(RED, (window_w/2-btn_w/2, window_h/2-(btn_h*3/2+gap), btn_w, btn_h), current_time, delays[0])
    rect3 = Rectangle(RED, (window_w/2-(btn_w*3/2+gap), window_h/2-btn_h/2, btn_w, btn_h), current_time, delays[2])
    rect2 = Rectangle(RED, (window_w/2-btn_w/2, window_h/2-btn_h/2, btn_w, btn_h), current_time, delays[1])
    rect4 = Rectangle(RED, (window_w/2+(btn_w/2+gap), window_h/2-btn_h/2, btn_w, btn_h), current_time, delays[3])
    rect5 = Rectangle(RED, (window_w/2-btn_w/2, window_h/2+(btn_h/2+gap), btn_w, btn_h), current_time, delays[4])

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
        rect1.update(current_time)
        rect2.update(current_time)
        rect3.update(current_time)
        rect4.update(current_time)
        rect5.update(current_time)
        window.fill(BLACK)
        rect1.draw(window)
        rect2.draw(window)
        rect3.draw(window)
        rect4.draw(window)
        rect5.draw(window)
        pygame.display.update()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        filename = f"output{datetime.now().strftime('-%d%m%Y-%H%M%S')}.txt"
    else:
        filename = sys.argv[1]
    main(filename)