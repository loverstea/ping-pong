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
win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
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
            
playeright = Player ("kirt.png", 630, 200, 5, 100, 150)
playerleft = Player ("kirt.png", -30, 200, 5, 100, 150)
ball = GameSprite("is.png", 350, 200, 5, 50, 50)
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
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(playeright, ball) or sprite.collide_rect(playerleft, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            game_over = True
        if ball.rect.x > 650:
            finish = True
            game_over = True
        playerleft.update_left()
        playeright.update_right()
        ball.update()
        
        
        
        
        
    display.update()
    clock.tick(FPS)
