from collections import defaultdict
import bisect

# -------------------------
# Load input
# -------------------------
f = open("Days/DayNine/PuzzleTwo/input.txt")
lines = [x.strip() for x in f.readlines() if x.strip()]

reds = []
for line in lines:
    a, b = line.split(",")
    reds.append((int(a), int(b)))

# -------------------------
# Shift coordinates so they start at 0
# -------------------------
xs = [p[0] for p in reds]
ys = [p[1] for p in reds]
min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

shifted = [(x - min_x, y - min_y) for x, y in reds]

shifted_xs = [p[0] for p in shifted]
shifted_ys = [p[1] for p in shifted]
W = max(shifted_xs) + 1
H = max(shifted_ys) + 1

# -------------------------
# Build axis-aligned edges (green paths)
# -------------------------
n = len(shifted)
vert_edges = []   # (x, y_low, y_high) inclusive
horiz_edges = []  # (y, x_low, x_high) inclusive

for i in range(n):
    x1, y1 = shifted[i]
    x2, y2 = shifted[(i + 1) % n]
    if x1 == x2:
        ylow, yhigh = (y1, y2) if y1 <= y2 else (y2, y1)
        vert_edges.append((x1, ylow, yhigh))
    elif y1 == y2:
        xlow, xhigh = (x1, x2) if x1 <= x2 else (x2, x1)
        horiz_edges.append((y1, xlow, xhigh))
    else:
        # per problem won't happen
        pass

# -------------------------
# Build allowed intervals per original integer row using scanline + boundary marking
# row_intervals[y] = list of (x_start, x_end) inclusive allowed on that row
# -------------------------
row_intervals = defaultdict(list)

# 1) Scanline interiors: for each integer row y, scanline at y+0.5 intersects vertical edges
for y in range(H):
    scan_y = y + 0.5
    xs_int = []
    for (ex, ey1, ey2) in vert_edges:
        if ey1 <= scan_y < ey2:
            xs_int.append(ex)
    if xs_int:
        xs_int.sort()
        for k in range(0, len(xs_int), 2):
            xL = xs_int[k]
            xR = xs_int[k + 1]
            if xL <= xR - 1:
                row_intervals[y].append((xL, xR - 1))

# 2) Horizontal edges add exact-row intervals
for (y, x1, x2) in horiz_edges:
    if 0 <= y < H:
        row_intervals[y].append((x1, x2))

# 3) Vertical edge boundary tiles: for x, for each y in [y1..y2], add (x,x)
for (ex, ey1, ey2) in vert_edges:
    ys0 = max(0, ey1)
    ys1 = min(H - 1, ey2)
    for y in range(ys0, ys1 + 1):
        row_intervals[y].append((ex, ex))

# 4) Mark red tiles
for rx, ry in shifted:
    if 0 <= ry < H:
        row_intervals[ry].append((rx, rx))

# 5) Merge intervals per row
for y in range(H):
    if y not in row_intervals:
        continue
    ivs = row_intervals[y]
    if not ivs:
        continue
    ivs.sort()
    merged = []
    cs, ce = ivs[0]
    for s, e in ivs[1:]:
        if s <= ce + 1:
            if e > ce:
                ce = e
        else:
            merged.append((cs, ce))
            cs, ce = s, e
    merged.append((cs, ce))
    row_intervals[y] = merged

# -------------------------
# Build compressed X-axis from all interval endpoints (exclusive-right technique)
# -------------------------
Xpoints = set()
for y, ivs in row_intervals.items():
    for s, e in ivs:
        Xpoints.add(s)
        Xpoints.add(e + 1)
# also include red x endpoints
for rx, ry in shifted:
    Xpoints.add(rx)
    Xpoints.add(rx + 1)
Xpoints.add(0)
Xpoints.add(W)
Xs = sorted(Xpoints)
Wc = len(Xs) - 1

# Map each row's intervals to compressed column indices (i_start..i_end inclusive)
row_iv_c = {}
for y in range(H):
    if y not in row_intervals:
        row_iv_c[y] = []
        continue
    mapped = []
    for s, e in row_intervals[y]:
        i1 = bisect.bisect_left(Xs, s)
        i2 = bisect.bisect_left(Xs, e + 1) - 1
        if i1 <= i2:
            mapped.append((i1, i2))
    # merge mapped (should already be non-overlapping but merge as safety)
    if not mapped:
        row_iv_c[y] = []
        continue
    mapped.sort()
    merged = []
    cs, ce = mapped[0]
    for a, b in mapped[1:]:
        if a <= ce + 1:
            if b > ce:
                ce = b
        else:
            merged.append((cs, ce))
            cs, ce = a, b
    merged.append((cs, ce))
    row_iv_c[y] = merged

# -------------------------
# Build column vertical intervals: col_intervals[i] = list of (y_start, y_end) inclusive rows where column i is covered
# We'll populate by iterating rows and their compressed intervals.
# -------------------------
col_rows = [[] for _ in range(Wc)]
for y in range(H):
    for (i1, i2) in row_iv_c.get(y, []):
        for i in range(i1, i2 + 1):
            col_rows[i].append(y)

