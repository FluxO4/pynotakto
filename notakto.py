import pygame


class board:
    def __init__(theboard, numrows, numcols, numline, posx, posy):
        theboard.active = True
        theboard.items = []
        for i in range(numrows):
            theboard.items.append([])
            for ii in range(numcols):
                theboard.items[i].append(False)
        
        theboard.posx = posx
        theboard.posy = posy
        theboard.numrows = numrows
        theboard.numcols = numcols
        theboard.numline = min(numline, numrows, numcols)

	
	
    def clear(theboard):
        for i in items:
            for ii in i:
                ii = False

    def play(theboard, r, c):
        if(theboard.items[r][c] ==  False):
            theboard.items[r][c] = True
            theboard.checkstab()
            return True
        return False
        pass
	
    def checkstab(theboard):
        if(max([sum(y) for y in theboard.items]) >= theboard.numline
           
                or max([sum([y[i] for y in theboard.items]) for i in range(theboard.numcols)]) >= theboard.numline
           
                or max([sum([theboard.items[i + k][ii + k] for k in range(theboard.numline)])
                for i in range(1 + theboard.numrows - theboard.numline)
                for ii in range(1 + theboard.numcols - theboard.numline)
                ]) >= theboard.numline
           
                or max([sum([theboard.items[i + k][ii - k] for k in range(theboard.numline)])
                for i in range(1 + theboard.numrows - theboard.numline)
                for ii in range(theboard.numcols - 1, theboard.numline - 2, -1)
                ]) >= theboard.numline
            ):
            theboard.active = False
    
	
	
    def drawWhat(theboard, item):
        if(item == True):
            return "X"
        return " "

    def worldtolocalcoords(theboard, worldx, worldy, alsoplay):
        x = worldx - theboard.posx
        y = worldy - theboard.posy
        rx, ry = -1,-1

        x = x // (boxsize + linethickness)
        y = y // (boxsize + linethickness)

        if(x >= 0 and x <= theboard.numrows-1):
            rx = x
        if(y >= 0 and y <= theboard.numcols-1):
            ry = y


        if alsoplay and rx != -1 and ry != -1:
            theboard.play(rx,ry)
        return rx, ry
        pass
	
    def draw(theboard, scr):
        linecolor = (255,255,255)
        blippcolour = blipcolour
        
        if(not theboard.active):
            linecolor = (100,100,100)
            blippcolour = (80,80,80)

        for i in range(theboard.numrows - 1):
            pygame.draw.rect(scr,linecolor,[boxsize*(i+1) + linethickness*(i) + theboard.posx,
                                                theboard.posy,
                                                linethickness,
                                                boxsize*(theboard.numcols) + linethickness*(theboard.numcols-1)]) #[xcoord, ycoord, width, height]
                        
        for i in range(theboard.numcols -1):
            pygame.draw.rect(scr,linecolor,[theboard.posx,
                                                boxsize*(i+1) + linethickness*(i) + theboard.posy,
                                                boxsize*(theboard.numrows) + linethickness*(theboard.numrows-1),
                                                linethickness]) #[xcoord, ycoord, width, height]
                        


        for i in range(theboard.numrows):
            for ii in range(theboard.numcols):
                if(theboard.items[i][ii] == True):
                     pygame.draw.rect(scr,blippcolour,[boxsize*(i) + linethickness*(i) + theboard.posx,
                                        boxsize*(ii) + linethickness*(ii) + theboard.posy,
                                        boxsize,
                                        boxsize]) #[xcoord, ycoord, width, height]

        




#START
black = (0, 0, 0)
boxsize = 50
linethickness = 5
blipcolour = (255,0,0)
players = ["Player 1", "Player 2"]
hhs = [board(3,3,3, 20,0), board(4,3,3,20,0), board(5,4,4,20,0)]
for i in range(len(hhs)):
    if(True):
        hhs[i].posy = (sum([hh.numcols for hh in hhs[:i]])* (boxsize + 2*linethickness))
    hhs[i].posy += 20
    



print([hh.numrows for hh in hhs])

quit
pygame.init()

window_size = [40+max([hh.numrows for hh in hhs])*(boxsize + linethickness), 40 + sum([hh.numcols for hh in hhs])*(boxsize + 2*linethickness)]
scr = pygame.display.set_mode(window_size)
pygame.display.set_caption("Notakto")
playing = True
clock = pygame.time.Clock()


#UPDATE
while playing:
    scr.fill(black)
    for hh in hhs:
        hh.draw(scr)
    pygame.display.flip()

    
    waitingForInput = True
    while waitingForInput:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                playing = False 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                rrx, rry = -1,-1
                for hh in hhs:
                    if(hh.active):
                        rrx, rry = hh.worldtolocalcoords(pos[0],pos[1], True)
                        if rrx != -1 and rry != -1:
                            waitingForInput = False
                            break

        clock.tick(50)

        
pygame.quit()
