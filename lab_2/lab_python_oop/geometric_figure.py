from math import pi
from abc import ABC

class GeometricFigure(ABC):
    def __init__(self, type_figure:str = "", lengt_figure:int = 0, width_figure:int = 0, radius_figure:int = 0, color_figure:str = None) -> None:
        super().__init__()
        self.type_figure = type_figure
        self.lengt_figure = lengt_figure
        self.width_figure = width_figure
        self.radius_figure = radius_figure
        self.color_figure = color_figure
        self.get_area()
    
    def get_area(self) -> float:
        self.area = 0
        if self.type_figure == "Прямоугольник" or self.type_figure == "Квадрат":
            self.area = self.lengt_figure * self.width_figure 
        elif self.type_figure == "Круг":
            self.area = pi * self.radius_figure**2
        return self.area
        
    def get_type_figure(self) -> str: 
        return self.type_figure   
        
    def repr(self) -> str:
        str_return = "Сводная информация по фигуре:"
        if len(self.type_figure):
            str_return += "\n Тип фигуры -  {}".format(self.type_figure) 
        if self.lengt_figure !=0:
            str_return += "\n Длинна: {} - {} ".format(self.type_figure, self.lengt_figure) 
        if self.width_figure !=0:
            str_return += "\n Ширина: {} - {} ".format(self.type_figure, self.width_figure) 
        if self.radius_figure !=0:
            str_return += "\n Радиус: {} - {} ".format(self.type_figure, self.radius_figure) 
        if self.color_figure is not None:
            str_return += "\n Цвет: {} - {} ".format(self.type_figure, self.color_figure)
        if self.area != 0:
            str_return += "\n Площадь: {} - {} ".format(self.type_figure, self.area)  
        str_return += "\n"       

        return str_return           
        
     