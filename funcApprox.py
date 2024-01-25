import random,math

# Set the standard deviation for the random Gaussian process
std = 0.001

# Define the mathematical function to be evaluated
def func(x):
    return pow(2, -2 * pow((x - 0.1) / 0.9, 2)) * pow(math.sin(5 * math.pi * x), 6)

# Point Mutation
def point_mutation(individual, mutation_rate):
    mutated_individual = individual + random.gauss(0, std)
    # Ensure the mutated value is within [0, 1]
    return max(0, min(1, mutated_individual))  

# Crossover
def crossover(parent1, parent2):
    crossover_point = random.uniform(0, 1)
    child = crossover_point * parent1 + (1 - crossover_point) * parent2
    # Ensure the child is within [0, 1]
    return max(0, min(1, child))  

# Genetic Algorithm
def genetic_algorithm(population_size, generations, mutation_rate):
    highest = 0

    for generation in range(generations):
        # Initialize population
        population = [random.uniform(0, 1) for _ in range(population_size)]

        # Evaluate fitness and update highest
        fitness_values = [func(individual) for individual in population]
        highest_in_generation = max(fitness_values)
        highest = max(highest, highest_in_generation)

        # Select parents for crossover
        parents = random.sample(population, k=2)

        # Apply crossover
        child = crossover(parents[0], parents[1])

        # Apply mutation to the child
        mutated_child = point_mutation(child, mutation_rate)

        # Update highest value if mutated child is greater
        highest = max(highest, func(mutated_child))

    return highest

# Run genetic algorithm with specified parameters
population_size = 50
generations = 10
mutation_rate = 0.01

result = genetic_algorithm(population_size, generations, mutation_rate)
print("Highest value:", result)
