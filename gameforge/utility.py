"""
Contains common functions and classes utilized frequently 
in the game development process.

Functions:
    clamp: Clamps a value between a minimum and maximum value
    lerp: Linearly interpolates between two values
    flip_around: Flips a point around a center point
    get_multiples: Gets all multiples of x between start and end
    
"""

def clamp(value : int | float, min_value: int | float, max_value: int | float) -> int | float:
    """
    Returns the value clamped between the max and min values. 

    Parameters:
        value (int or float): The value to be clamped
        min_value (int or float): The minimum possible value
        max_value (int or float): The maximum possible value

    """
    return max(min(value, max_value), min_value)


def lerp(start : int | float, end : int | float, lerp_speed : int | float) -> int | float:
    """
    Linearly interpolates between two values.

    Parameters:
        start (int or float): The start value
        end (int or float): The end value
        lerp_speed (int or float): The speed at which to interpolate
    """
    return (1 - lerp_speed) * start + lerp_speed * end


def flip_around(point : float, center : float) -> float:
    """
    Flips a point around a center point.

    Parameters:
        point (float): The point to flip
        center (float): The point to flip around
    """
    distance = point - center
    return center - distance

def get_multiples(x: int, start, end) -> list[int]:
    """
    Gets all multiples of x between start and end.
    """
    return [i for i in range(start, end+1) if i % x == 0]