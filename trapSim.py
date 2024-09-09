import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trap Atışı Simülasyonu")


ORANGE = (237, 77, 22)
GREEN = (11, 127, 26)

# Plak sınıfı
class Plate:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 5  # Hareket hızı

    def move(self):
        # Açıya göre x ve y hareket miktarları hesabı
        radian_angle = math.radians(self.angle)
        self.x += self.speed * math.cos(radian_angle) * (-1 if self.angle < 0 else 1) #x ekseninde hareket
        self.y -= self.speed * abs(math.sin(radian_angle))#y ekseninde hareket


    def draw(self, screen):
        pygame.draw.rect(screen, ORANGE, (self.x, self.y, 20, 10))  # 20x10 boyutunda turuncu plaka

# Oyun döngüsü
clock = pygame.time.Clock()
running = True
plates = []  # Plakların listesi

while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Space tuşuna basıldığında yeni bir plak
                angle = random.choice([10, 15, 20, 30, 40, 45])  # Rastgele bir açı seç
                direction = random.choice([-1, 1])  # Sağa (-1) veya sola (1) yön belirle
                angle *= direction  # Açının yönünü belirle
                new_plate = Plate(WIDTH // 2, HEIGHT, angle)  # Alt orta noktadan başlat
                plates.append(new_plate)  # Yeni plağı listeye ekle

    # Plak hareketi ve çizimi
    for plate in plates:
        plate.move()
        plate.draw(screen)

    pygame.display.flip()  # Ekran güncellemesi
    clock.tick(60)  # FPS

pygame.quit()
