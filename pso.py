import random


def cost_function(position):

    """
    The cost function takes the position of the particle and evaluates the
    performance by running some experiment that utilizes the position. Keep in
    mind that the position of a particle is effectively it's location in the
    N-dimensional search-space.
    """

    return sum([x * x for x in position])


class Particle:
    def __init__(self, parameters):

        # The position of the particle.
        self.position = [parameter for parameter in parameters]

        # The velocity of the particle.
        self.velocity = [random.uniform(-1, 1) for _ in range(len(parameters))]

        # The highest-performing previous location of the particle.
        self.pos_best = []

        # The best performance value discovered so far of the particle.
        self.value_best = -1

        # The performance value of the particle.
        self.value = -1

    def evaluate(self, cost_func):

        """
        Evaluate the performance of the particle by applying it's current
        position to the cost function.
        """

        self.value = cost_func(self.position)

        # Keep track of highest performing position and value.
        if self.value < self.value_best or self.value_best == -1:

            self.pos_best = self.position
            self.value_best = self.value

    def update_velocity(self, pos_best_g):

        """
        Update the velocity of the particle.
        """

        # Cognitive constant. Used for calculating cognitive force vector.
        c1 = 1

        # Social constant. Used for calculating social force vector.
        c2 = 2

        # Constant inertia weight (how much to weigh the previous velocity).
        w = 0.5

        for i in range(len(self.position)):

            r1 = random.random()
            r2 = random.random()

            # Calculate cognitive velocity.
            vel_cognitive = c1 * r1 * (self.pos_best[i] - self.position[i])

            # Calculate social velocity.
            vel_social = c2 * r2 * (pos_best_g[i] - self.position[i])

            # Update velocity of the particle.
            self.velocity[i] = w * self.velocity[i] + vel_cognitive + vel_social

    def update_position(self, bounds):

        """
        Update the position of the particle.
        """

        for i in range(len(self.position)):

            self.position[i] = self.position[i] + self.velocity[i]

            # Adjust maximum position if necessary.
            if self.position[i] > bounds[i][1]:

                self.position[i] = bounds[i][1]

            # Adjust minimum position if neseccary.
            if self.position[i] < bounds[i][0]:

                self.position[i] = bounds[i][0]


class Swarm:
    def __init__(self, x0, bounds, particle_count, max_iter):

        global num_dimensions
        num_dimensions = len(x0)
        self.best = None
        self.particle_count = particle_count
        self.max_iter = max_iter

        # Create the swarm.
        self.swarm = [Particle(x0) for _ in range(particle_count)]

    def optimize(self, cost_func):

        for _ in range(self.max_iter):

            # Evaluate fitness for each particle.
            for particle in self.swarm:

                particle.evaluate(cost_func)

                # Check if particle is best performing in the swarm.
                if not self.best or particle.value < self.best.value:

                    self.best = particle

            # Update position and velocity of each particle.
            for particle in self.swarm:

                particle.update_velocity(self.best.position)
                particle.update_position(bounds)

        # Print results.
        print(f"Best Position -> {self.best.position}")
        print(f"Best Value    -> {self.best.value}")


initial_position = [5, 5, 5, 5]
bounds = [(-10, 10), (-10, 10), (-10, 10), (-10, 10)]

# Create the swarm and optimize.
swarm = Swarm(initial_position, bounds, 15, 300)
swarm.optimize(cost_function)
