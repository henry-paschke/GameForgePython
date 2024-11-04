"""
This module contains the State_machine class, which is a simple state machine.

Classes:
    State_machine: A simple state machine for managing game states or entities.
"""
from typing import Callable

class State_machine:
    """
    A simple state machine for managing game states or entities.

    Attributes:
        states (dict[str, Callable]): A dictionary of states and their update functions
        current_state (str): The current state of the state machine
        triggers (dict[str, Callable]): A dictionary of triggers and their functions
        suppressed_triggers (list[str]): A list of triggers that are currently suppressed
    """
    def __init__(self, states : dict[str, Callable] | dict[str, list[Callable, Callable]] , initial_state : str) -> None:
        """
        Constructs a state machine.

        Parameters:
            states (dict[str, Callable]): A dictionary of states 
            and their update functions, or a dictionary of states and their update functions and init functions in a list
            initial_state (str): The state that the state machine will start in
        """
        self.states: dict[str, Callable]  = states
        self.init_functions: dict[str, Callable] = {}
        for state, functions in states.items():
            if isinstance(functions, list):
                self.states[state] = functions[0]
                self.init_functions[state] = functions[1]
        self.current_state: str = initial_state
        self.triggers : dict[str, Callable] = {}
        self.suppressed_triggers: list[str] = []

    def update(self) -> None:
        """
        Calls the current state's update function.
        """
        self.states[self.current_state]()
        for state, trigger in self.triggers.items():
            if state not in self.suppressed_triggers:
                if trigger():
                    self.set_state(state)
                    break
        self.suppressed_triggers.clear()

    def add_init_function(self, state : str, function : Callable) -> None:
        """
        Adds a function to be called when the state machine enters a state.

        Parameters:
            state (str): The state that the function will be called in
            function (Callable): The function to be called
        """
        self.init_functions[state] = function

    def set_state(self, state : str) -> None:
        """
        Sets the current state of the state machine. 
        Calls the init function for that state.

        Parameters:
            state (str): The state to be set
        """
        if self.current_state != state:
            self.current_state = state
            if state in self.init_functions:
                self.init_functions[state]()

    def get_state(self) -> str:
        """
        Returns the current state of the state machine.
        """
        return self.current_state
    
    def add_state(self, state : str, 
                  function : Callable, 
                  init_function : Callable = None
                  ) -> None:
        """
        Adds a state to the state machine.

        Parameters:
            state (str): The state to be added
            function (Callable): The function to be called 
                when the state is active
        """
        self.states[state] = function
        if init_function != None:
            self.init_functions[state] = init_function

    def add_trigger(self, state : str, trigger : Callable) -> None:
        """
        Adds a trigger to the state machine.
        Triggers are checked every frame, and if they return true, 
        the state machine will enter the state that the trigger is attached to.

        Parameters:
            state (str): The state that the trigger will be added to
            trigger (Callable): The function to be called when the trigger 
                is activated
        """
        self.triggers[state] = trigger

    def suppress_triggers(self, suppressed_triggers : list[str]) -> None:
        """
        Suppresses all listed triggers in the state machine for the next frame.
        """
        self.suppressed_triggers = suppressed_triggers