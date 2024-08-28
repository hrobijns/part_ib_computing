import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989e30  # mass of the sun (kg)
dt = 60 * 60   # time step (seconds)
planet_radius = 0.5e10  # visualization size of the planet
sun_radius = 1.0e10  # visualization size of the sun
num_steps = 1000 # frames in the simulation

class Planet:
    def __init__(self, position, velocity, mass, radius, color):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
        self.radius = radius
        self.color = color

    def move(self):
        r = np.linalg.norm(self.position)
        force_magnitude = G * M_sun * self.mass / r**2
        force_direction = -self.position / r
        acceleration = force_magnitude * force_direction / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

# initialize the planet with specific initial conditions
planet = Planet(
    position=[1.496e11, 0],  # initial position (meters)
    velocity=[0, 29783],     # initial velocity (meters/second)
    mass=5.972e24,           # mass of the planet (kg)
    radius=planet_radius,   
    color='#862323'
)

# set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-2e11, 2e11)
ax.set_ylim(-2e11, 2e11)
ax.set_aspect('equal', 'box')
ax.set_xticks([])
ax.set_yticks([])

planet_patch = plt.Circle(planet.position, planet.radius, color=planet.color)
sun_patch = plt.Circle((0, 0), sun_radius, color='#FFCA00')

ax.add_patch(planet_patch)
ax.add_patch(sun_patch)

# animation
def update(frame):
    planet.move()
    planet_patch.set_center(planet.position)
    return planet_patch,

ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=dt*0.001, blit=True)
plt.show()