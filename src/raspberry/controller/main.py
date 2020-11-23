import os
import sys

THISDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(THISDIR))
os.chdir(THISDIR)

import EasyPygame
from EasyPygame.Components import *
from OpenGL.GL import *

class Scene1(Scene):
    def __init__(self):
        super().__init__()
        self.carrot = None

    def onLoad(self):
        self.carrot = GameObject(self, "Carrot")
        self.carrot.renderComp = DefaultRenderComponent()

    def preRender(self, ms):
        if EasyPygame.isDown("LEFT"):
            self.carrot.transform.translate(-0.1, 0, 0)

        if EasyPygame.isDown("RIGHT"):
            self.carrot.transform.translate(0.1, 0, 0)

        if EasyPygame.isDown("UP"):
            self.carrot.transform.translate(0, 0.1, 0)

        if EasyPygame.isDown("DOWN"):
            self.carrot.transform.translate(0, -0.1, 0)

if __name__ == "__main__":
    EasyPygame.initWindow(500, 500, "Sample", 75)
    EasyPygame.loadScene("Scene1")
    EasyPygame.switchScene("Scene1")
    EasyPygame.run()