# Merge contiguous rows per column into intervals
col_intervals = [[] for _ in range(Wc)]
for i in range(Wc):
    if not col_rows[i]:
        continue
    col_rows[i].sort()
    s = col_rows[i][0]
    e = s
    for y in col_rows[i][1:]:
        if y == e + 1:
            e = y
        else:
            col_intervals[i].append((s, e))
            s = y
            e = y
    col_intervals[i].append((s, e))

# helper: does column i have an interval that fully covers rows r1..r2?
def col_covers(i, r1, r2):
    ivs = col_intervals[i]
    if not ivs:
        return False
    # binary search to find interval with start <= r1
    lo = 0
    hi = len(ivs) - 1
    idx = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if ivs[mid][0] <= r1:
            idx = mid
            lo = mid + 1
        else:
            hi = mid - 1
    if idx == -1:
        return False
    return ivs[idx][1] >= r2

# -------------------------
# Build red positions per compressed column and per row:
# red_in_col[i] = sorted list of rows j where there is a red at column i
# red_cols_in_row[y] = sorted list of columns i where there is a red at row y
# -------------------------
red_in_col = [[] for _ in range(Wc)]
red_cols_in_row = defaultdict(list)
for rx, ry in shifted:
    i = bisect.bisect_left(Xs, rx)
    if i >= Wc:
        continue
    red_in_col[i].append(ry)
    red_cols_in_row[ry].append(i)

for i in range(Wc):
    red_in_col[i].sort()
for y in red_cols_in_row:
    red_cols_in_row[y].sort()

# list of rows that contain at least one red (sorted)
rows_with_reds = sorted(red_cols_in_row.keys())

# -------------------------
# For each pair of rows (r1, r2) from rows_with_reds (r1 <= r2),
# compute 'good' columns where the column fully covers r1..r2,
# then for each contiguous segment of good columns compute candidate left/right red columns
# from red_cols_in_row[r1] and red_cols_in_row[r2] limited to the segment.
# -------------------------
best_area = 0
total_rows = H  # vertical span in shifted tile units

# Precompute for speed: for each column i, we will query col_covers many times.
# The col_intervals lists are small, so col_covers is already log-time; OK.

for idx1 in range(len(rows_with_reds)):
    r1 = rows_with_reds[idx1]
    # small optimization: if even full width * maximum possible height can't beat best, skip r1 early?
    # Hard to compute cheaply here; skip micro-optimizations for clarity.

    for idx2 in range(idx1, len(rows_with_reds)):
        r2 = rows_with_reds[idx2]
        height_real = r2 - r1 + 1

        # quick bound: if even using full X span can't beat best, skip
        max_width_possible = Xs[-1] - Xs[0]
        if max_width_possible * height_real <= best_area:
            continue

        # Build a boolean array of good columns for this (r1,r2)
        good = [False] * Wc
        for i in range(Wc):
            if col_covers(i, r1, r2):
                good[i] = True

        # scan contiguous segments of good columns
        i = 0
        while i < Wc:
            if not good[i]:
                i += 1
                continue
            j = i
            while j + 1 < Wc and good[j + 1]:
                j += 1
            # segment [i..j]
            # find columns in this segment that have red at r1 and red at r2
            Llist = red_cols_in_row.get(r1, [])
            Rlist = red_cols_in_row.get(r2, [])

            # find any L in Llist within [i..j]
            li = bisect.bisect_left(Llist, i)
            if li >= len(Llist) or Llist[li] > j:
                # no left-red in this segment
                i = j + 1
                continue
            # find any R in Rlist within [i..j]
            ri = bisect.bisect_left(Rlist, i)
            if ri >= len(Rlist) or Rlist[ri] > j:
                # no right-red in this segment
                i = j + 1
                continue

            # compute candidate extremes
            minL = Llist[li]
            # maxL: last index in Llist <= j
            lj = bisect.bisect_right(Llist, j) - 1
            maxL = Llist[lj]

            minR = Rlist[ri]
            rj = bisect.bisect_right(Rlist, j) - 1
            maxR = Rlist[rj]

            # candidate widths: (maxR - minL), (maxL - minR) if positive
            # convert compressed column indices to real width in tiles: Xs[c+1] - Xs[c']
            # need to ensure left < right
            # Candidate 1: left = minL, right = maxR
            if minL < maxR:
                width_real = Xs[maxR + 1] - Xs[minL]
                area = width_real * height_real
                if area > best_area:
                    best_area = area
            # Candidate 2: left = minR, right = maxL (in case red rows swapped)
            if minR < maxL:
                width_real = Xs[maxL + 1] - Xs[minR]
                area = width_real * height_real
                if area > best_area:
                    best_area = area

            i = j + 1

# print final answer (in original tile counts)
print(best_area)


