import pygame

class Rectangle():

    def __init__(self, color, rect, start_time, delay):
        self.color = color
        self.rect = rect
        self.time = start_time
        self.delay = delay
        self.show = False

    def draw(self, screen):
        if self.show:
            pygame.draw.rect(screen, self.color, self.rect)

    def update(self, current_time):
        if current_time >= self.time:
             self.time = current_time + self.delay
             self.show = not self.show