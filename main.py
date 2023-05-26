import random
import pygame
from sys import exit
l=False
r=False
a=50
b=370
u=False
d=False
jump=False
score=0
fall=False
k=0
vilocity=4
pygame.init()
ls=[]
ly=[]
for i in range(1,1000):
    y=random.randint(100,400)
    t=random.randint(100,400)
    ls.append(y)
    ly.append(t)
print(pygame.font.get_fonts)
font=pygame.font.Font("assets/neon_pixel-7.ttf",50)
text=font.render("hello world",False,"Green")
screen=pygame.display.set_mode((1000,600))
scrrect=screen.get_rect()
pygame.display.set_caption("runner")
sky=pygame.Surface((2000,600))
font=pygame.font.Font("assets/he.ttf",50)
sky.fill("SkyBlue")
surface3=pygame.Surface((1000,200))
surface3.fill("Brown")
clock=pygame.time.Clock()
surface4=pygame.Surface((1000,100))
surface4.fill("Green")
pillerbottom=pygame.image.load("assets/pill1.png")
pillerbottom=pygame.transform.scale(pillerbottom,(100,400))
birdflapp=pygame.image.load("assets/bird2.png")
px=60
py=50
birdflapp=pygame.transform.scale(birdflapp,(px,py))
birdnormal=pygame.image.load("assets/bird1.png")
birdnormal=pygame.transform.scale(birdnormal,(px,py))
pillertop=pygame.image.load("assets/pill2.png")
pillertop=pygame.transform.scale(pillertop,(100,400))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if(event.key==pygame.K_a):
                l=True
            if(event.key==pygame.K_d):
                r=True
            if(event.key==pygame.K_w):
                u=True
            if(event.key==pygame.K_s):
                d=True
            if(event.key==pygame.K_SPACE):
                jump=True
                fall=False
                vilocity=20
                ty=b
        if event.type==pygame.KEYUP:
            if(event.key==pygame.K_a):
                l=False
            if(event.key==pygame.K_d):
                r=False
            if(event.key==pygame.K_w):
                u=False
            if(event.key==pygame.K_s):
                d=False
    screen.blit(sky,(0,0))
    screen.blit(surface3,(0,540))
    screen.blit(surface4,(0,540))
    text=font.render(str(int(score-1)),False,"Black")
    for i in range(1,len(ls)-1):
        rec1=pillerbottom.get_rect(topleft=(k+i*500,ls[i]+100))
        screen.blit(pillerbottom,(rec1))
        rec2=pillertop.get_rect(topleft=(k+i*500,ls[i]-100-400))
        screen.blit(pillertop,rec2)

    rec3=birdnormal.get_rect(topleft=(a,b))
    rec4=birdflapp.get_rect(topleft=(a,b))
    screen.blit(text,(800,0))
    if(jump):
        screen.blit(birdflapp,rec4)
    else:
        screen.blit(birdnormal,rec3)
    if(jump):
        if(b>ty-60):
            b-=vilocity
            vilocity-=.1
        else:
            jump=False
            ky=k
            fall=True
            vilocity=4
    if(fall):
        if(ky>k+10000):
            pass
        else:
            b+=vilocity
            vilocity+=.2
    if(k%508==0):
        score+=1
    rec1=pillerbottom.get_rect(topleft=(k+score*500,ls[score]+100))
    rec2=pillertop.get_rect(topleft=(k+score*500,ls[score]-100-400))
    if(rec1.colliderect(rec3) or rec1.colliderect(rec4) or rec2.colliderect(rec3) or rec2.colliderect(rec4)):
        break 
    if(scrrect.colliderect(rec3) or scrrect.colliderect(rec4)):
        pass
    else:
        break
    if(l):
        if a>0:
            a-=6
    if(r):
        if a<1000:
            a+=6
    if(u):
        if b>0:
            b-=6
    if(d):
        if b<600:
            b+=6
    pygame.display.update()
    k-=4
    clock.tick(30)