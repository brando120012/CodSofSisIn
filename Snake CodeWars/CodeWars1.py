def trim_canvas(canvas):
    """
    Given a 2D list of chars, strip any full‐blank rows on top/bottom
    and any full‐blank columns on left/right.
    Returns the trimmed canvas (possibly [] if nothing remains).
    """
    # 1) Drop blank rows
    rows = [r for r in canvas if any(c != ' ' for c in r)]
    if not rows:
        return []

    # 2) Transpose, drop blank cols, transpose back
    cols = list(zip(*rows))
    cols = [c for c in cols if any(ch != ' ' for ch in c)]
    return [list(r) for r in zip(*cols)]


def python_snake(body):
    # 1) Build raw positions
    positions = []
    x = y = 0
    direction = 1
    for i, length in enumerate(body):
        # on first segment we stay at y=0, after that we bump y by 1
        if i:
            y += 1
        segment = [(x + j*direction, y) for j in range(length)]
        positions.extend(segment)
        # move x to the end of this segment
        x += (length - 1)*direction
        direction *= -1

    # 2) Compute bounding‐box
    xs, ys = zip(*positions)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # 3) Shift coords so min becomes (0,0)
    positions = [ (px - min_x, py - min_y) for px,py in positions ]

    # 4) Create full canvas at exact size and draw H, x, T
    w, h = max_x - min_x + 1, max_y - min_y + 1
    canvas = [[' ']*w for _ in range(h)]

    for idx, (px, py) in enumerate(positions):
        char = 'H' if idx==0 else ('T' if idx==len(positions)-1 else 'x')
        canvas[py][px] = char

    # 5) (Optional) In this construction, no extra blank rows/cols remain—
    #    but if you ever need it, just uncomment the next line:
    # canvas = trim_canvas(canvas)

    return canvas