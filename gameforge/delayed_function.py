"""
This module contains the Delayed_function class. 
This class is used to store a function with no parameters to later be called.

Classes:
    Delayed_function: Stores a function with no parameters to later be called
"""

from typing import Callable

class Delayed_function:
    """
    Stores a function with no parameters to later be called.

    Attributes:
        length (int): The time in milliseconds before the function is called
        time_elapsed (int): The number of milliseconds elapsed since this 
        class was constructed or reset
        function (function): The function to be called

    """
    def __init__(self, length : int, function : Callable) -> None:
        """
        Constructs a delayed function and begins tracking time.

        Parameters:
            length (int): How many milliseconds until the function is called
            function (function): The function with no parameters to call 
                after the time has passed

        """
        self.length: int = length
        self.time_elapsed: int = 0
        self.function: Callable = function

    def update(self, dt : int) -> bool:
        """
        Updates the process' internal clock to match the game's delta time. 
        If enough time has elapsed, the function is called.
        Returns a bool indicating whether or not to continue updating the process.

        Parameters:
            dt (int) : The time in milliseconds since the last update

        """
        self.time_elapsed += dt

        if self.time_elapsed > self.length:
            self.function()
            return False
        return True
    
    def reset(self) -> None:
        """
        Resets the process to begin again.

        """
        self.time_elapsed = 0

    def check_done(self) -> bool:
        """
        Returns a bool indicating whether or not the process has finished.

        """
        return self.time_elapsed > self.length