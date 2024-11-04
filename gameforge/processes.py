"""
A number of self-contained processes and functions to allow 
for simple and effective implementations.

Classes:
    Linear_process: A linear interpolation process
    Angular_linear_process: A linear interpolation process for radian angles
    Transform_linear_process: A linear interpolation process for Transform2 objects

"""

# Other Engines
from numpy import pi

# Utilities
from .vector2 import Vector2
from .transform2 import Transform2

# Constants
TWO_PI = pi*2

class Linear_process():
    """
    Stores all the data used to linear interpolate a number or vector. 
    Theoretically works with any data type that has addition, 
    subtraction, and multipication overloaded.
    This object is intended to be disposed of. 
    Each process should simply create a new instance.

    Attributes:
        start (float, Vector2): The start position of the process
        end (float, Vector2): The end position of the process
        length (int): The length in milliseconds that this process will take
        elapsed (int): The number of milliseconds elapsed 

    Methods:
        update(float): increments the elapsed counter
        get_pos(): Returns the number or vector interpolated 
            according to the process attributes
        finish(): Finishes the process regardless of time elapsed

    """

    def __init__(self, 
                 start : float | Vector2, 
                 end : float | Vector2, 
                 length : int
                 ) -> None:
        """
        Constructs a linear process. 
        The process sets its internal timer to 0 and begins tracking time.

        Parameters:
            start (float, Vector2): The start position of the process
            end (float, Vector2): The end position of the process
            length (int): The length in milliseconds that this process will take

        """
        self.start: float | Vector2 = start
        self.end: float | Vector2 = end
        self.length: int = length
        self.elapsed: int = 0
    
    def update(self, dt : int) -> None:
        """
        Updates the process' internal clock to match the game's delta time.
        This method does not do anything on its own.

        Parameters:
            dt (int) : The time in milliseconds since the last update

        """
        self.elapsed += dt
        
    def get_pos(self) -> float | Vector2:
        """
        Finds the position of the process by using linear interpolation.
        Returns whatever data type was passed into the constructor.

        """
        if self.elapsed > self.length:
            return self.end
        else:
            return self.start + ((self.end - self.start) * 
                                 (self.elapsed/self.length))
        
    def finish(self) -> None:
        """
        Artificially completes the process.

        """
        self.elapsed = self.length + 1

    def check_done(self) -> bool:
        """
        Checks if the process is done.

        Returns:
            bool: True if the process is done, False otherwise.

        """
        return self.elapsed > self.length
    
class Angular_linear_process(Linear_process):
    """
    A child of the linear process, the angular linear process.
    does some extra calculations beforehand to ensure the quickest route is taken.
    Stores all the data used to linear interpolate an angle. 
    This object is intended to be disposed of. 
    Each process should simply create a new instance.

    Attributes:
        start (float): The start angle of the process. 
            This angle will be between 0 and 2π.
        end (float): The end angle of the process. 
            This will be between -2π and 4π, whichever iteration 
            of the angle is closest to the start angle.
        length (int): The length in milliseconds that this process will take
        elapsed (int): The number of milliseconds elapsed

    Methods:
        update(float): increments the elapsed counter
        get_pos(): Returns the angle interpolated accourding 
            to the process attributes


    """
    def __init__(self, start, end, length) -> None:
        """
        Constructs an angular linear process. 
        The process sets its internal timer to 0 and begins tracking time.
        Angles will be clamped to allow for the shortest path possible.

        Parameters:
            start (float): The start angle of the process. 
            end (float): The end angle of the process.
            length (int): The length in milliseconds that this process will take

        """

        self.start: float | Vector2 = start % TWO_PI
        self.end: float | Vector2 = end % TWO_PI
        self.length: int = length
        self.elapsed: int = 0

        if self.start - self.end > pi:
            self.end += TWO_PI
        if self.start - self.end < -pi:
            self.end -= TWO_PI

    

class Transform_linear_process:
    """
    A process that linearly interpolates a Transform2 object.
    Wraps an instance of Linear_process and Angular_linear_process.
    This object is intended to be disposed of. Each process should simply create a new instance.

    Attributes:

    position_process (Linear_process): The linear process for the position
    rotation_process (Angular_linear_process): The angular linear process for the rotation
    """
    def __init__(self, start: Transform2, end: Transform2, length: int) -> None:
        """
        Constructs a transform linear process.

        Parameters:
            start (Transform2): The start transform of the process
            end (Transform2): The end transform of the process
            length (int): The length in milliseconds that this process will take
        """
        self.position_process = Linear_process(start.position, end.position, length)
        self.rotation_process = Angular_linear_process(start.rotation, end.rotation, length)

    def update(self, dt: int) -> None:
        """
        Updates the process' internal clock to match the game's delta time.
        """
        self.position_process.update(dt)
        self.rotation_process.update(dt)
    
    def get_pos(self) -> Transform2:
        """
        Returns the position of the process by using linear interpolation.
        """
        return Transform2(self.position_process.get_pos(), self.rotation_process.get_pos())
    
    def finish(self) -> None:
        """
        Artificially completes the process.
        """
        self.position_process.finish()
        self.rotation_process.finish()

    def check_done(self) -> bool:
        """
        Checks if the process is done.
        """
        return self.position_process.check_done() and self.rotation_process.check_done()
    