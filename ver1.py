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

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed


class Enemy(GameSprite):
    def __init__(self, sprite_image, x, y, enemy_speed):
        GameSprite.__init__(self, sprite_image, x, y, 50, 50)

        self.speed = enemy_speed



class Walls(GameSprite):
    def __init__(self, sprite_image, x, y):
        GameSprite.__init__(self, sprite_image, x, y)


player = Player('player.jpg', 40, 40, 5)
enemy = Enemy('enemy.jpg', 200, 200, 3)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish:
        window.blit(background, (0,0))
        player.update()


        player.reset()
        enemy.reset()

        if sprite.collide_rect(player, enemy):
            finish = False

    display.update()
    clock.tick(FPS)