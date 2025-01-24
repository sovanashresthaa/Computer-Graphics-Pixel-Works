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

tx = int(input("Enter the translating point in x"))
ty = int(input("Enter the translating point in y"))

#Translation

def trans(x1,x2,y1,y2):
    x3 = x1 + tx
    x4 = x2 + tx
    y3 = y1 + ty
    y4 = y2 + ty

    pygame.draw.line(screen, "WHITE", (x3,y3),(x4,y4),7)


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
        x1 = 50
        x2 = 100
        y1 = 50
        y2 = 100
        

        pygame.draw.line(screen, "WHITE", (x1,y1),(x2,y2),7)
        trans(x1,y1,x2,y2)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()