# import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# define the function that we can later use to animate
def update(frame):
    global positions, velocities, masses, scatters
    
    # update positions based on velocities
    positions += velocities
    
    # consider collissions with walls
    for i in range(len(positions)):
        if positions[i] < 0:
            positions[i] = 0
            velocities[i] = abs(velocities[i])
        elif positions[i] > box_length:
            positions[i] = box_length
            velocities[i] = -abs(velocities[i])
    
    # check for collisions between balls
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            if abs(positions[i] - positions[j]) < ball_radius * 2:
                # simple elastic collision
                v1_f = velocities[i] * (masses[i] - masses[j]) / (masses[i] + masses[j]) + \
                       2 * masses[j] * velocities[j] / (masses[i] + masses[j])
                v2_f = velocities[j] * (masses[j] - masses[i]) / (masses[i] + masses[j]) + \
                       2 * masses[i] * velocities[i] / (masses[i] + masses[j])
                velocities[i] = v1_f
                velocities[j] = v2_f
    
    # update scatter plots
    for i in range(len(positions)):
        scatters[i].set_offsets([[positions[i], 0]])

# initialize parameters
box_length = 10.0
ball_radius = 0.2
positions = np.array([1.0, 2.0, 3.0, 5.0, 8.0])
velocities = np.array([0.1, -0.15, 0.2, -0.25, 0.3])
masses = np.array([1.0, 1.0, 1, 1.0, 1.0])

# create the plot
fig, ax = plt.subplots()
ax.set_xlim(0, box_length)
ax.set_ylim(-1, 1)

# plot the balls
scatters = [ax.scatter(positions[i], 0, s=masses[i]*100, cmap='viridis', edgecolors='k', alpha=0.7) for i in range(len(positions))]

# create animation
animation = FuncAnimation(fig, update, frames=200, interval=50)

plt.show()
