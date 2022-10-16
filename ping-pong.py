from pygame import*
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
background=transform.scale(image.load("dyhastmish.jpg"),(700,500))
window = display.set_mode((700, 500))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y > 0:
            self.rect.x = self.rect.y - self.speed
        if keys[K_UP] and self.rect.y < 490:
            self.rect.x = self.rect.y + self.speed

ball = 

FPS = 60


display.update()
clock.tick(FPS)
