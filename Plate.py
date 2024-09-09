import math
import pygame

ORANGE = (237, 77, 22)
class Plate:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 5  # Hareket hızı

    def move(self):
        # Açıya göre x ve y hareket miktarlarını hesapla
        radian_angle = math.radians(self.angle)
        direction1 = -1 if self.angle < 0 else 1
        self.x += direction1 * self.speed * math.cos(radian_angle)
        self.y -= self.speed * abs(math.sin(radian_angle))# Y ekseni ters


    def draw(self, screen):
        pygame.draw.rect(screen, ORANGE, (self.x, self.y, 20, 10))  # 20x20 boyutunda turuncu plaka