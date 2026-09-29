def slope(x):
    return -2 * (x - 2)              # slope of the hill f(x) = 4 - (x-2)^2

a = 0.0                              # left end of our search window
b = 3.0                              # right end of our search window
# slope(a) is +4 and slope(b) is -2: opposite signs, so the top must be between them

for step in range(1, 51):
    c = (a + b) / 2                  # look at the middle of the window
    print(f"step {step:2d}: window [{a:.4f}, {b:.4f}]  middle c = {c:.4f}  slope(c) = {slope(c):.4f}")

    if abs(slope(c)) < 0.00001:      # slope is basically zero: we found the top
        break

    if slope(a) * slope(c) > 0:      # same sign as the left end -> top is to the right of c
        a = c
    else:                            # different sign -> top is to the left of c
        b = c

print(f"\nFound the top at x = {c:.5f}")