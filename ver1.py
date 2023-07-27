from typing import Any
from pygame import *

window = display.set_mode((800, 800))

game, finish = True, True
FPS = 60
clock = time.Clock()

background = transform.scale(image.load('background.jpg'), (800,800))

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
        GameSprite.__init__(self, sprite_image, x, y, 50, 50)

        self.speed = player_speed
        self.health = 3
        self.direction = None

    def update(self):
        #сделать проверку направления движения вверх + влево вправо + вверх и тп
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "LEFT"
        elif keys[K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "RIGHT"
        elif keys[K_DOWN]:
            self.rect.y += self.speed
            self.direction = "DOWN"
        elif keys[K_UP]:
            self.rect.y -= self.speed
            self.direction = "UP"


class Enemy(GameSprite):
    def __init__(self, sprite_image, x, y, enemy_speed):
        GameSprite.__init__(self, sprite_image, x, y, 50, 50)

        self.speed_x = enemy_speed
        self.speed_y = enemy_speed
        self.direction = None
        self.direction_list = []
        self.index = 0
    
    def update(self):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed_x
            self.direction = "RIGHT"
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed_x
            self.direction = "LEFT"
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed_y
            self.direction = "DOWN"
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed_y
            self.direction = "DOWN"



class Walls(GameSprite):
    def __init__(self, sprite_image, x, y, width, height):
        GameSprite.__init__(self, sprite_image, x, y, width, height)
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Player('player.jpg', 40, 40, 5)
enemy = Enemy('enemy.jpg', 800, 800, 1)

wall_1 = Walls('enemy.jpg', 500, 500, 60, 100)
walls_group = sprite.Group()
walls_group.add(wall_1)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        '''if e.type == KEYDOWN:
            if key == K_  '''      
    if finish:
        window.blit(background, (0,0))
        player.update()
        enemy.update()
        wall_1.draw_wall()

        player.reset()
        enemy.reset()


        if sprite.spritecollide(player, walls_group, False):
            if player.direction == "LEFT":
                player.rect.x += player.speed
            elif player.direction == "RIGHT":
                player.rect.x -= player.speed
            elif player.direction == "DOWN":
                player.rect.y -= player.speed
            elif player.direction == "UP":
                player.rect.y += player.speed
        
        if sprite.spritecollide(enemy, walls_group, False):
            if enemy.direction == "LEFT":
                enemy.rect.x += enemy.speed_x
                enemy.speed_x += enemy.speed_y
                enemy.speed_y = enemy.speed_x - enemy.speed_y
                enemy.speed_x -= enemy.speed_y
            elif enemy.direction == "RIGHT":
                enemy.rect.x -= enemy.speed_x
            elif enemy.direction == "DOWN":
                enemy.rect.y -= enemy.speed_y
            elif enemy.direction == "UP":
                enemy.rect.y += enemy.speed_y



        if sprite.collide_rect(player, enemy):
            player.health -= 1

        if player.health == 0:
            finish = False


    display.update()
    clock.tick(FPS)