import numpy as np

# f(x, y, z) = (x-1)^2 + (y+2)^2 + z^4 - 4z
def gradient(v):
    x, y, z = v
    slope_x = 2 * (x - 1)
    slope_y = 2 * (y + 2)
    slope_z = 4 * z**3 - 4                    # slope of z^4 - 4z
    return np.array([slope_x, slope_y, slope_z])

v = np.array([0.0, 0.0, 0.0])
alpha = 0.1

for step in range(1, 1001):
    g = gradient(v)
    if np.linalg.norm(g) < 0.000001:
        break
    v = v - alpha * g

print(f"Stopped after {step - 1} steps at {v.round(4)}")