"""
Contians the Transform2 class, which represents the position and 
rotation of an object in 2D space.

Classes:
    Transform2: Represents the position and rotation of an object in 2D space.

"""

from typing import Type

from .vector2 import Vector2



class Transform2:
    """
    Represents the position and rotation of an object in 2D space.

    Attributes:
        position (Vector2): The position of the object
        rotation (float): The rotation of the object
    """

    def __init__(self, position : Vector2 = Vector2(0,0), rotation : float = 0) -> None:
        """
        Constructs a Transform2 object.

        Parameters:
            position (Vector2): The position of the object
            rotation (float): The rotation of the object in radians

        """

        self.position: Vector2 = position
        self.rotation: float = rotation


    def __add__(self, other : Type['Transform2']) -> Type['Transform2']:
        """
        Adds two transforms together by summing all of their 
        components and returns it.

        """
        return Transform2(self.position + other.position, 
                          self.rotation + other.rotation)
    

    def __sub__(self, other : Type['Transform2']) -> Type['Transform2']:
        """
        Subtracts one transform from another by taking the 
        difference of all of their components and returns it.

        """
        return Transform2(self.position - other.position, 
                          self.rotation - other.rotation)  

    def __str__(self) -> str:
        """
        Returns a string that contains the attributes of the transform.

        """
        return "Transform2 (" + str(self.position.x) + ", " + str(self.position.y) + ", " + str(self.rotation) + ")"

    def translate(self, distance : Vector2) -> Type['Transform2']:
        """
        Modifies only the position component by moving it a 
        constant distance, and returns it

        Parameters:
            distance (Vector2): The distance to move

        """
        return Transform2(self.position + distance, self.rotation)

    def rotate_locally(self, angle : float) -> Type['Transform2']:
        """
        Modifies only the rotation component by moving it a constant 
        distance, and returns it

        Parameters:
            angle (float): The radian angle to rotate

        """
        return Transform2(self.position, self.rotation + angle)


    def rotate_globally(self, angle : float) -> Type['Transform2']:
        """
        Returns a transform with a position component modified 
        by rotating it around the origin

        Parameters:
            angle (float): The radian angle to rotate

        """
        return Transform2(self.position.rotate(angle), self.rotation)