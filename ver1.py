from typing import Any
from pygame import *

init()

info = display.Info()
window = display.set_mode((800, 800))
window_rect = window.get_rect()

game, finish = True, True
FPS = 60
clock = time.Clock()

background = transform.scale(image.load('background.jpg'), (info.current_w, info.current_h))


class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x, y, size_x, size_y):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(sprite_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, sprite_image, x, y, player_speed):
        GameSprite.__init__(self, sprite_image, x, y, 40, 40)

        self.speed = player_speed
        self.health = 3
        self.direction = None
    
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "LEFT"
            self.image = transform.scale(image.load('mc_left.jpg'), (40, 40))
        elif keys[K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "RIGHT"
            self.image = transform.scale(image.load('mc_right.jpg'), (40, 40))
        elif keys[K_DOWN]:
            self.rect.y += self.speed
            self.direction = "DOWN"
            self.image = transform.scale(image.load('mc_down.jpg'), (40, 40))
        elif keys[K_UP]:
            self.rect.y -= self.speed
            self.direction = "UP"
            self.image = transform.scale(image.load('mc_up.jpg'), (40, 40))


class Enemy(GameSprite):
    def __init__(self, sprite_image, x, y, enemy_speed):
        GameSprite.__init__(self, sprite_image, x, y, 50, 50)

        self.speed = enemy_speed
        self.direction = "DOWN"

    def update(self):
        if self.direction == "RIGHT":
            self.rect.x += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed   
        elif self.direction == "DOWN":
            self.rect.y += self.speed   
        elif self.direction == "UP":
            self.rect.y -= self.speed
            
    def change_direction(self):
        if self.direction == "LEFT":
            self.rect.x += self.speed
            self.direction = "UP"
        elif self.direction == "RIGHT":
            self.rect.x -= self.speed
            self.direction = "DOWN"
        elif self.direction == "DOWN":
            self.rect.y -= self.speed
            self.direction = "LEFT"
        elif self.direction == "UP":
            self.rect.y += self.speed
            self.direction = "RIGHT"



class Walls(GameSprite):
    def __init__(self, sprite_image, x, y, width, height):
        GameSprite.__init__(self, sprite_image, x, y, width, height)
        self.width = width
        self.height = height
        self.image = transform.scale(image.load('enemy.jpg'), (self.width, self.height))

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Player('mc_down.jpg', 5, 5, 5)
enemy_1 = Enemy('enemy.jpg', 570, 180, 5)
enemy_2 = Enemy('enemy.jpg', 180, 570, 5)
walls_group = sprite.Group()

#вертикальные стены начиная слева
#1
walls_group.add(Walls('enemy.jpg', 50, 50, 10, 420))
walls_group.add(Walls('enemy.jpg', 50, 520, 10, 230))
#2
walls_group.add(Walls('enemy.jpg', 110, 110, 10, 240))
walls_group.add(Walls('enemy.jpg', 110, 400, 10, 190))
walls_group.add(Walls('enemy.jpg', 110, 640, 10, 40))
#3
walls_group.add(Walls('enemy.jpg', 160, 740, 10, 60))#самая нижняя короткая

walls_group.add(Walls('enemy.jpg', 170, 170, 10, 460))

walls_group.add(Walls('enemy.jpg', 200, 0, 10, 60))#верхняя короткая

walls_group.add(Walls('enemy.jpg', 220, 680, 10, 60))

walls_group.add(Walls('enemy.jpg', 360, 120, 10, 60))

walls_group.add(Walls('enemy.jpg', 620, 170, 10, 260))
walls_group.add(Walls('enemy.jpg', 620, 490, 10, 130))

walls_group.add(Walls('enemy.jpg', 680, 60, 10, 160))
walls_group.add(Walls('enemy.jpg', 680, 270, 10, 470))

walls_group.add(Walls('enemy.jpg', 740, 60, 10, 60))
walls_group.add(Walls('enemy.jpg', 740, 170, 10, 360))
walls_group.add(Walls('enemy.jpg', 740, 580, 10, 170))
#горизонтальные стены
#1 слой
walls_group.add(Walls('enemy.jpg', 110, 50, 250, 10))
walls_group.add(Walls('enemy.jpg', 410, 50, 340, 10))
#2
walls_group.add(Walls('enemy.jpg', 110, 110, 580, 10))
#3
walls_group.add(Walls('enemy.jpg', 170, 170, 460, 10))
#4
walls_group.add(Walls('enemy.jpg', 60, 400, 60, 10))
walls_group.add(Walls('enemy.jpg', 680, 400, 60, 10))

walls_group.add(Walls('enemy.jpg', 120, 460, 60, 10))
walls_group.add(Walls('enemy.jpg', 740, 460, 60, 10))

walls_group.add(Walls('enemy.jpg', 170, 620, 460, 10))

walls_group.add(Walls('enemy.jpg', 110, 680, 250, 10))
walls_group.add(Walls('enemy.jpg', 410, 680, 270, 10))

walls_group.add(Walls('enemy.jpg', 60, 740, 500, 10))
walls_group.add(Walls('enemy.jpg', 610, 740, 140, 10))

#границы
walls_group.add(Walls('enemy.jpg', 0, 0, 5, 800))
walls_group.add(Walls('enemy.jpg', 795, 0, 5, 800))
walls_group.add(Walls('enemy.jpg', 0, 0, 800, 5))
walls_group.add(Walls('enemy.jpg', 0, 795, 740, 5))
#стена которая уберется после взятия ключа
end_wall = Walls('enemy.jpg', 740, 795, 60, 5)
walls_group.add(end_wall)
#квадрат внутри
walls_group.add(Walls('enemy.jpg', 230, 230, 340, 10))
walls_group.add(Walls('enemy.jpg', 230, 560, 340, 10))

walls_group.add(Walls('enemy.jpg', 230, 230, 10, 140))
walls_group.add(Walls('enemy.jpg', 230, 430, 10, 140))
walls_group.add(Walls('enemy.jpg', 560, 230, 10, 330))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish:
        window.blit(background, (0,0))
        player.update()
        enemy_1.update()
        enemy_2.update()

        walls_group.update()

        player.reset()
        enemy_1.reset()
        enemy_2.reset()

        if sprite.spritecollide(player, walls_group, False):
            if player.direction == "LEFT":
                player.rect.x += player.speed
            elif player.direction == "RIGHT":
                player.rect.x -= player.speed
            elif player.direction == "DOWN":
                player.rect.y -= player.speed
            elif player.direction == "UP":
                player.rect.y += player.speed
        
        if sprite.spritecollide(enemy_1, walls_group, False):
            enemy_1.change_direction()

        if sprite.spritecollide(enemy_2, walls_group, False):
            enemy_2.change_direction()
        
        if sprite.collide_rect(player, enemy_1) or sprite.collide_rect(player, enemy_2):
            player.health -= 1

        if player.health == 0:
            finish = False


    display.update()
    clock.tick(FPS)