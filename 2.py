import matplotlib.pyplot as plt
import numpy as np

def koch_segment(p1, p2, depth):
    if depth == 0:
        return [p1, p2]
    
    pA = p1 + (p2 - p1) / 3
    pB = p1 + 2 * (p2 - p1) / 3

    rotation_matrix = np.array([[0.5, -np.sqrt(3)/2], [np.sqrt(3)/2, 0.5]])
    
    v_segment = pB - pA
    
    pC_relative = np.dot(rotation_matrix, v_segment)
    pC = pA + pC_relative

    points = []
    points.extend(koch_segment(p1, pA, depth - 1))
    points.extend(koch_segment(pA, pC, depth - 1))
    points.extend(koch_segment(pC, pB, depth - 1))
    points.extend(koch_segment(pB, p2, depth - 1))
    
    return points

def plot_koch_snowflake(depth):
    side_length = 100.0
    h = side_length * np.sqrt(3) / 2
    
    p1 = np.array([0.0, 0.0], dtype=float)
    p2 = np.array([side_length, 0.0], dtype=float)
    p3 = np.array([side_length / 2, h], dtype=float)

    offset_x = -side_length / 2
    offset_y = -h / 2
    
    p1 += np.array([offset_x, offset_y], dtype=float)
    p2 += np.array([offset_x, offset_y], dtype=float)
    p3 += np.array([offset_x, offset_y], dtype=float)

    points1 = koch_segment(p1, p2, depth)
    points2 = koch_segment(p2, p3, depth)
    points3 = koch_segment(p3, p1, depth)

    all_points = points1 + points2 + points3

    x_coords = [p[0] for p in all_points]
    y_coords = [p[1] for p in all_points]

    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])

    plt.figure(figsize=(8, 8))
    plt.plot(x_coords, y_coords, color='blue')
    plt.title(f"Сніжинка Коха (Ітерація: {depth})")
    plt.axis('equal')
    plt.axis('off')
    plt.show()


plot_koch_snowflake(depth=4)