from pygame import*
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__(self,p_image, p_x, p_y, p_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(width,height))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
background=transform.scale(image.load("dyhastmish.jpg"),(700,500))
window = display.set_mode((700, 500))
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if [K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_right(self):
        if [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if [K_s] and self.rect.y < 450:
            self.rect.y += self.speed
            
playeright =Player("stovp.png", 630, 200, 5, 40, 150)
playerleft =Player("stovp.png", 30, 200, 5, 40, 150)
ball = GameSprite("basketball-png-535126.png", 350, 200, 5, 40, 40)
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
        playerleft.reset()
        playeright.reset()
        ball.reset()
        playerleft.update_left()
        playeright.update_right()
        ball.update()
        
        
        
        
        
    display.update()
    clock.tick(FPS)
