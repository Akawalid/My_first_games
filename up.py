
import pygame,random,math,time
pygame.init()
win = pygame.display.set_mode((1200,600))
pygame.display.set_caption("mon 3eme jeux")

def mygame():
    global stop_the_loop, xr, go, x, y, yr, counter, score
    stop_the_loop = True
    xr = 900
    yr = 40
    rectwidth = 40
    rectheight = []
    x = 600
    y = 300
    go = 0
    counter = 0
    score = 0
    white = (255,255,255 )
    font = pygame.font.SysFont("Agency_FB", 60)

    def setgame():
        for i in range(50):
            k = int(random.randrange(40,300))
            rectheight.append(k)

    def message(msg, color):
        messa = font.render(msg, True, color)
        win.blit(messa,(600,50))

        
    def drawrect ():
        global stop_the_loop,xr,go,x,y,yr,counter,score
        avance = math.ceil((1200-xr)/200)
        
        for i in range(avance):
            if xr + 200*i >= -30:
                pygame.draw.rect(win, (204, 163, 0), pygame.Rect(xr + 200*i, yr, rectwidth, rectheight[i]))
                pygame.draw.rect(win, (204, 163, 0), pygame.Rect(xr + 200*i, yr + 175 + rectheight[i], rectwidth, 560 - (yr + 175 + rectheight[i])))
                if (xr +200*i -30 < x <xr +40 + 200*i and (y <= rectheight[i] +yr or y>= yr+145+rectheight[i])) or y <= 40 or y >= 540:
                    
                    time.sleep(2)
                
                if go != 0:
                    e = (800 - xr) / 230
                    if score - math.floor(score) == 0:
                        score = int(e)
                        message(str(score),white)
                    xr -= 0.5
                else:
                    pass

        pygame.draw.rect(win, (204, 163, 0), pygame.Rect(x,int(y),30,30))
        if go != 0:
        
            y -= 10-counter
            counter += 1
            
        

        

    
    
    while stop_the_loop:
        pygame.time.delay(20)
        win.fill((255, 212, 48))
        for i in range(2):
            pygame.draw.rect(win, (204, 163, 0), pygame.Rect(0,i*560,1200,40))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            go = 1
            counter = 0
            
        setgame()
        drawrect()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_the_loop = False

    pygame.quit()
    quit()
mygame()

