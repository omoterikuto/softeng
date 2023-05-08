from xyrange import XYRange
from shape import Shape

class CircleS(Shape):    
    def inside(self, x: float, y: float) -> bool:
        return x * x + y * y <= 9.0

    def get_range(self) -> XYRange:
        return XYRange(-5.0, 5.0, 0.25, -5.0, 5.0, 0.5)