"""
Contains several classes that provide simple and encapsulated 
solutions to common game development problems.

"""

from .vector2 import Vector2
from .transform2 import Transform2
from .state_machine import State_machine
from .delayed_function import Delayed_function
from .utility import clamp, lerp, flip_around, get_multiples
from .processes import Linear_process, Angular_linear_process, Transform_linear_process