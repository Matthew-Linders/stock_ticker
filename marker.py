import pygame
import resource

class Marker:
    resources = [""]
    def __inti__(self, name):
        self.name = name
        self.value = 0

    def begin(self, surface, resource):
        pygame.draw.circle(surface, resource.colour, resource.center, 4)