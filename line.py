import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bresenham's line drawing algorithm")

WHITE = (222, 255, 205)
BLACK = (0, 0, 0)

def draw_line_bresh(x1,y1,x2,y2):
    dx = abs (int(x2-x1))
    dy = abs (int(y2-y1))
    x = x1
    y = y1
    if (x2>x1):
        lx = 1

    else:
        lx = ly

    if (y2>y1):
        ly = 1

    else:
        ly= -1
        
    if (dx>dy):
        p = 2*dy-dx
        screen.set_at((round(x), round (y)))
        while(not(x==x2)):
            if (p<0):
                p = p + 2*dy

            else:
                y = y + ly 
                p = p + 2*dy - 2*dx
                x = x+lx 
            screen.set_at((round(x), round (y))) 
    else:
        p = 2*dx - dy
        while (not(y==y2)):
            if (p<0):
                p = p + 2*dx
            else: 
                x = x + lx
                p + p + 2*dx - 2*dy
            y = y +ly
            screen.set_at((round(x), round (y)))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        screen.fill(BLACK)
        
    
        draw_line_bresh(20,20,100,100)

        pygame.display.flip()

if __name__ == "__main__":

    main()
