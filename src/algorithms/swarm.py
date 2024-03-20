import matplotlib.pyplot as plt
import numpy as np

class AntAlgorithm:
    def __init__(self, order, warehouse) -> None:
        self.order = order
        self.warehouse = warehouse
        print(self.order)
        print(self.warehouse)


# class TargetedAntColonyOptimizerFixed:
#     def __init__(self, distances, targets, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
#         self.distances = distances
#         self.targets = targets  # List of target shelf indices
#         self.pheromone = np.ones(self.distances.shape) / len(distances)
#         self.n_ants = n_ants
#         self.n_best = n_best
#         self.n_iterations = n_iterations
#         self.decay = decay
#         self.alpha = alpha
#         self.beta = beta
#         self.shortest_path_history = []  # Track the length of the shortest path over iterations

#     def spread_pheromone(self, all_paths, n_best, shortest_path):
#         sorted_paths = sorted(all_paths, key=lambda x: x[1])
#         for path, distance in sorted_paths[:n_best]:
#             for move in path:
#                 self.pheromone[move] += 1.0 / self.distances[move]

#         # Reinforce path pheromone on the shortest path found so far
#         for move in shortest_path[0]:
#             self.pheromone[move] += 1.0 / shortest_path[1]

#     def ant_path(self, start):
#         path = []
#         visited = set([start])
#         prev = start
#         while not all(target in visited for target in self.targets):
#             move = self.pick_move(self.pheromone[prev], self.distances[prev], visited, prev)
#             if move in self.targets:
#                 path.append((prev, move))
#                 visited.add(move)
#             prev = move
#         return path

#     def pick_move(self, pheromone, dist, visited, current):
#         pheromone = np.copy(pheromone)
#         pheromone[list(visited)] = 0

#         choices = [i for i in self.targets if i not in visited and self.distances[current][i] > 0]
#         if not choices:
#             return current  # No valid move, return to current location (should not happen with valid targets)

#         dist = dist[choices]
#         pheromone = pheromone[choices]
#         probabilities = pheromone ** self.alpha * ((1.0 / dist) ** self.beta)
#         probabilities /= probabilities.sum()
#         move = np.random.choice(choices, 1, p=probabilities)[0]
#         return move

#     def run(self):
#         all_time_shortest_path = ("placeholder", np.inf)
#         for i in range(self.n_iterations):
#             all_paths = []
#             for start in self.targets:  # Initialize ants at target locations
#                 path = self.ant_path(start)
#                 all_paths.append((path, self.path_distance(path)))
#                 if all_paths[-1][1] < all_time_shortest_path[1]:
#                     all_time_shortest_path = all_paths[-1]
#             self.spread_pheromone(all_paths, self.n_best, all_time_shortest_path)
#             self.pheromone *= self.decay
#             self.shortest_path_history.append(all_time_shortest_path[1])
#         return all_time_shortest_path

#     def path_distance(self, path):
#         total_dist = 0
#         for ele in path:
#             total_dist += self.distances[ele]
#         return total_dist

# distances = np.array([[0, 1, 1, 0, 0, 0, 0, 0], 
#                       [1, 0, 0, 1, 0, 0, 0, 0],
#                       [1, 0, 0, 0, 1, 0, 0, 0], 
#                       [0, 1, 0, 0, 0, 1, 0, 0],
#                       [0, 0, 1, 0, 0, 0, 1, 0], 
#                       [0, 0, 0, 1, 0, 0, 0, 1],
#                       [0, 0, 0, 0, 1, 0, 0, 1], 
#                       [0, 0, 0, 0, 0, 1, 1, 0]])

# targets = [1, 2]  # Półki docelo

# # Initialize and run the fixed algorithm
# aco_fixed = TargetedAntColonyOptimizerFixed(distances, targets, n_ants=1, n_best=1, n_iterations=1, decay=0.5, alpha=1, beta=2)
# shortest_path_fixed = aco_fixed.run()

# # Plotting the improvement over iterations with the fixed algorithm
# plt.figure(figsize=(10, 6))
# plt.plot(aco_fixed.shortest_path_history, marker='o', linestyle='-', color='r')
# plt.title('Improvement of Shortest Path Length Over Iterations (Fixed)')
# plt.xlabel('Iteration')
# plt.ylabel('Length of Shortest Path')
# plt.grid(True)
# plt.show()



# # import numpy as np

# # class TargetedAntColonyOptimizer:
# #     def __init__(self, distances, targets, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
# #         self.distances = distances
# #         self.targets = targets  # Lista indeksów półek docelowych
# #         self.pheromone = np.ones(self.distances.shape) / len(distances)
# #         self.n_ants = n_ants
# #         self.n_best = n_best
# #         self.n_iterations = n_iterations
# #         self.decay = decay
# #         self.alpha = alpha
# #         self.beta = beta

# #     def spread_pheromone(self, all_paths, n_best, shortest_path):
# #         sorted_paths = sorted(all_paths, key=lambda x: x[1])
# #         for path, distance in sorted_paths[:n_best]:
# #             for move in path:
# #                 self.pheromone[move] += 1.0 / self.distances[move]
                
# #         # Dodatkowo wzmacniamy ślad na najkrótszej ścieżce
# #         for move in shortest_path[0]:
# #             self.pheromone[move] += 1.0 / shortest_path[1]

# #     def ant_path(self, start):
# #         path = []
# #         visited = set([start])
# #         prev = start
# #         while not all(target in visited for target in self.targets):
# #             move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
# #             if move in self.targets:
# #                 path.append((prev, move))
# #                 visited.add(move)
# #             prev = move
# #         return path

# #     def pick_move(self, pheromone, dist, visited):
# #         pheromone = np.copy(pheromone)
# #         pheromone[list(visited)] = 0

# #         row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)
# #         norm_row = row / row.sum()
# #         move = np_choice(self.targets, 1, p=norm_row)[0]  # Zmieniono na wybór spośród celów
# #         return move

# #     def run(self):
# #         shortest_path = None
# #         all_time_shortest_path = ("placeholder", np.inf)
# #         for i in range(self.n_iterations):
# #             all_paths = []
# #             for start in self.targets:  # Inicjalizacja mrówek w miejscach docelowych
# #                 path = self.ant_path(start)
# #                 all_paths.append((path, self.path_distance(path)))
# #                 if all_paths[-1][1] < all_time_shortest_path[1]:
# #                     all_time_shortest_path = all_paths[-1]            
# #             self.spread_pheromone(all_paths, self.n_best, all_time_shortest_path)
# #             self.pheromone * self.decay
# #         return all_time_shortest_path

# #     def path_distance(self, path):
# #         total_dist = 0
# #         for ele in path:
# #             total_dist += self.distances[ele]
# #         return total_dist

# # def np_choice(a, size, p):
# #     return np.random.choice(a, size=size, replace=False, p=p)

# # # Przykładowe odległości i cele
# # distances = np.array([[0, 1, 2, 3], [1, 0, 4, 5], [2, 4, 0, 6], [3, 5, 6, 0]])
# # targets = [1, 3]  # Półki docelowe

# # # Inicjalizacja i uruchomienie algorytmu
# # aco = TargetedAntColonyOptimizer(distances, targets, n_ants=4, n_best=1, n_iterations=100, decay=0.5, alpha=1, beta=2)
# # shortest_path = aco.run()
# # print(f"Najkrótsza ścieżka: {shortest_path[0]} z długością: {shortest_path[1]}")
