import random  # Random is al ingebouwd in mesa, dus deze import wordt feitelijk nooit gebruikt.

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from agent import *

def compute_gini(model):
    agent_wealths = [agent.money for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.agent_count
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B

class MModel(Model):
    """The environment(?) in which the simulation takes place(??)"""
    def __init__(self, agent_count,width,height):

        self.agent_count = agent_count  # Might wanna save it for reference I suppose
        self.schedule = RandomActivation(self)  # Runs step() on agents in random order each time step() is called on this object
        self.grid = MultiGrid(width,height,True)  # Waar is de True voor?
        self.running = True  # Model is aan de slag; als deze false is beëindigt hij.

        for i in range(agent_count):
            a = MAgent(i,self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.datacollector = DataCollector(
            model_reporters={"Gini":compute_gini},
            agent_reporters={"Money":"money"})

    def step(self):
        """Advance time by one step"""
        self.datacollector.collect(self)
        self.schedule.step()
