from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.color_figure import ColorFigure

class Rectangle(GeometricFigure):
    def __init__(self, type_figure:str = "Прямоугольник", lengt_figure:int = 0, width_figure:int = 0, radius_figure:int = 0, color_figure:str = None) -> None:
        super().__init__(type_figure, lengt_figure, width_figure, radius_figure, color_figure)        
        self.get_area()
        self.color_propertis = ColorFigure(Rectangle)
        

    def get_area(self):
        self.area = self.lengt_figure * self.width_figure
        return self.area

