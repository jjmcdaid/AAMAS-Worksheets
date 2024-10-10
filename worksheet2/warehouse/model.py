from pydoc import doc
import mesa
import random
import numpy as np
from random import randint
from warehouse.agents import PickerRobot
from warehouse.agents import Box
from .agents import UNDONE



class Warehouse(mesa.Model):
    """ Model representing an automated warehouse"""
    def __init__(self, n_robots, n_boxes, width=50, height=50):
        """
            * Set schedule defining model activation
            * Sets the number of robots as per user input
            * Sets the grid space of the model
            * Create n Robots as required and place them randomly on the edge of the left side of the 2D space.
            * Create m Boxes as required and place them randomly within the model (Hint: To simplify you can place them in the same horizontal position as the Robots). Make sure robots or boxes do not overlap with each other.
        """
        super().__init__()
        # TODO implement
        self.running = True

    def step(self):
        """
        * Run while there are Undone boxes, otherwise stop running model.
        """
        # TODO implement