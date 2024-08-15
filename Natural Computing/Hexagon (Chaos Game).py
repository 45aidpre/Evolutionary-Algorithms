import pygame
import random
import math

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Main function to run the chaos game
def chaos_game(screen, vertices, num_points):
    # Select a random starting point within the hexagon
    current_point = random.choice(vertices)
    
    for _ in range(num_points):
        # Roll a dice
        dice_roll = random.randint(0, 5)
        
        # Determine the next point based on the dice roll
        next_point = midpoint(current_point, vertices[dice_roll])
        
        # Draw the point
        pygame.draw.circle(screen, BLUE, (int(next_point[0]), int(next_point[1])), 1)
        
        # Update the display
        pygame.display.flip()
        
        # Update the current point
        current_point = next_point

# Function to get the midpoint between two points
def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chaos Game - Hexagon")
    screen.fill(BLACK)
    
    # Define the vertices of the hexagon
    vertices = []
    for i in range(6):
        angle = i * (2 * math.pi) / 6
        x = WIDTH // 2 + 200 * math.cos(angle)
        y = HEIGHT // 2 + 200 * math.sin(angle)
        vertices.append((x, y))
    
    # Draw the hexagon
    pygame.draw.polygon(screen, BLACK, vertices, 1)
    
    # Run the chaos game and determine amount of particles
    chaos_game(screen, vertices, 100000)
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == "__main__":
    main()
