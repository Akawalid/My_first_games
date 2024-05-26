import pygame, random, math, time
pygame.init()

class out:
    def quite(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.gamel = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
obj = out()
obj.run = True
obj.gamel = True
hscore = 0
def gameloop():
    
    swidth = 500
    sheigth = 500
    win = pygame.display.set_mode((730,525))
    pygame.display.set_caption("mon premier jeux")

    x = 50
    y = 50
    radius = 8
    vel = 4
    x1 = 260
    y1 = 250
    k = 0
    calrec = 0
    seqx=[0]*1
    seqy=[0]*1
    mo = 0
    tim = 40
    tr = True
    tl = True
    tu = True
    td = True
    gameover = pygame.image.load("wow.png")
    background = pygame.image.load("abc.jpg")
    global hscore
    score = 0
    font = pygame.font.SysFont(None, 30)
    white = (150,150,150)

    def draw():

        
        def message(msg,food,hmsg,color):
            mesg = font.render(msg,True,color)
            fod = font.render(food,True,color)
            hsr = font.render(hmsg,True,color)
            win.blit(mesg,(615,210))
            win.blit(fod,(612,268))
            win.blit(hsr,(648,153))

        win.blit(background, (0,0))
        message(str(calrec*5),str(calrec),str(hscore),white)
        pygame.draw.circle(win, (194, 0, 8), (x, y), radius)
        pygame.draw.circle(win, ( 0, 0, 0), (x1, y1), radius)
        f = 1
        for i in range(calrec):
            f += 4
            pygame.draw.circle(win, (194, 0, 8), (seqx[k-f+1],seqy[k-f+1]), radius)
                    
            if seqx[k-f+1] - radius < x <seqx[k-f+1]+radius and  seqy[k-f+1] - radius<y <seqy[k-f+1] + radius :
                time.sleep(2)
                while obj.gamel  :
                    win.fill((0,0,0))
                    win.blit(gameover, (252,147))
                    pygame.display.update()
                    obj.quite()
                            
        pygame.display.update()


 
    while obj.run:
        pygame.time.delay(tim)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                obj.run = False


        keys = pygame.key.get_pressed()

        if mo == 1 or keys[pygame.K_LEFT] and tl == True:
            if x <= 10+ radius:
                    x = swidth + 10 - radius 
            else:
                x -= vel
            mo = 1
            tr = False
            tu = True
            td = True
        
        if mo == 2 or keys[pygame.K_RIGHT] and tr == True :
            if x >= swidth + 10 - radius:
                x = radius + 10
            else:
                x += vel
            mo = 2
            tl = False
            tu = True
            td = True

        if mo == 3 or keys[pygame.K_UP] and tu == True:
            if y <= radius + 10:
                y = sheigth + 10 - radius 
            else:
                y -= vel
            mo = 3
            tl = True
            tr = True
            td = False

        if mo == 4 or keys[pygame.K_DOWN] and td == True:
            if y >= sheigth + 10 -radius:
                y = radius +10
            else:
                y += vel
            mo = 4
            tl = True
            tr = True
            tu = False

        seqx.append(x)
        seqy.append(y)
        length = math.sqrt(math.pow(x - x1, 2) + math.pow(y - y1,2))
          
        if length < 2*radius:
            x1 = random.randrange(20,swidth + 10 - radius)
            y1 = random.randrange(20,sheigth + 10 - radius)
            if hscore == calrec*5:
                hscore += 5
            else:
                pass
            calrec += 1
            if calrec > 3 and calrec%2 == 0 and tim >=30:
                tim -= 2
            
        k += 1
        draw()
 
    pygame.quit()
    quit()


gameloop()              


