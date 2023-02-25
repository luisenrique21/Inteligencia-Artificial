import time
inicio = time.time()

def knapsack_recursive(items, capacity, cost, index):
    if index >= len(items) or capacity <= 0 or cost > 878:
        return 0

    item = items[index]
    if item[1] > capacity:
        return knapsack_recursive(items, capacity, cost, index + 1)
    else:
        with_item = item[0] + knapsack_recursive(items, capacity - item[1], cost + item[1], index + 1)
        without_item = knapsack_recursive(items, capacity, cost, index + 1)
        return max(with_item, without_item)


def knapsack(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        items = []
        for line in lines:
            b, c = map(int, line.split())         #cambiar a float cuando se tenga puros numeros con decimal
            items.append((b, c))
        items.sort(key=lambda x: x[0] / x[1], reverse=True)
        return knapsack_recursive(items, 375, 0, 0)

print(knapsack("f7_l-d_kp_7_50.txt"))
fin = time.time()
print(fin-inicio)