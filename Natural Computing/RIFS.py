import numpy as np
import matplotlib.pyplot as plt

# Define IFS codes for each fractal

# Sierpinski Gasket
sierpinski_transforms = [
    (0.5, 0, 0, 0, 1, 1),
    (0.5, 0, 0, 0, 1, 50),
    (0.5, 0, 0, 0, 50, 50)
]
sierpinski_probs = [0.33, 0.33, 0.34]

# Square
square_transforms = [
    (0.5, 0, 0, 0.5, 1, 1),
    (0.5, 0, 0, 0.5, 50, 1),
    (0.5, 0, 0, 0.5, 1, 50),
    (0.5, 0, 0, 0.5, 50, 50)
]
square_probs = [0.25, 0.25, 0.25, 0.25]

# Barnsley fern
barnsley_transforms = [
    (0, 0, 0, 0.16, 0, 0),
    (0.85, 0.04, -0.04, 0.85, 0, 1.6),
    (0.2, -0.26, 0.23, 0.22, 0, 1.6),
    (-0.15, 0.28, 0.26, 0.24, 0, 0.44)
]
barnsley_probs = [0.01, 0.85, 0.07, 0.07]

# Tree
tree_transforms = [
    (0, 0, 0, 0.5, 0, 0),
    (0.42, -0.42, 0.42, 0.42, 0, 0.2),
    (0.42, 0.42, -0.42, 0.42, 0, 0.2),
    (0.1, 0, 0, 0.1, 0, 0.2)
]
tree_probs = [0.05, 0.4, 0.4, 0.15]

# Function to select a random transformation based on probabilities
def select_transform(transforms, probabilities):
    return np.random.choice(len(transforms), p=probabilities)

# Function to apply a transformation to a point
def apply_transform(transform, point):
    a, b, c, d, e, f = transform
    x, y = point
    return a * x + b * y + e, c * x + d * y + f

# Function to generate points using RIFS
def generate_fractal(transforms, probabilities, iterations):
    points = [(0, 0)]
    for _ in range(iterations):
        chosen_transform = select_transform(transforms, probabilities)
        points.append(apply_transform(transforms[chosen_transform], points[-1]))
    return points

# Function to plot a fractal
def plot_fractal(points, color, title):
    plt.scatter(*zip(*points), s=1, color=color, marker='.')
    plt.title(title)
    plt.axis('equal')

# Generate and plot Sierpinski Gasket
plt.subplot(2, 2, 1)
sierpinski_points = generate_fractal(sierpinski_transforms, sierpinski_probs, 100000)
plot_fractal(sierpinski_points, 'blue', 'Sierpinski Gasket')

# Generate and plot Square
plt.subplot(2, 2, 2)
square_points = generate_fractal(square_transforms, square_probs, 100000)
plot_fractal(square_points, 'green', 'Square')

# Generate and plot Barnsley Fern
plt.subplot(2, 2, 3)
barnsley_points = generate_fractal(barnsley_transforms, barnsley_probs, 100000)
plot_fractal(barnsley_points, 'orange', 'Barnsley Fern')

# Generate and plot Tree
plt.subplot(2, 2, 4)
tree_points = generate_fractal(tree_transforms, tree_probs, 100000)
plot_fractal(tree_points, 'brown', 'Tree')

plt.tight_layout()
plt.show()
