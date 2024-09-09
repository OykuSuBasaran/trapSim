import pygame
import random
import math

# Pygame başlatma
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trap Atışı Simülasyonu")

# Renk tanımları
ORANGE = (237, 77, 22)
GREEN = (11, 127, 26)

# Plaka sınıfı
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

# Oyun döngüsü
clock = pygame.time.Clock()
running = True
plates = []  # Plakaları saklamak için bir liste

while running:
    screen.fill(GREEN)  # Ekranı temizle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Space tuşuna basıldığında yeni bir plaka oluştur
                angle = random.choice([10, 15, 20, 30, 40, 45])  # Rastgele bir açı seç
                direction = random.choice([-1, 1])  # Sağa (-1) veya sola (1) yön belirle
                angle *= direction  # Açının yönünü belirle
                new_plate = Plate(WIDTH // 2, HEIGHT, angle)  # Alt orta noktadan başlat
                plates.append(new_plate)  # Yeni plakayı listeye ekle

    # Her plakayı hareket ettir ve çiz
    for plate in plates:
        plate.move()
        plate.draw(screen)

    pygame.display.flip()  # Ekranı güncelle
    clock.tick(60)  # FPS ayarı

pygame.quit()
