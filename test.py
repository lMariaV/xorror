import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров игрового окна
width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Хоррор")

# Загрузка изображения игрока и приведение его размеров
player_image = pygame.image.load("player.jpg")
player_image = pygame.transform.scale(player_image, (50, 50))
player_rect = player_image.get_rect()

# Загрузка изображения монстра и приведение его размеров
monster_image = pygame.image.load("enemy.jpg")
monster_image = pygame.transform.scale(monster_image, (50, 50))
monster_rect = monster_image.get_rect()

# Установка начальных координат игрока и монстра
player_rect.x = width // 2
player_rect.y = height // 2
monster_rect.x = random.randint(0, width - monster_rect.width)
monster_rect.y = random.randint(0, height - monster_rect.height)

# Установка скорости игрока и монстра
player_speed = 5
monster_speed = 0

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка движения игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Обработка движения монстра в сторону игрока
    if monster_rect.x < player_rect.x:
        monster_rect.x += monster_speed
    elif monster_rect.x > player_rect.x:
        monster_rect.x -= monster_speed
    if monster_rect.y < player_rect.y:
        monster_rect.y += monster_speed
    elif monster_rect.y > player_rect.y:
        monster_rect.y -= monster_speed

    # Ограничение выхода за границы окна
    if player_rect.x < 0:
        player_rect.x = 0
    if player_rect.x > width - player_rect.width:
        player_rect.x = width - player_rect.width
    if player_rect.y < 0:
        player_rect.y = 0
    if player_rect.y > height - player_rect.height:
        player_rect.y = height - player_rect.height

    # Проверка на столкновение игрока с монстром
    if player_rect.colliderect(monster_rect):
        print("Game Over")
        running = False

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Отрисовка игрока и монстра
    screen.blit(player_image, player_rect)
    screen.blit(monster_image, monster_rect)

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
