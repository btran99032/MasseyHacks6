from pygame import *
from pygame.mixer import *

from random import *


init()
mixer.init()
font.init()
size = [600,720] 
screen =display.set_mode(size)
display.set_caption("Covid-19 Questionaire")
running = True


def background():
    global backgrounds
    global level
    screen.blit(transform.scale(image.load("hackathon 2020/p2.png"),(600,720)),(0,0))


question = 1
point = 0
levels = 7
finish = 0
game = 0

def edges_rect(color,x,y,length,width):
    draw.rect(screen,color,(x,y,length,width))
    draw.rect(screen,(0,0,0),(x+3,y+3,length-6,width-6))

def collide_point(x,y,length,width,mx,my,mb):
    if x <= mx <= x+length:
        if y <= my <= y+width:
            if mb[0] == 1:
                print("hello")

            
def level(level,answer,mx,my,mb):
    global point
    global finish
    if mb[0] == 1:
        if 80 <= mx <= 520:
            if 250 <= my <= 300:
                if answer == "A":
                    point += 1
                    finish = 1
                else:
                    finish = 2
            if 350 <= my <= 400:
                if answer == "B":
                    point += 1
                    finish = 1
                else:
                    finish = 2
            if 450 <= my <= 500:
                if answer == "C":
                    point += 1
                    finish = 1
                else:
                    finish = 2
            if 550 <= my <= 600:
                if answer == "D":
                    point += 1
                    finish = 1
                else:
                    finish = 2

