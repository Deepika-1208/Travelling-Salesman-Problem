import matplotlib.pyplot as plt

from itertools import permutations

# Function to calculate the distance of a route

def calculate_route_distance(route, distance_matrix):

    total_distance = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

    return total_distance

# Function to visualize the TSP decision tree without using networkx

def draw_tsp_decision_tree(cities, distance_matrix):

    start_city = cities[0]

    # Generate all possible routes (permutations of cities excluding the start city)

    possible_routes = [tuple([start_city] + list(route) + [start_city]) for route in permutations(cities[1:])]

    # Prepare data for plotting

    fig, ax = plt.subplots(figsize=(10, 8))

    y_pos = range(len(possible_routes))

    labels = [" → ".join(map(str, route)) for route in possible_routes]

    distances = [calculate_route_distance(route, distance_matrix) for route in possible_routes]

  

# Plot each route as a labeled point with distance

    for i, (label, distance) in enumerate(zip(labels, distances)):

        ax.plot([0, 1], [i, i], marker='o', color='lightblue', markersize=10, linewidth=2)

        ax.text(1.1, i, f"{label} (Distance: {distance})", verticalalignment='center', fontsize=10)

    # Set plot title and hide axes

    ax.set_title("TSP Decision Tree", fontsize=15)

    ax.axis('off')

    plt.show()

# Example usage:

cities = [0, 1, 2]

distance_matrix = [

    [0, 10, 15],  # Distances from city 0

    [10, 0, 35],  # Distances from city 1

    [15, 35, 0]   # Distances from city 2

]

# Draw the TSP decision tree


draw_tsp_decision_tree(cities, distance_matrix)