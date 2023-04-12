import random


def greedy_construction(items, capacity, alpha):
    sorted_items = sorted(items, key=lambda x: x[1] / x[2], reverse=True)
    solution = [0] * len(items)
    current_weight = 0

    for i in range(len(sorted_items)):
        if random.uniform(0, 1) <= alpha:
            item = sorted_items[i]
            if current_weight + item[2] <= capacity:
                solution[item[0]] = 1
                current_weight += item[2]

    return solution


def local_search(items, capacity, solution):
    current_weight = sum([items[i][2] for i in range(len(items)) if solution[i] == 1])

    while True:
        best_delta = 0
        best_item = None
        best_index = None

        for i in range(len(solution)):
            if solution[i] == 0:
                item = items[i]
                delta = item[1] - item[1] / item[2] * current_weight
                if delta > best_delta and current_weight + item[2] <= capacity:
                    best_delta = delta
                    best_item = item
                    best_index = i

        if best_item is None:
            break

        solution[best_index] = 1
        current_weight += best_item[2]

    return solution


def grasp(items, capacity, alpha, max_iter):
    best_solution = None
    best_value = 0

    for i in range(max_iter):
        solution = greedy_construction(items, capacity, alpha)
        solution = local_search(items, capacity, solution)
        solution_value = sum([items[i][1] for i in range(len(items)) if solution[i] == 1])

        if solution_value > best_value:
            best_solution = solution
            best_value = solution_value

    return best_solution, best_value


items = [(0, 55, 95), (1, 10, 4), (2, 47, 60),  (3, 5, 32), (4, 4 ,23), (5 ,50 ,72),
         (6 ,8 ,80),(7 ,61 ,62), (8 ,85, 65), (9, 87, 46)]

capacity = 269
alpha = 0.5
max_iter = 1000

solution, value = grasp(items, capacity, alpha, max_iter)
print("Solution:", solution)
print("Value:", value)
