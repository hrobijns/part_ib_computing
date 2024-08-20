import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# constants
G = 6.67430e-11  # m^3 kg^-1 s^-2

# planet class
class Planet:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

def gravitational_force(m1, m2, r):
    # calculate gravitational force between two masses
    force_magnitude = G * (m1 * m2) / r**2
    force_direction = r / np.linalg.norm(r)
    force = force_magnitude * force_direction
    return force

def update_position_velocity(planet, force, dt):
    # update position and velocity using Euler's method
    acceleration = force / planet.mass
    planet.velocity += acceleration * dt
    planet.position += planet.velocity * dt

# function to initialize the plot
def init():
    ax.set_xlim(-2e11, 2e11)
    ax.set_ylim(-2e11, 2e11)
    return []

# function to update the plot for each animation frame
def update(frame):
    for planet in planets:
        # calculate net force on the planet
        net_force = np.array([0.0, 0.0])
        for other_planet in planets:
            if other_planet != planet:
                r = other_planet.position - planet.position
                force = gravitational_force(planet.mass, other_planet.mass, np.linalg.norm(r))
                net_force += force
        # update position and velocity
        update_position_velocity(planet, net_force, dt)

    # update plot data
    lines.set_data([planet.position[0] for planet in planets], [planet.position[1] for planet in planets])
    return lines,

# create a Sun
sun = Planet(mass=1.989e30, position=[0, 0], velocity=[0, 0])

# create a planet (e.g., Earth)
earth = Planet(mass=5.972e24, position=[1.5e11, 0], velocity=[0, 30000])

# set up the simulation parameters
planets = [sun, earth]
dt = 60*60  # time step size in seconds

# set up the plot
fig, ax = plt.subplots()
lines, = ax.plot([], [], 'o', markersize=10)

# create the animation
animation = FuncAnimation(fig, update, frames=range(500), init_func=init, blit=True, interval=50)

# show the animation
plt.show()
