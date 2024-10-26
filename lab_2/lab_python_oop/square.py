from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color_figure import ColorFigure

class Square(Rectangle):
    def __init__(self, type_figure:str = "Квадрат", lengt_figure:int = 0, width_figure:int = 0, radius_figure:int = 0, color_figure:str = None) -> None:
        super().__init__(type_figure, lengt_figure, width_figure, radius_figure, color_figure)
        self.width_figure = lengt_figure
        self.color_propertis = ColorFigure(Square)
        self.get_area()
        # color_figure.property_color = "Небесно-голубой"


    def get_area(self):
        self.area = self.lengt_figure * self.width_figure
        return self.area

