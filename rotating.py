import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transformation")

# Colors
WHITE = (222, 255, 205)
BLACK = (0, 0, 0)


def rotate (x1, y1, x2, y2,angle):
   
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


    theta = angle * (math.pi / 180)
    
    # Perform rotation for both points (x1, y1) and (x2, y2)
    x3 = (x1 * math.cos(theta)) - (y1 * math.sin(theta))
    y3 = (y1 * math.cos(theta)) + (x1 * math.sin(theta))
    x4 = (x2 * math.cos(theta)) - (y2 * math.sin(theta))
    y4 = (y2 * math.cos(theta)) + (x2 * math.sin(theta))
    
    # DDA Line Drawing Algorithm
    dx = x4 - x3
    dy = y4 - y3
    steps = max(abs(dx), abs(dy))
    
    # If steps is a float, make sure to convert to int
    steps = int(steps)
    
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
        rotate (200, 100, 500, 400, 10)
        


        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()