##while running:
##    for e in event.get():
##        if e.type == QUIT:
##            running = False
while running:
    mp=False
    for evnt in event.get():              
        if evnt.type == QUIT:
            running = False
        elif evnt.type==MOUSEBUTTONDOWN:
            if evnt.button==1:
                mp=True
    screen.fill((0,0,0))
    keys=key.get_pressed()
    mx,my=mouse.get_pos()
                
    nextlev = font.SysFont("timesnewroman",18)
    background()
            

    if finish == 1:
        screen.fill((0,255,0))
        x = ("press a different number")
        nextlevel = nextlev.render(x,True,(255,0,0))
        screen.blit(nextlevel,(100,620))
            
    elif finish == 2:
        screen.fill((255,0,0))
        x = ("press a different number")
        nextlevel = nextlev.render(x,True,(255,0,0))
        screen.blit(nextlevel,(100,620))

    keys = key.get_pressed()
    if keys:
        if keys[K_0] == 1:
            level(1,"C",mx,my,mb)
            game = 1
        if keys[K_1] == 1:
            level(2,"A",mx,my,mb)
            game = 2
        if keys[K_2] == 1:
            level(3,"B",mx,my,mb)
            game = 3  
        if keys[K_3] == 1:
            level(4,"D",mx,my,mb)
            game = 4
        if keys[K_4] == 1:
            level(5,"A",mx,my,mb)
            game = 5
        if keys[K_5] == 1:
            level(6,"D",mx,my,mb)
            game = 6
        if keys[K_6] == 1:
            level(7,"A",mx,my,mb)
            game = 7
        if keys[K_7] == 1:
            level(8,"D",mx,my,mb)
            game = 8
        if keys[K_8] == 1:
            level(9,"D",mx,my,mb)
            game = 9
        if keys[K_9] == 1:
            level(10,"A",mx,my,mb)
            game = 10
    edges_rect((150,150,255),80,100,440,100)
    edges_rect((150,255,150),80,250,440,50)
    edges_rect((150,255,150),80,350,440,50)
    edges_rect((150,255,150),80,450,440,50)
    edges_rect((150,255,150),80,550,440,50)

    

    if game == 1:
        question1 = nextlev.render("Where did Coronavirus originate?",True,(255,255,255))
        screen.blit(question1,(90,110))
        A1 = nextlev.render("A.Sudan",True,(255,255,255))
        screen.blit(A1,(90,260))
        B1 = nextlev.render("B.USA",True,(255,255,255))
        screen.blit(B1,(90,360))
        C1 = nextlev.render("C.China",True,(255,255,255))
        screen.blit(C1,(90,460))
        D1 = nextlev.render("D.Canada",True,(255,255,255))
        screen.blit(D1,(90,560))
    if game == 2:
        question2 = nextlev.render("What should you do if you are too close to someone?",True,(255,255,255))
        screen.blit(question2,(90,110))
        A2 = nextlev.render("A.walk away",True,(255,255,255))
        screen.blit(A2,(90,260))
        B2 = nextlev.render("B.stay still and wait",True,(255,255,255))
        screen.blit(B2,(90,360))
        C2 = nextlev.render("C.cough and preten you have covid-19",True,(255,255,255))
        screen.blit(C2,(90,460))
        D2 = nextlev.render("D.none of the above",True,(255,255,255))
        screen.blit(D2,(90,560))
    if game == 3:
        question3 = nextlev.render("As of 2020-05-30, how many cases are there?",True,(255,255,255))
        screen.blit(question3,(90,110))
        A3 = nextlev.render("A.1000000",True,(255,255,255))
        screen.blit(A3,(90,260))
        B3 = nextlev.render("B.6000000",True,(255,255,255))#
        screen.blit(B3,(90,360))
        C3 = nextlev.render("C.10000000",True,(255,255,255))
        screen.blit(C3,(90,460))
        D3 = nextlev.render("D.3000000",True,(255,255,255))
        screen.blit(D3,(90,560))
    if game == 4:
        question4 = nextlev.render("What should you do if you think you have it?",True,(255,255,255))
        screen.blit(question4,(90,110))
        A4 = nextlev.render("A.inform people",True,(255,255,255))
        screen.blit(A4,(90,260))
        B4 = nextlev.render("B.visit the hospital",True,(255,255,255))
        screen.blit(B4,(90,360))
        C4 = nextlev.render("C.self isolate",True,(255,255,255))
        screen.blit(C4,(90,460))
        D4 = nextlev.render("D.all of the above",True,(255,255,255))#
        screen.blit(D4,(90,560))
    if game == 5:
        question5 = nextlev.render("The country with the most cases as of May 30th, 2020 is? ",True,(255,255,255))
        screen.blit(question5,(90,110))
        A5 = nextlev.render("A.USA",True,(255,255,255))#
        screen.blit(A5,(90,260))
        B5 = nextlev.render("B.China",True,(255,255,255))
        screen.blit(B5,(90,360))
        C5 = nextlev.render("C.Italy",True,(255,255,255))
        screen.blit(C5,(90,460))
        D5 = nextlev.render("D.Canada",True,(255,255,255))
        screen.blit(D5,(90,560))
    if game == 6:
        question6 = nextlev.render("What is NOT a covid-19 tip?",True,(255,255,255))
        screen.blit(question6,(90,110))
        A6 = nextlev.render("A.stay home",True,(255,255,255))
        screen.blit(A6,(90,260))
        B6 = nextlev.render("B.keep a safe distance",True,(255,255,255))
        screen.blit(B6,(90,360))
        C6 = nextlev.render("C.wash your hands often",True,(255,255,255))
        screen.blit(C6,(90,460))
        D6 = nextlev.render("D.go out when you feel ill",True,(255,255,255))#
        screen.blit(D6,(90,560))
    if game == 7:
        question7 = nextlev.render("What should you do during this pandemic?",True,(255,255,255))
        screen.blit(question7,(90,110))
        A7 = nextlev.render("A.Do some social distance excercises",True,(255,255,255))#
        screen.blit(A7,(90,260))
        B7 = nextlev.render("B.Play League of Legends all day long",True,(255,255,255))
        screen.blit(B7,(90,360))
        C7 = nextlev.render("C.Go to highly crowded areas",True,(255,255,255))
        screen.blit(C7,(90,460))
        D7 = nextlev.render("D.Go traveling",True,(255,255,255))
        screen.blit(D7,(90,560))
    if game == 8:
        question8 = nextlev.render("How long should you wash your hands for?",True,(255,255,255))
        screen.blit(question8,(90,110))
        A8 = nextlev.render("A.5 seconds",True,(255,255,255))
        screen.blit(A8,(90,260))
        B8 = nextlev.render("B.10 seconds",True,(255,255,255))
        screen.blit(B8,(90,360))
        C8 = nextlev.render("C.15 seconds",True,(255,255,255))
        screen.blit(C8,(90,460))
        D8 = nextlev.render("D.20+ seconds",True,(255,255,255))#
        screen.blit(D8,(90,560))
    if game == 9:
        question9 = nextlev.render("How can you prevent coronavirus?",True,(255,255,255))
        screen.blit(question9,(90,110))
        A9 = nextlev.render("A.go outside",True,(255,255,255))
        screen.blit(A9,(90,260))
        B9 = nextlev.render("B.excercize",True,(255,255,255))
        screen.blit(B9,(90,360))
        C9 = nextlev.render("C.eat healthy",True,(255,255,255))
        screen.blit(C9,(90,460))
        D9 = nextlev.render("D. B and C",True,(255,255,255))#
        screen.blit(D9,(90,560))
    if game ==10:
        question10 = nextlev.render("You can have coronavirus and not have any symptoms ",True,(255,255,255))
        screen.blit(question10,(90,110))
        A10 = nextlev.render("A.True",True,(255,255,255))#
        screen.blit(A10,(90,260))
        B10 = nextlev.render("B.False",True,(255,255,255))
        screen.blit(B10,(90,360))
        C10 = nextlev.render("C.Error",True,(255,255,255))
        screen.blit(C10,(90,460))
        D10 = nextlev.render("D. Error",True,(255,255,255))
        screen.blit(D10,(90,560))

     
    display.flip()
    display.update()
quit()
