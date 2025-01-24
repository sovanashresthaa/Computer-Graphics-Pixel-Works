
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (255, 222, 255)


def draw_line_dda(x1, y1, x2, y2):
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
        x1 = int(input("Enter x1"))
        x2 = int(input("Enter x2"))
        y1 = int(input("Enter y1"))
        y2 = int(input("Enter y2"))

        draw_line_dda(x1,x2 , y1 , y2)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
