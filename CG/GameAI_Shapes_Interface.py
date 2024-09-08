from abc import ABC

class DrawShapes(ABC):
    """
    `ObjectShapes` interface.
    """

    def draw_shape(self) -> int:
        """
        Should add shapes to the container
        """
        # default implementation
        return 0
