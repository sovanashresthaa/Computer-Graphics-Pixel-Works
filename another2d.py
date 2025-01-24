import numpy as np
import matplotlib.pyplot as plt

# Define a 2D object (triangle) by its vertices (x, y)
triangle = np.array([
    [0, 0],   # Vertex 1
    [1, 0],   # Vertex 2
    [0.5, 1]  # Vertex 3
])

# Function to apply a transformation matrix to an object
def apply_transformation(vertices, transformation_matrix):
    # Convert vertices to homogeneous coordinates by adding a third dimension (z=1)
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    # Apply transformation
    transformed_vertices = (transformation_matrix @ vertices_homogeneous.T).T
    return transformed_vertices[:, :2]

# Define 2D transformation matrices

# 1. Translation Matrix (tx, ty)
tx, ty = 2, 1
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
])

# 2. Scaling Matrix (sx, sy)
sx, sy = 1.5, 1.5  # Scaling by 1.5 in both directions
scaling_matrix = np.array([
    [sx, 0, 0],
    [0, sy, 0],
    [0, 0, 1]
])

# 3. Rotation Matrix (angle in degrees)
angle_deg = 45  # Rotate 45 degrees counterclockwise
angle_rad = np.radians(angle_deg)  # Convert to radians
rotation_matrix = np.array([
    [np.cos(angle_rad), -np.sin(angle_rad), 0],
    [np.sin(angle_rad), np.cos(angle_rad), 0],
    [0, 0, 1]
])

# Combine the transformations: Apply rotation, then scaling, then translation
combined_transformation = translation_matrix @ scaling_matrix @ rotation_matrix

# Apply the transformations to the triangle
transformed_triangle = apply_transformation(triangle, combined_transformation)

# Plot the original and transformed triangle
plt.figure(figsize=(6, 6))

# Original triangle
plt.plot(triangle[:, 0], triangle[:, 1], label="Original Triangle", color="blue", marker='o')

# Transformed triangle
plt.plot(transformed_triangle[:, 0], transformed_triangle[:, 1], label="Transformed Triangle", color="red", marker='o')

# Add labels and legend
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('2D Transformations: Translation, Scaling, Rotation')
plt.legend()

# Show plot
plt.show()