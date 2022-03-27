from pygame import *
window = display.set_mode((700,500))
display.set_caption('Pingpong')
FPS =60
clock = time.Clock()
background = transform.scale(image.load('123.jpg'),(700,500))
speed_x = 3
speed_y = 3
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed,width=65,height=65):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image),(width, height))
        self.speed = sprite_speed
        self.rect =self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and  self.rect.x > 5:
            self.rect.x -= 10
        if keys_pressed[K_d] and  self.rect.x < 630:
            self.rect.x += 10
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and  self.rect.x > 5:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT] and  self.rect.x < 630:
            self.rect.x += 10
class Ball(GameSprite):
    pass
font.init()
font = font.SysFont('Arial',27)
sprite1 = Player(('bullet.png'),25,25,10)
sprite2 = Player(('bullet.png'),430,400,10)
sprite3 = Ball(('asteroid.png'),100,400,10)
win = font.render('YOU WIN!', True, (0,250,0))
lose = font.render('YOU LOSE!', True, (225,0,0))
run = True
finish = False
while run:
    window.blit(background,(0,0))
    sprite1.update()
    sprite1.reset()
    sprite2.update1()
    sprite2.reset()
    sprite3.update()
    sprite3.reset()
    if sprite.collide_rect(sprite1,sprite3) or sprite.collide_rect(sprite2,sprite3):
        speed_y *= -1
    if sprite3.rect.x <= 0:
        speed_x *= -1
    if sprite3.rect.x <= 630:
        speed_x *= -1












    for e in event.get():
        if e.type == QUIT:
            run = False
        
    clock.tick(FPS)
    display.update()