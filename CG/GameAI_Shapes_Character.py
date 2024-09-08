from GameAI_Shapes_Interface import DrawShapes
import pygame

class CharacterShapes(DrawShapes):
    def __init__(self, color, name):
        self.color = color
        self.name = name
    
    def draw_shape(self):
        print("draw character")