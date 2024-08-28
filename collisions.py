import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
box_size = 10.0  # size of the box (10x10)
ball_radius = 0.3  # radius of the balls
dt = 0.01  # time step
num_steps = 1000  # number of steps in the simulation

class Ball:
    def __init__(self, position, velocity, radius, color):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.radius = radius
        self.color = color

    def move(self):
        self.position += self.velocity * dt

    def check_wall_collision(self):
        for i in range(2):  # checking both x and y directions
            if self.position[i] - self.radius < 0 or self.position[i] + self.radius > box_size:
                self.velocity[i] *= -1

    def check_ball_collision(self, other):
        # calculate distance between the balls
        dist = np.linalg.norm(self.position - other.position)
        if dist < self.radius + other.radius:
            # normal vector
            normal = (self.position - other.position) / dist
            # relative velocity
            relative_velocity = self.velocity - other.velocity
            # velocity along the normal
            velocity_along_normal = np.dot(relative_velocity, normal)
            
            if velocity_along_normal > 0:
                return  # balls are moving away from each other
            
            # elastic collision response
            self.velocity -= velocity_along_normal * normal
            other.velocity += velocity_along_normal * normal

# initialize balls with random positions and velocities
ball1 = Ball(
    position=[np.random.uniform(ball_radius, box_size-ball_radius),
              np.random.uniform(ball_radius, box_size-ball_radius)],
    velocity=[np.random.uniform(-2, 2), np.random.uniform(-2, 2)],
    radius=ball_radius,
    color='#EDD8CD'  
)

ball2 = Ball(
    position=[np.random.uniform(ball_radius, box_size-ball_radius),
              np.random.uniform(ball_radius, box_size-ball_radius)],
    velocity=[np.random.uniform(-2, 2), np.random.uniform(-2, 2)],
    radius=ball_radius,
    color='#37906D'  
)

ball3 = Ball(
    position=[np.random.uniform(ball_radius, box_size-ball_radius),
              np.random.uniform(ball_radius, box_size-ball_radius)],
    velocity=[np.random.uniform(-2, 2), np.random.uniform(-2, 2)],
    radius=ball_radius,
    color='#FF6347' 
)

# set up plot
fig, ax = plt.subplots()
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal', 'box') 

ball1_patch = plt.Circle(ball1.position, ball1.radius, color=ball1.color)
ball2_patch = plt.Circle(ball2.position, ball2.radius, color=ball2.color)
ball3_patch = plt.Circle(ball3.position, ball3.radius, color=ball3.color)
ax.add_patch(ball1_patch)
ax.add_patch(ball2_patch)
ax.add_patch(ball3_patch)

# animation
def update(frame):
    ball1.move()
    ball2.move()
    ball3.move()

    ball1.check_wall_collision()
    ball2.check_wall_collision()
    ball3.check_wall_collision()

    ball1.check_ball_collision(ball2)
    ball1.check_ball_collision(ball3)
    ball2.check_ball_collision(ball3)

    ball1_patch.set_center(ball1.position)
    ball2_patch.set_center(ball2.position)
    ball3_patch.set_center(ball3.position)

    return ball1_patch, ball2_patch, ball3_patch

ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=dt*1000, blit=True)

plt.show()
