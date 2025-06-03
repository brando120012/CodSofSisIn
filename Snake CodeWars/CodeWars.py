def python_snake(body):
    # Directions: right, up, left, down
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_idx = 0  # Start moving to the right
    
    x, y = 0, 0  # Starting position
    grid = {}
    coords = []

    for i, length in enumerate(body):
        for step in range(length):
            # Determine character to draw
            if i == 0 and step == 0:
                char = 'H'
            elif i == len(body) - 1 and step == length - 1:
                char = 'T'
            else:
                char = 'x'

            x += directions[dir_idx][0]
            y += directions[dir_idx][1]
            
            grid[(x, y)] = char
            coords.append((x, y))

        # Rotate direction clockwise
        dir_idx = (dir_idx + 1) % 4

    # Find bounds
    min_x = min(x for x, y in coords)
    max_x = max(x for x, y in coords)
    min_y = min(y for x, y in coords)
    max_y = max(y for x, y in coords)

    # Build final matrix with padding
    result = []
    for y_coord in range(min_y - 1, max_y + 2):
        row = []
        for x_coord in range(min_x - 1, max_x + 2):
            row.append(grid.get