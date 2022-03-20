from pygame import *
from random import randint
from time import time as timer
window = display.set_mode((700,500))
display.set_caption('Pingpong')
clock = time.Clock()
FPS =60
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
    def fire(self):
        bullets.add(Bullet('bullet.png',self.rect.centerx,self.rect.top,10,10,10))

font.init()
font1 = font.SysFont('Arial',27)

win = font.render('YOU WIN!', True, (0,250,0))
lose = font.render('YOU LOSE!', True, (225,0,0))
wait = font.render('Wait,reload...', True, (225,0,0))
run = True
finish = False
while run:
    if finish != True:
        window.blit(background,(0,0))
        monsters.update()
        monsters.draw(window)
        sprite1.update()
        sprite1.reset()
        bullets.update()
        bullets.draw(window)
        if sprite.groupcollide(monsters, bullets, True, True):
            sbito +=1
            monsters.add(Enemy('ufo.png ',randint(50,645),0,3))
        txt2 = font1.render('Пропущено:' + str(lost),1,(150,0,225))
        txt = font1.render('Счет:' + str(sbito),1,(150,0,225))
        txt3 = font1.render('Оставшиеся пули:' + str(num_fire),1,(150,0,225))
        txt4 = font1.render('Оставшиеся жизни:' + str(health),1,(150,0,225))
        window.blit(txt,(0,30))
        window.blit(txt2,(0,0))
        window.blit(txt3,(0,60))
        window.blit(txt4,(0,90))
        if sprite.groupcollide(players,monsters, False, True):
            health -= 1
            if health == 0:
                window.blit(lose, (300,200))
                finish = True
        if rel_time == True:
            time1 = timer()
            if time1 - time_start <  3:
                window.blit(wait, (300,200))
            else:
                num_fire = 5
                rel_time = False
        if lost >= 3:
            window.blit(lose, (300,200))
            finish = True
        if sbito >= 10:
            window.blit(win, (300,200))
            finish = True
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire <= 5:
                    sprite1.fire()
                    num_fire -= 1
                if num_fire == 0:
                    rel_time = True
                    time_start = timer()
        
    clock.tick(FPS)
    display.update()