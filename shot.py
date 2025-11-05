import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", center, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt