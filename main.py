import sys
import pygame
from datetime import datetime
from utils.constants import *
from gui.gui_utils import *
from game.game_controls import *
from game.game_events import *
from pynput.keyboard import Controller

def main(output_file):

    pygame.init()
    #window = pygame.display.set_mode((1500, 600))
    window = pygame.display.set_mode((0,0))
    pygame.display.set_caption('Brainware Games')
    pygame.display.set_icon(pygame.image.load('resources/logo.png'))

    btn_w = 100
    btn_h = 100
    gap = 50
    window_w = window.get_width() * 3/2
    window_h = window.get_height()

    line_width = 5
    margin = 50
    draw_game_grid(window, line_width, margin)

    o_img, x_img = pygame.image.load('./resources/o.png'), pygame.image.load('./resources/x.png')

    row = 1
    col = 1
    highlight_tile(window, row, col, margin)
    board = [[None, None, None], [None, None, None], [None, None, None]]
    draw_board(board, window, x_img, o_img, margin)

    button_names = ["UP", "RIGHT", "DOWN", "LEFT", "SELECT"]
    control_buttons = draw_control_buttons(button_names, btn_w, btn_h, gap, window_w, window_h)

    keyboard = Controller()
    NEW_COMMAND = pygame.USEREVENT + 1

    count = 0
    turn = -1
    last_idx = 1
    end_game = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not end_game:
                match event.key:
                    case pygame.K_SPACE:
                        if count % 2 == 0:
                            s = "Start"
                        else:
                            s = "End"
                        with open(output_file, 'a') as f:
                            print(f"{s} @ {datetime.now()}", file=f)
                        count += 1
                    case pygame.K_UP:
                        highlight_tile(window, row, col, margin, BLACK)
                        row = (row-1) % 3
                        highlight_tile(window, row, col, margin)
                    case pygame.K_DOWN:
                        highlight_tile(window, row, col, margin, BLACK)
                        row = (row+1) % 3
                        highlight_tile(window, row, col, margin)
                    case pygame.K_LEFT:
                        highlight_tile(window, row, col, margin, BLACK)
                        col = (col-1) % 3
                        highlight_tile(window, row, col, margin)
                    case pygame.K_RIGHT:
                        highlight_tile(window, row, col, margin, BLACK)
                        col = (col+1) % 3
                        highlight_tile(window, row, col, margin)
                    case pygame.K_RETURN:
                        selected, end_game = select(row, col, board, turn, window)
                        if selected and not end_game:
                            turn = (-1) * turn
                    case pygame.K_n:
                        pygame.event.post(pygame.event.Event(NEW_COMMAND)) # TODO: Trigger event when events.txt gets updated
            elif event.type == NEW_COMMAND:
                process_events(keyboard, last_idx)
                last_idx += 1

        current_time = pygame.time.get_ticks()
        for name in button_names:
            control_buttons[name].update(current_time)
        window.fill(BLACK, (window.get_width() // 2 + margin, 0, window.get_width() // 2, window.get_height())) # refresh only command buttons side
        draw_game_grid(window, line_width, margin)
        draw_board(board, window, x_img, o_img, margin)
        for name in button_names:
            control_buttons[name].draw(window)
        pygame.display.update()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        filename = f"output{datetime.now().strftime('-%d%m%Y-%H%M%S')}.txt"
    else:
        filename = sys.argv[1]
    main(filename)