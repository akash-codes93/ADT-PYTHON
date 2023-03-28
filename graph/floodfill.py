def flood_fill(grid, pos, new_value):
    queue = [pos]
    traversed = set()
    val = grid[pos[0]][pos[1]]

    while queue:
        i, j = queue.pop(0)
        grid[i][j] = new_value

        if (i, j) in traversed:
            continue

        traversed.add((i, j))

        if i - 1 >= 0 and grid[i - 1][j] == val:
            queue.append((i - 1, j))

        if j - 1 >= 0 and grid[i][j - 1] == val:
            queue.append((i, j - 1))

        if i + 1 < len(grid) and grid[i + 1][j] == val:
            queue.append((i + 1, j))

        if j + 1 < len(grid[i]) and grid[i][j + 1] == val:
            queue.append((i, j + 1))


grid = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 2, 2, 1, 1],
    [1, 1, 2, 2, 1, 1],
    [2, 2, 2, 2, 2, 2]
]

flood_fill(grid, (0, 0), 5)

print(grid)
