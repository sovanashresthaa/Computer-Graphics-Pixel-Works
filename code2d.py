import pygame  
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 8
00
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


tx = int(input("Enter transalation x"))
ty = int(input("Enter transalation y"))

sx = float(input("Enter scaling x"))
sy = float(input("Enter scaling y"))

theta = int(input("Enter rotation angle "))

def translation(x1, y1, x2, y2, tx, ty):
   
    x1a = x1 + tx
    y1a = y1 + ty
    x2a = x2 + tx
    y2a = y2 + ty
    pygame.draw.line(screen, "RED", (x1a, y1a), (x2a, y2a), 5)

def scaling(x1, y1, x2, y2, sx, sy):
   
    x1a = x1*sx
    y1a = y1*sy
    x2a = x2*sx
    y2a = y2*ty
    pygame.draw.line(screen, "GREEN", (x1a, y1a), (x2a, y2a), 5)

def rotation(x1, y1, x2, y2, theta):
    # Convert angle to radians (if theta is in degrees)
    angle = math.radians(theta)  # Convert theta to radians if it's in degrees
    
    # Apply the rotation formulas to both points
    x1a = x1 * math.cos(angle) - y1 * math.sin(angle)
    y1a = x1 * math.sin(angle) + y1 * math.cos(angle)
    x2a = x2 * math.cos(angle) - y2 * math.sin(angle)
    y2a = x2 * math.sin(angle) + y2 * math.cos(angle)
    
    # Draw the rotated line (rounded to nearest integer)
    pygame.draw.line(screen, "Yellow", (round(x1a), round(y1a)), (round(x2a), round(y2a)), 5)


# Function to draw a line using DDA algorithm
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
    translation(x1, y1, x2, y2, tx, ty)  
    scaling(x1, y1, x2, y2, sx, sy) 
    rotation(x1, y1, x2, y2, theta) 

# Main loop
def main():    
    # Coordinates for the line
    x1 = 20
    y1 = 20
    x2 = 100
    y2 = 200

    # Apply the translation based on user input
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw translated line using DDA algorithm
        draw_line_dda(x1, y1, x2, y2)
       
        

        # Update the display
        pygame.display.flip()
    


if __name__ == "__main__":
    main()
