import numpy as np
 
def gradient(v):
    x, y = v                                  # unpack the position into x and y
    slope_x = 2 * x - y - 4
    slope_y = -x + 2 * y - 6
    return np.array([slope_x, slope_y])

v = np.array([0.0, 0.0])                      # starting position: x = 0, y = 0
alpha = 0.1                                   # step size

for step in range(1, 1001):
    g = gradient(v)                           # the slope where we're standing
    if np.linalg.norm(g) < 0.000001:          # ground is flat: we're at the bottom
        break
    v = v - alpha * g                         # step DOWNhill (minus), in x and y at once

print(f"Stopped after {step - 1} steps at {v.round(3)}")