import numpy as np
import matplotlib.pyplot as plt

# Part_1 – initialization parameters
POPULATION_SIZE = 200
NUM_GENERATIONS = 5000
CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.01
PENALTY = 1e6  # penalty if constraint x + y >= 1 is broken

# Part_2 - chromosome encoding
X_BITS = 15
Y_BITS = 16
CHROMOSOME_LENGTH = X_BITS + Y_BITS  # total 31 bits long

X_BOUND = (0, 2)
Y_BOUND = (0, 3)

# Part_3 - chromosomes decoding
def decode_chromosome(chromosome):
    x_bin = chromosome[:X_BITS]
    y_bin = chromosome[X_BITS:]
    x_int = int("".join(str(int(bit)) for bit in x_bin), 2)
    y_int = int("".join(str(int(bit)) for bit in y_bin), 2)
    x_real = X_BOUND[0] + x_int * (X_BOUND[1] - X_BOUND[0]) / (2**X_BITS - 1)
    y_real = Y_BOUND[0] + y_int * (Y_BOUND[1] - Y_BOUND[0]) / (2**Y_BITS - 1)
    return x_real, y_real

# Part_4 - population initialization
def initialize_population():
    return np.random.randint(0, 2, (POPULATION_SIZE, CHROMOSOME_LENGTH))

# Part_5 - fitness function (how good the solution is)
def fitness_function(chromosome):
    x, y = decode_chromosome(chromosome)

    #Constraint Handling
    if x + y < 1:
        return -PENALTY

    #Fitness Evaluation
    value = np.cos((x - 1.14) ** 6) - 100 * (y**2 - x) ** 4
    return value

# Part_6 - selection (robust roulette with rank fallback)
def selection(population, fitnesses):
    # sanitize
    fitnesses = np.nan_to_num(fitnesses, nan=-1e12, posinf=1e12, neginf=-1e12)

    # shift to positive for roulette
    min_fit = np.min(fitnesses)
    adjusted = fitnesses - min_fit + 1e-12
    total = adjusted.sum()

    # fallback: rank-based if total invalid
    if (not np.isfinite(total)) or (total <= 0):
        ranks = np.argsort(np.argsort(-fitnesses)) + 1  # 1..N
        probs = ranks / ranks.sum()
    else:
        probs = adjusted / total

    # stabilize
    probs = np.clip(probs, 0, None)
    s = probs.sum()
    if s == 0 or not np.isfinite(s):
        probs = np.ones_like(probs) / len(probs)
    else:
        probs = probs / s

    selected_indices = np.random.choice(
        np.arange(POPULATION_SIZE), size=POPULATION_SIZE, p=probs
    )
    return population[selected_indices]

# Part 7 - crossover (two-point crossover between two parents)
def crossover(parent1, parent2):
    if np.random.rand() < CROSSOVER_RATE:
        point1 = np.random.randint(0, CHROMOSOME_LENGTH)
        point2 = np.random.randint(point1, CHROMOSOME_LENGTH)
        child1 = np.concatenate((parent1[:point1], parent2[point1:point2], parent1[point2:]))
        child2 = np.concatenate((parent2[:point1], parent1[point1:point2], parent2[point2:]))
        return child1, child2
    else:
        return parent1.copy(), parent2.copy()

# Part_8 - mutation (flipping the individual bits)
def mutate(chromosome):
    for i in range(CHROMOSOME_LENGTH):
        if np.random.rand() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# Part_9 - main algorithm loop
def genetic_algorithm():
    population = initialize_population()

    best_fitness_history = []
    best_solution = None
    best_fitness_value = -np.inf

    for generation in range(NUM_GENERATIONS):
        fitnesses = np.array([fitness_function(individual) for individual in population])

        generation_best_index = np.argmax(fitnesses)
        generation_best_fitness = fitnesses[generation_best_index]

        if generation_best_fitness > best_fitness_value:
            best_fitness_value = generation_best_fitness
            best_solution = population[generation_best_index].copy()

        best_fitness_history.append(best_fitness_value)
        selected_population = selection(population, fitnesses)
        next_generation = []

        for i in range(0, POPULATION_SIZE, 2):
            parent1, parent2 = selected_population[i], selected_population[i+1]
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutate(child1))
            next_generation.append(mutate(child2))

        population = np.array(next_generation)

    return best_solution, best_fitness_value, best_fitness_history

# Part_10 - run & plot results
best_chromosome, best_fitness, fitness_history = genetic_algorithm()
x_opt, y_opt = decode_chromosome(best_chromosome)

print(f"Best solution found: x = {x_opt:.4f}, y = {y_opt:.4f}")
print(f"Maximum value of f(x, y): {best_fitness:.6f}")

plt.plot(fitness_history)
plt.title("Evolution History")
plt.xlabel("Generations")
plt.ylabel("Best objective function")
plt.grid(True)
plt.show()


