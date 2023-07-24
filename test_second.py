import pygame

# Инициализация Pygame
pygame.init()

# Создание окна
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Загрузка изображений
player_image = pygame.image.load('player.jpg').convert_alpha()
wall_image = pygame.image.load('player.jpg').convert_alpha()
exit_image = pygame.image.load('enemy.jpg').convert_alpha()

# Задание размеров блока
block_size = 32

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)

# Определение игровых объектов
player = pygame.Rect(50, 50, block_size, block_size)
exit_rect = pygame.Rect(704, 512, block_size, block_size)
walls = [pygame.Rect(160, 0, block_size, 224), pygame.Rect(96, 288, block_size * 3, block_size * 3),
         pygame.Rect(224, 288, block_size * 3, block_size * 3), pygame.Rect(96, 480, block_size * 4, block_size),
         pygame.Rect(448, 32, block_size, block_size * 6), pygame.Rect(512, 128, block_size * 7, block_size),
         pygame.Rect(320, 320, block_size * 5, block_size), pygame.Rect(576, 256, block_size, block_size * 7),
         pygame.Rect(576, 480, block_size * 3, block_size)]

# Определение переменных игры
player_speed = 4
movement = [0, 0]
game_over = False

# Основной игровой цикл
while not game_over:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movement[1] = -player_speed
            elif event.key == pygame.K_DOWN:
                movement[1] = player_speed
            elif event.key == pygame.K_LEFT:
                movement[0] = -player_speed
            elif event.key == pygame.K_RIGHT:
                movement[0] = player_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                movement[1] = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement[0] = 0

    # Обновление координат персонажа
    player.x += movement[0]
    player.y += movement[1]

    # Проверка столкновений и перемещение в случае столкновения со стеной
    for wall in walls:
        if player.colliderect(wall):
            if movement[0] > 0:
                player.right = wall.left
            elif movement[0] < 0:
                player.left = wall.right
            elif movement[1] > 0:
                player.bottom = wall.top
            elif movement[1] < 0:
                player.top = wall.bottom

    # Ограничение видимости персонажа
    if player.x < block_size:
        player.x = block_size
    elif player.x > window_width - block_size * 2:
        player.x = window_width - block_size * 2
    if player.y < block_size:
        player.y = block_size
    elif player.y > window_height - block_size * 2:
        player.y = window_height - block_size * 2

    # Отрисовка игрового поля
    window.fill(black)
    pygame.draw.rect(window, white, player)
    pygame.draw.rect(window, white, exit_rect)
    for wall in walls:
        pygame.draw.rect(window, white, wall)
    pygame.display.update()

    # Проверка условия победы
    if player.colliderect(exit_rect):
        game_over = True

# Завершение игры
pygame.quit()
