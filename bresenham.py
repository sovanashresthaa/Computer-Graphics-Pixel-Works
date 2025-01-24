import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's/ Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Function to draw a line using DDA algorithm
def draw_line_bresh(x1, y1, x2, y2):
    dx=abs(int(x2-x1))
    dy=abs(int(y2-y1))
    x = x1
    y = y1
    if (x2>x1):
        lx = 1
    else:
        lx = -1

    if (y2>y1):
        ly = 1
    else:
        ly = -1

    if(dx>dy):
        p = 2*dy - dx
        screen.set_at((round(x), round(y)), WHITE) 
        while(not(x==x2)):
            screen.set_at((round(x), round(y)), WHITE) 
            if(p<0):
                x = x + lx
                p = p + 2*dy
            else:
                y = y + ly
                x = x + lx
                p = p + 2*dy - 2*dx
           
    else:
        p = 2*dx - dy
        while(not(y==y2)):
            screen.set_at((round(x), round(y)), WHITE)   
            if(p<0):
                y = y + ly
                p = p + 2*dx
            else:
                x = x + lx
                y = y + ly
                p = p + 2*dx - 2*dy
                
                
      
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a square using Bresenham's algorithm
        draw_line_bresh(20,20 ,100, 200)
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
   
   
   
   
   
   