from lab_python_oop.rectangle import Rectangle 
from lab_python_oop.circle import Circle 
from lab_python_oop.square import Square
import requests
 

def main():
    rectangle = Rectangle(lengt_figure=14, width_figure=14, color_figure="Синий")
    print (rectangle.repr())
    circle = Circle(color_figure="Зеленый", radius_figure=14)
    print (circle.repr())
    square = Square(color_figure="Красный", lengt_figure=14)
    print (square.repr())
    respons = requests.get('https://yandex.ru')
    print(respons.content)


if __name__ == '__main__':
    main()  