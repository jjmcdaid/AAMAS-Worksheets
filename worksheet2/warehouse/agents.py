from optparse import check_builtin
import mesa

NUMBER_OF_CELLS = 50
BUSY = 0
FREE = 1
UNDONE = 0
DONE = 1

class PickerRobot(mesa.Agent):
    """Represents a Robot of the warehouse."""
    def __init__(self, id, pos, model, init_state=FREE):
        """
        Initialise state attributes, including:
          * current and next position of the robot
          * state (FREE/BUSY)
          * payload (id of any box the robot is carrying)
        """
        super().__init__(id, model)
        # TODO implement
  

    @property
    def isBusy(self):
        return self.state == BUSY

    def step(self):
        """
        * Obtain action as a result of deliberation
        * trigger action
        """
        # TODO implement

    # Robot decision model

    def deliberate(self):
        """
        
        Simple rule-based architecture, should determine the action to execute based on the robot state.

        """
        action = ""
        # TODO implement
        return action

    
    # Robot actions

    def move(self):
        """
        Move robot to the next position.
        """
        # TODO implement

    def move_payload(self):
        """
        * Obtains the box whose id is in the payload (Hint: you can use the method: self.model.schedule.agents to iterate over existing agents.)
        * move the payload together with the robot
        """
        # TODO implement

    def wait(self):
        """
        Keep the same position as the current one.
        """
        # TODO implement

    def move_fw(self):
        """
        Move the robot towards the boxes from left to right.
        """
        # TODO implement
    
    def move_bw(self):
        """
        Move the robot and the payload towards the collection point (right to left).
        """
        # TODO implement
        
    def pick(self):
        """
        * change robot state to Busy
        * find out the id of the box next to the robot
        * store the box id in the payload of the robot
        """
        # TODO implement
    
    def drop_off(self):
        """
        * change state of the robot to Free
        * Get the Box whose id is in the payload and remove it from the grid and change its state to Done.
        * Remove payload from robot
        * move agent to next position ahead of the box
        """
        # TODO implement
   
    def advance(self):
       """
       Advances position of the robot.
       """
       self.x = self.next_x
       self.y = self.next_y


class Box(mesa.Agent):
    """Represents a Box in the warehouse."""
    def __init__(self, id, pos, model, init_state=UNDONE):
        """
        Intialise state and position of the box
        """
        super().__init__(id, model)
        # TODO implement