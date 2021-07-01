import time

from pygame import *


def loadimg(img, wisota, wirina):
    return transform.scale(image.load(img), (wisota, wirina))


class Gamesprite(sprite.Sprite):
    def __init__(self, playerimg, playerx, playery, playerspeed, wisota, wirina):
        super().__init__()
        self.image = loadimg(playerimg, wisota, wirina)
        self.speed = playerspeed
        self.rect = self.image.get_rect()
        self.rect.x = playerx
        self.rect.y = playery

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Playr(Gamesprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < winwisota - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < winwisota - 80:
            self.rect.y += self.speed


bac = (255, 0, 0)
winwisota = 500
winwirina = 600
window = display.set_mode((winwirina, winwisota))
window.fill(bac)
game = True
stop = False
clock = time.Clock()
fps = 60
racket1 = Playr('racket.png', 30, 200, 4, 50, 150)
racket2 = Playr('racket.png', 520, 200, 4, 50, 150)
ball = Gamesprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speedx = 3
speedy = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not stop:
        window.fill(bac)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speedx
        ball.rect.y += speedy
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speedx *= -1
        if ball.rect.y > winwisota - 50 or ball.rect.y<0:
            speedy*=-1
        if ball.rect.x<0:
            stop=True
            window.blit(lose1,(200,200))
        if ball.rect.x>winwirina:
            stop=True
            window.blit(lose2,(200,200))
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(fps)
