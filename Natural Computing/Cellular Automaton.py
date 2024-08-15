def apply_rule(rule, neighborhood):
    #Apply the transition rule to the neighborhood.
    return rule.get(neighborhood, 0)

def evolve_ca(initial_state, rule, steps):
    #Evolve the cellular automaton.
    current_state = initial_state
    next_state = [0] * len(initial_state)
    for _ in range(steps):
        for i in range(len(initial_state)):
            neighborhood = ''.join(str(current_state[(i+j) % len(initial_state)]) for j in [-1, 0, 1])
            next_state[i] = apply_rule(rule, neighborhood)
        current_state, next_state = next_state, current_state
        yield current_state

def print_ca(evolution):
    #Print the cellular automaton evolution.
    for state in evolution:
        print(''.join(map(str, state)))

# Transition rules for Table 1
rule_1 = {
    '000': 0, '100': 1,
    '001': 1, '101': 1,
    '010': 1, '110': 0,
    '011': 0, '111': 0
}

# Transition rules for Table 2
rule_2 = {
    '000': 0, '100': 1,
    '001': 1, '101': 1,
    '010': 1, '110': 1,
    '011': 1, '111': 0
}

# Initial condition
initial_condition = [0] * 31
initial_condition[15] = 1  # Set a single seed in the middle

print("Evolution according to Table 1:")
evolution_1 = evolve_ca(initial_condition, rule_1, 500)
print_ca(evolution_1)

print("\nEvolution according to Table 2: \n")
evolution_2 = evolve_ca(initial_condition, rule_2, 500)
print_ca(evolution_2)
