from circle import Circle
from rectangle import Rectangle
from square import Square

class ShapeFactory():
    def get_shape(self, shape_type: str) -> object:
        if(shape_type is None):
            return None

        if(shape_type == 'Circle'):
            return Circle()

        if(shape_type == 'Rectangle'):
            return Rectangle()

        if(shape_type == 'Square'):
            return Square()

        return None        