# Of course it draws a circle lmao
import pygame
import random
import math

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Main function to run the chaos game
def chaos_game(screen, center, radius, num_points):
    # Select a random starting point within the circle
    current_angle = random.uniform(0, 2*math.pi)
    current_point = (center[0] + radius * math.cos(current_angle), center[1] + radius * math.sin(current_angle))
    
    for _ in range(num_points):
        # Roll a dice
        dice_roll = random.uniform(0, 1)
        
        # Determine the next point based on the dice roll
        next_angle = dice_roll * 2 * math.pi
        next_point = (center[0] + radius * math.cos(next_angle), center[1] + radius * math.sin(next_angle))
        
        # Draw the point
        pygame.draw.circle(screen, BLUE, (int(next_point[0]), int(next_point[1])), 1)
        
        # Update the display
        pygame.display.flip()
        
        # Update the current point
        current_point = next_point

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chaos Game - Circle")
    screen.fill(BLACK)
    
    # Define the center and radius of the circle
    center = (WIDTH // 2, HEIGHT // 2)
    radius = min(WIDTH, HEIGHT) // 3
    
    # Draw the circle
    pygame.draw.circle(screen, BLACK, center, radius, 1)
    
    # Run the chaos game and determine amount of particles
    chaos_game(screen, center, radius, 10000)
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == "__main__":
    main()
