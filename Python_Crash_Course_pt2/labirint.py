def solve_maze_iterative(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        current = stack.pop()
        if current == end:
            return True

        if current in visited:
            continue

        visited.add(current)
        row, col = current

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if (0 <= r < rows and 0 <= c < cols and
                maze[r][c] == 0 and (r, c) not in visited):
                stack.append((r, c))

    return False
