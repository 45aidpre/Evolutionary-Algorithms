import pygame
import random

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Function to get the midpoint between two points
def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# Main function to run the chaos game

def chaos_game(screen, vertices, num_points):
    # Select a random starting point within the triangle
    current_point = random.choice(vertices)
    
    for _ in range(num_points):
        # Roll a dice
        dice_roll = random.randint(1, 6)
        
        # Determine the next point based on the dice roll
        if dice_roll in [1, 2]:
            next_point = midpoint(current_point, vertices[0])
        elif dice_roll in [3, 4]:
            next_point = midpoint(current_point, vertices[1])
        else:
            next_point = midpoint(current_point, vertices[2])
        
        # Draw the point
        pygame.draw.circle(screen, BLUE, (int(next_point[0]), int(next_point[1])), 1)
        
        # Update the display
        pygame.display.flip()
        
        # Update the current point
        current_point = next_point

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chaos Game - Triangle")
    screen.fill(BLACK)
    
    # Define the vertices of the equilateral triangle
    vertices = [(WIDTH // 2, 100), (100, HEIGHT - 100), (WIDTH - 100, HEIGHT - 100)]
    
    # Draw the triangle
    pygame.draw.polygon(screen, BLACK, vertices, 1)
    
    # Run the chaos game and determine amount of particles
    chaos_game(screen, vertices, 10000)
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == "__main__":
    main()
