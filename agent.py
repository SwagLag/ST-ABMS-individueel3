from mesa import Agent

class MAgent(Agent):
    """An agent who starts with a set amount of money."""
    def __init__(self, identification, model):
        super().__init__(identification, model)
        self.money = 100
        self.happy = True  # Is blij als hij geld heeft weggegeven, niet blij als hij beroofd is.
        self.state = 1
        self.neighbors = []
        # Stage 1: Genoeg geld, gewoon geld uitgeven
        # Stage 2: Niet genoeg geld, geld stelen

    def move(self):
        """Moves to a (random) adjectant cell."""
        possible_cells = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_cells)
        self.model.grid.move_agent(self,new_position)

    def see(self):
        """Gets all neighboring agents (if there's any)"""
        neighbors = []  # Reset the perception.
        possible_cells = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=True
        )
        for cell in possible_cells:
            neighbors.append(self.model.grid.get_cell_list_contents([cell]))
        unnested = [filtered for lst in neighbors for filtered in lst]
        self.neighbors = unnested

    def update(self):
        """Updates the agent's stage based on the amount of
        money he has."""
        if self.money >= 10:
            self.state = 1  # Genoeg geld, voorlopig.
        elif self.money < 10:
            self.state = 2  # Hey, weinig geld. Tijd om wat geld te gaan 'halen'...

    def act(self):
        """Gives money to a (random) adjectant agent. If there's
        no agents, does nothing."""
        self.move()  # Altijd eerst ergens random naar toe.
        self.see()
        if self.state == 1:
            if len(self.neighbors) > 1:  # We willen een element van willekeurigheid
                target = self.random.choice(self.neighbors)
                money = self.random.randrange(self.money)
                self.transfer(target,money)
                self.happy = True  # Je hebt iets moois gedaan met je geld.
        elif self.state == 2:
            if len(self.neighbors) > 1:
                target = self.random.choice(self.neighbors)
                money = self.random.randrange(target.money)
                self.transfer(target,-money)
                target.happy = False  # Het is toch niet zo fijn om je geld te verliezen

    def transfer(self, agent, money):
        """Transfers an amount of money to an agent and deducts it from
        their own balance."""
        agent.money += money
        self.money -= money

    def step(self):
        # What the agent does goes here.
        # self.move()
        self.update()
        self.act()