import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid point ellipse algorithm")

# Colors
WHITE = (222, 255, 205)
BLACK = (0, 0, 0)

# Function to draw a line using DDA algorithm
def draw_ellipse(xc,yc,rx,ry):
    x=0
    y=ry
    p1 = (ry**2) - ((rx**2)*ry)+(0.25*(ry**2))
    while((2*(ry**2)*x) <= (2*(rx**2)*y)):
        if p1<0:
            x = x + 1
            y = y
            p1=p1+(2*(ry**2)*x)+ ry**2
        else:
            x = x+1
            y = y-1
            p1=p1+(2*(ry**2)*x) - (2*(rx**2)*y)+ (ry**2)

        screen.set_at((round (x+xc), round (y+yc)),WHITE)
        screen.set_at((round (x+xc), round (-y+yc)),WHITE)
        screen.set_at((round (-x+xc), round (y+yc)),WHITE)
        screen.set_at((round (-x+xc), round (-y+yc)),WHITE)

    
    p2 = ((ry**2)*((x + 0.5)**2))+((rx**2)*((y-1)**2)) - ((rx**2)*(ry**2))
    while(y!=0):
        if p2>0:
            x = x 
            y = y-1
            p2=p2-(2*(rx**2)*y)+ (rx**2)
        else:
            x = x + 1
            y = y - 1
            p2=p2+(2*(ry**2)*x) - (2*(rx**2)*y)+ (rx**2)
           
        screen.set_at((round (x+xc), round (y+yc)),WHITE)
        screen.set_at((round (x+xc), round (-y+yc)),WHITE)
        screen.set_at((round (-x+xc), round (y+yc)),WHITE)
        screen.set_at((round (-x+xc), round (-y+yc)),WHITE)


# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # draw an ellipse
        draw_ellipse(700, 450, 600, 300)
        draw_ellipse(700, 450, 100, 100)
        draw_ellipse(700, 450, 400, 200)
        draw_ellipse(700, 450, 700, 400)

        draw_ellipse(300, 450, 50, 50)
        draw_ellipse(400, 180, 60, 60)
        draw_ellipse(900, 750, 40, 40)
        draw_ellipse(900, 60, 50, 50)

        pygame.display.flip()

if __name__ == "__main__":
    main()