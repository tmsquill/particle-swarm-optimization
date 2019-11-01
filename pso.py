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

    """
    Represents an individual particle in the search space.
    """

    def __init__(self, parameters):

        # The position of the particle.
        self.position = parameters

        # The velocity of the particle.
        self.velocity = [random.uniform(-1, 1) for _ in range(len(parameters))]

        # The highest-performing previous location of the particle.
        self.pos_best = []

        # The best performance value discovered so far of the particle.
        self.value_best = -1

        # The performance value of the particle.
        self.value = -1

    def __repr__(self):

        return f"Position: {self.position} Value: {self.value}"

    def __str__(self):

        return repr(self)

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
        cog_force = 1

        # Social constant. Used for calculating social force vector.
        soc_force = 2

        # Constant inertia weight (how much to weigh the previous velocity).
        inertia = 0.5

        for i in range(len(self.position)):

            r1 = random.random()
            r2 = random.random()

            # Calculate cognitive velocity.
            vel_cognitive = cog_force * r1 * (self.pos_best[i] - self.position[i])

            # Calculate social velocity.
            vel_social = soc_force * r2 * (pos_best_g[i] - self.position[i])

            # Update velocity of the particle. Velocity value is calculated by
            # adding the sum of the cognitive vector (pointing to personal
            # best), the social vector (pointing to swarm best) and the current
            # velocity multiplied by some inertia weight.
            self.velocity[i] = inertia * self.velocity[i] + vel_cognitive + vel_social

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

    """
    Represents a swarm of particles in the search space. Orchestrates the
    behavior of particles.
    """

    def __init__(self, initial_position, bounds, particle_count, iters):

        global num_dimensions
        num_dimensions = len(initial_position)
        self.best = None
        self.particle_count = particle_count
        self.bounds = bounds
        self.iters = iters

        # Create the swarm.
        self.swarm = [Particle(initial_position) for _ in range(particle_count)]

    def optimize(self, cost_func):

        for _ in range(self.iters):

            # Evaluate fitness for each particle.
            for particle in self.swarm:

                particle.evaluate(cost_func)

                # Check if particle is best performing in the swarm.
                if not self.best or particle.value < self.best.value:

                    self.best = particle

            # Update position and velocity of each particle.
            for particle in self.swarm:

                particle.update_velocity(self.best.position)
                particle.update_position(self.bounds)

        # Print the best-performing particle.
        print(f"Best Particle -> {self.best}")

# Create the swarm and optimize.
swarm = Swarm(
    [5, 5, 5, 5],                                 # Position
    [(-10, 10), (-10, 10), (-10, 10), (-10, 10)], # Bounds
    15,                                           # Particle Count
    300                                           # Iterations
)
swarm.optimize(cost_function)
