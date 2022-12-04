import pygame

class Pointer():

    def __init__(self, pos, start_time, delay):
        self.pos = pos
        self.delay = delay
        self.time = start_time
        self.pointer_w = 27
        self.pointer_h = 8
        self.pointer = pygame.image.load('./resources/pointer.png')
        self.counter = -1

    def draw(self, screen):
        screen.blit(self.pointer, self.pos)

    def update(self, current_time, window_w, window_h, btn_w, btn_h, gap):
        if current_time >= self.time:
            self.time = current_time + self.delay
            self.counter = (self.counter + 1) % 5
            match self.counter:
                case 0:
                    self.pos = (window_w/2-self.pointer_w/2, window_h/2-(btn_h*3/2+gap)-2*self.pointer_h)
                case 1:
                    self.pos = ((window_w/2+btn_w+gap)-self.pointer_w/2, (window_h/2-btn_h/2)-2*self.pointer_h)
                case 2:
                    self.pos = (window_w/2-self.pointer_w/2, window_h/2+(btn_h/2+gap)-2*self.pointer_h)
                case 3:
                    self.pos = (window_w/2-(btn_w+gap)-self.pointer_w/2, window_h/2-btn_h/2-2*self.pointer_h)
                case 4:
                    self.pos = (window_w/2-self.pointer_w/2, (window_h/2-btn_h/2)-2*self.pointer_h)