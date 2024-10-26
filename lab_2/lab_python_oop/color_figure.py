from lab_python_oop.geometric_figure import GeometricFigure

class ColorFigure():
    def __init__(self, figure:GeometricFigure) -> None:
        self.geometric_figure = figure
        # self.color_figure = color_figure

    def get_color(self) -> str:
        if hasattr(self.geometric_figure, 'color_figure'):
            return self.geometric_figure.color_figure
        else:
            return "Класс geometric_figure не имеет свойства color_figure"

    def set_color(self, value) -> None:
        self.geometric_figure.color_figure = value 

    def dell_color(self) -> None:
        del self.geometric_figure.color_figure

    property_color = property(get_color, set_color, dell_color, "Свойство 'Цвет фигуры'.")    

