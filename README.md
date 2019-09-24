# Particle Swarm Optimization

Particle swarm optimization is tool in the evolutionary computation arsenal. It involves swarms of "particles" whose positions correspond to candidate solutions in a search space. The velocity of the particles changes their positions. In the most basic form, velocity is computed by adding the following vectors at each iteration:

- Particle Inertia (Previous Velocity)
- Cognitive Force (Distance To Best Previous Position of Particle)
- Social Force (Distance To Best Previous Position of Swarm)

The original research paper on PSO was published by James Kennedy and Russell Eberhart and can be viewed [here](https://ieeexplore.ieee.org/document/488968).

Finally, the example demonstrated in this repository is trivial. It can be thought of PSO in the simplest form. A more comprehensive research platform for PSO written in Python can be found [here](https://github.com/ljvmiranda921/pyswarms).