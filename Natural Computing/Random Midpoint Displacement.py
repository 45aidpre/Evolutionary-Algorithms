import random
import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((600, 480))  # Set up a window with dimensions 600x480 pixels.
pygame.display.set_caption("rmda")  # Set the window title to "rmda".
screen.fill((255, 255, 255))  # Fill the window with a white background.

nrc = 5  # Number of recursion levels
std = 3  # Standard deviation
x = []  # List to store the heights of points
de = [0]  # List to store displacement values

# Function to generate points using the midpoint displacement algorithm
def randmidpoint1D(nrc, std):
    n = pow(2, nrc)  # Calculate the number of points based on the recursion level
    x.append(0)  # Initialize the first point with a height of 0
    for i in range(n - 1):
        x.append(0)  # Initialize the other points with a height of 0
    x.append(std * random.normalvariate(0, std))  # Set the last point with a random height
    for i in range(nrc):
        de.append(std * pow(0.5, (i + 1) / 2))  # Calculate displacement values for each recursion level
    recursion(x, 0, n, 1, nrc)  # Perform midpoint displacement recursion

# Function for recursive midpoint displacement
def recursion(x, t0, t2, t, nrc):
    t1 = int((t0 + t2) / 2)  # Calculate the midpoint index
    # Calculate the height of the midpoint with displacement
    x[t1] = 0.5 * (x[t0] + x[t2]) + de[t] * random.normalvariate(0, std)
    if t < nrc:  # If not reached the maximum recursion level
        # Recursively call the function for the left and right segments
        recursion(x, t0, t1, t + 1, nrc)
        recursion(x, t1, t2, t + 1, nrc)

randmidpoint1D(nrc, std)  # Generate the points using midpoint displacement
sc = 10  # Scale factor for drawing

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the window is closed
            running = False  # Exit the loop

    # Drawing the lines
    for i in range(len(x) - 1):
        # Draw lines between consecutive points with appropriate scaling
        pygame.draw.line(screen, (0, 0, 0), (i * sc, 240 - x[i] * sc), ((i + 1) * sc, 240 - x[i + 1] * sc))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
