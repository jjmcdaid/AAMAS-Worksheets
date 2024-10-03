import mesa

class Cell(mesa.Agent):

    DEAD = 0
    ALIVE = 1

    def __init__(self, pos, model, init_state=DEAD):

        super().__init__(pos, model)
        self.x, self.y = pos
        self.state = init_state
        self.nextState = None

    @property
    def isAlive(self):
        return self.state == self.ALIVE

    @property
    def neighbors(self):
        return self.model.grid.iter_neighbors((self.x, self.y), True)

    def step(self):
        live_neighbors = sum(neighbor.isAlive for neighbor in self.neighbors)

        self._nextState = self.state

        if self.isAlive:
            if live_neighbors < 2 or live_neighbors > 3:
                self._nextState = self.DEAD
        else:
            if live_neighbors == 3:
                self._nextState = self.ALIVE

    def advance(self):
        self.state = self._nextState


class ConwaysGameOfLife(mesa.Model):

    def __init__(self, width=50, height=50):
        self.schedule = mesa.time.SimultaneousActivation(self)

        self.grid = mesa.space.SingleGrid(width, height, torus=True)

        for contents, (x, y) in self.grid.coord_iter():
            cell = Cell((x, y), self)
            if self.random.random() < 0.1:
                cell.state = cell.ALIVE
            self.grid.place_agent(cell, (x, y))
            self.schedule.add(cell)
        
        self.running = True
    
    def step(self):
        self.schedule.step()


def portrayCell(cell):

    if cell is None:
        raise AssertionError

    return {
        "Shape": "rect",
        "w": 1,
        "h": 1,
        "Filled": "true",
        "Layer": 0,
        "x": cell.x,
        "y": cell.y,
        "Color": "black" if cell.isAlive else "white",
    }


canvas_element = mesa.visualization.CanvasGrid(portrayCell, 50, 50, 250, 250)

server = mesa.visualization.ModularServer(
    ConwaysGameOfLife, [canvas_element], "Game of Life", {"height": 50, "width": 50}
)


server.launch()