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
FILL_COLOR = (255, 220, 220)  # Red color for filling the ellipse

# Function to draw and fill an ellipse using pygame's optimized method
def draw_ellipse(xc, yc, rx, ry, fill=False):
    rect = pygame.Rect(xc - rx, yc - ry, 2 * rx, 2 * ry)
    
    if fill:
        pygame.draw.ellipse(screen, FILL_COLOR, rect)  # Fill the ellipse
    pygame.draw.ellipse(screen, WHITE, rect, 2)  # Draw the border of the ellipse

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw and fill one ellipse, and just draw borders for others
        draw_ellipse(700, 450, 600, 300)  # Filled red ellipse
        draw_ellipse(700, 450, 100, 100,fill=True)             # Just border
        draw_ellipse(700, 450, 400, 200)             # Just border
        draw_ellipse(700, 450, 700, 400)             # Just border

        draw_ellipse(300, 450, 50, 50)               # Just border
        draw_ellipse(400, 180, 60, 60)               # Just border
        draw_ellipse(900, 750, 40, 40)               # Just border
        draw_ellipse(900, 60, 50, 50)                # Just border

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()