import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transformation")

# Colors
WHITE = (222, 255, 205)
BLACK = (0, 0, 0)


def translate(x1, y1, x2, y2,tx,ty):
   
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1
    for i in range(steps):
        screen.set_at((round(x), round(y)), WHITE)
        x += x_increment
        y += y_increment
    
    
    x3 = x1 + tx
    x4 = x2 + tx
    y3 = y1 + ty
    y4 = y2 + ty
    
    dx = x4 - x3
    dy = y4 - y3
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x = x3
    y = y3

    for i in range(steps):
        screen.set_at((round(x), round(y)), WHITE)
        x += x_increment
        y += y_increment
      


# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        translate (10, 100, 100, 300,200,0)
        


        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()