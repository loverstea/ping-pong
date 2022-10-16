from pygame import*
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__():
        pass
        
background=transform.scale(image.load("dyhastmish.jpg"),(700,500))
window = display.set_mode((700, 500))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y > 0:
            self.rect.x = self.rect.y - self.speed
        if keys[K_UP] and self.rect.y < 490:
            self.rect.x = self.rect.y + self.speed
run = True
clock = time.Clock()
finish  = False
FPS = 60
while run:
 
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))
        
        
        
        
    display.update()
    clock.tick(FPS)
