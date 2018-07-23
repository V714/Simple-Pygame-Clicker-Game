import random as r
import pygame

class Circle(object):
    def __init__(self,x,y,vel):
        self.x=x
        self.y=y
        self.width=0
        self.height=0
        self.rad=0
        self.vel=vel
        self.time=3
        self.clock=0
    def grow(self):
        self.rad+=self.vel


x=360 #Screen width
y=640 #Screen Height

pygame.font.init()
pygame.init()
wnd = pygame.display.set_mode((x,y))
pygame.display.set_caption("Aim Training")

run = True
rep=True

def game_menu():  
    run = True
    fnt = pygame.font.get_default_font()
    font = pygame.font.SysFont(fnt, 40)
    text_color=(20,20,20)
    while run:
        pygame.time.delay(3)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx>x/2-30 and mx<x/2+100 and my>y/2-20 and my<y/2+40:
                    text_color=(0,180,180)
            if e.type == pygame.MOUSEBUTTONUP:
                text_color=(20,20,20)
                if mx>x/2-30 and mx<x/2+100 and my>y/2-20 and my<y/2+40:
                    run = False
        wnd.fill((200,200,200))
        menu_text = font.render("Start",True,text_color)
        wnd.blit(menu_text,(x/2-30,y/2-20))
        
        pygame.display.update()

def game_loop():   
    run = True  
    fnt = pygame.font.get_default_font()
    font = pygame.font.SysFont(fnt, 40)
    cirs=[]
    time_count=0
    faster=1
    snds=0
    text_color=(50,50,50)
    game_over=False
    width =10
    height =10
    vel =0.1
    drag=False
    pts=0
    clock=pygame.time.Clock()
    
    while run:
        dt = clock.tick()
        if pts>10:
            faster=1+pts/10
        pygame.time.delay(3)
        time_count+=faster/3
        if time_count>200:
            time_count=0
            cirs.append(Circle(r.randint(1,x),r.randint(1,y),(r.randint(1,2)/10)))
        if cirs and not game_over:
            for obj in cirs:
                obj.grow()
                obj.clock += dt
                if obj.clock > 1000:
                   obj.time-=1 
                   if obj.time==0:
                       game_over=True
                   obj.clock =0
        mx, my = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.MOUSEBUTTONDOWN and cirs and not game_over:
                for obj in cirs:
                    if mx>obj.x-obj.rad and mx<obj.x+obj.rad and my>obj.y-obj.rad and my<obj.y+obj.rad:
                        cirs.remove(obj)
                        pts+=1
                        time_count=200
            if e.type == pygame.MOUSEBUTTONDOWN and game_over:
                if mx>x/2-45 and mx<x/2+70 and my>y/2+140 and my<y/2+180:
                    text_color=(0,200,200)
            if e.type == pygame.MOUSEBUTTONUP and game_over:
                text_color=(50,50,50)
                if mx>x/2-45 and mx<x/2+70 and my>y/2+140 and my<y/2+180:
                    run = False
        wnd.fill((230,230,230))
        if cirs:
            for obj in cirs:
                pygame.draw.circle(wnd,(250,50,90),(obj.x,obj.y),int(obj.rad),0)  
                time_left_font= pygame.font.SysFont(fnt,int(obj.rad))
                time_left_text= time_left_font.render("{:d}".format(int(obj.time)), True,(180,30,70))
                wnd.blit(time_left_text,(obj.x-(obj.rad/6),obj.y-(obj.rad/4)))
        text = font.render("Score: {:d}".format(pts), True, (21, 221, 230))
        if not game_over:
            wnd.blit(text,((x/2)-50,y-50))
        else: 
            text2=font.render("Game Over",True,(80,80,80))
            text_re=font.render("Retry",True,text_color)
            wnd.blit(text2,((x/2)-70,y/2+10))
            wnd.blit(text,((x/2)-55,y/2+60))
            wnd.blit(text_re,(x/2-40,y/2+140))
        pygame.display.update()

game_menu()
while rep:
    game_loop()
pygame.quit()
