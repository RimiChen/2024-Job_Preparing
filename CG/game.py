### import library
import pygame as pg
from OpenGL.GL import *

### Constant
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class App:
    def __init__(self):
        
        ### initialize python
        pg.init()
        # double buffer for rendering, one pass to graphical card, and one display
        pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pg.OPENGL|pg.DOUBLEBUF)
        # clock for control the frame rate
        self.clock = pg.time.Clock()

        ###initialize opengl
        # R, G, B, A
        glClearColor(0.1, 0.2, 0.2, 1)
        self.mainloop()

    ### game loop
    def mainloop(self):
        running = True
        while(running):
            # check events
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    running = False
            

            # refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            #timing, holding the frame rate
            self.clock.tick(60)
        
        self.quit()

    ### quit function
    def quit(self):
        pg.quit()

if __name__ == "__main__":
    
    myApp = App()
