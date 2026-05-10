def astar(graph, heuristic, start, goal):
    open_list = [(start, 0)]
    closed_list = set()
    parent = {start: None}
    g_cost = {start: 0}

    while open_list:
        # Sort based on f(n) = g(n) + h(n)
        open_list.sort(key=lambda x: g_cost[x[0]] + heuristic[x[0]])
        current = open_list.pop(0)[0]

        if current == goal:
            break

        closed_list.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue

            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = current
                open_list.append((neighbor, new_cost))

    # Reconstruct path
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]

    return path[::-1]


# --------- Graph Definition ---------
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# --------- Heuristic Values ---------
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}

# --------- Run A* ---------
path = astar(graph, heuristic, 'A', 'G')
print("Shortest Path:", path)