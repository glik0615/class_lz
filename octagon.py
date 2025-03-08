import matplotlib.pyplot as plt
import math
from math import sqrt, sin, cos, pi
import matplotlib.patches as pat
import numpy as np

# Создаем класс "Октагон". Вводим необходимые атрибуты и методы
class Octagon:
    def __init__(self,length):
        
        self.length = length
        # Вводим "константные" атрибуты
        self.angle = 135
        self.const = 1  + sqrt(2)
    #----------------------------------------------------------



    # Вводим функцию, находящая значения радиуса и площади для
    #  описанной окружности соответственно
    def circumscribed(self): 

        R = self.length / sqrt(2-sqrt(2))
        print(f"Радиус описанной окружности равен",{R})
        S = (pi * (R**2))
        print(f"Площадь описанной окружности равна",{S})
        

    # Вводим функцию, находящая значения радиуса и площади для
    #  вписанной окружности соответственно
    def inscribed(self): 

        r = self.length / (2*(sqrt(2)-1)) #нахождение радиуса вписанной 
        print(f" Радиус вписанной окружности равен",{r})
        S = (pi * (r**2)) #нахождение площади вписанной
        print(f"площадь вписанной",{S})


    # Вводим функцию, находящая значения площади и периметра для
    #  октагона соответственно
    def octagon(self):

        S = (2 * (self.length**2))*self.const
        print(f"Площадь октагона равна",{S})
        P = 8 * self.length
        print(f"Периметр октагона равен",{P})
        R = self.length / sqrt(2 - sqrt(2))

 # Вводим функцию, создающую график, на котором будут отображены все фигуры, с которыми мы работали
    def graph(self): 

        r_cir = self.length / sqrt(2-sqrt(2))
        r_in = self.length / (2*(sqrt(2)-1)) 

        fig, ax = plt.subplots(figsize=(20, 20))
        ax.set_aspect('equal')
        ax.set_xlim(-self.const * self.length, self.const * self.length)
        ax.set_ylim(-self.const * self.length, self.const * self.length)

        angle = np.linspace(0, 2 * np.pi, 9)
        x=[]
        y=[]

        for i in range(8):
            num = r_cir * cos(i * np.pi/4)
            x.append(num)

        for i in range(8):
            num = r_cir * sin(i *  np.pi/4)
            y.append(num)

        ax.fill(x, y, label='octagon')

        in_circle = plt.Circle((0, 0), r_in, color='green', fill=False, label="Вписанная окружность" )
        ax.add_patch(in_circle)

        cir_circel = plt.Circle((0, 0), r_cir, color='red', fill=False, label="Описанная окружность" )
        ax.add_patch(cir_circel)

        # Визуализируем график
        plt.legend()
        plt.show()

    # Создали деструктор
    def __del__(self):
        print("del done")

# Создали функцию в main
def main(): 
    
    length = int(input("Введите значение стороны октагона:"))
    octagon = Octagon(length)


    # Вызвали все методы
    octagon.circumscribed()
    octagon.inscribed()
    octagon.octagon()
    octagon.graph()


if __name__ == "__main__":
    main()