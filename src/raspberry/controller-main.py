import EasyPygame

# this is necessary to register the scene to EasyPyGame
import controller.MainScene

if __name__ == "__main__":
    EasyPygame.initWindow(500, 500, "Sample", 75)
    EasyPygame.loadScene("MainScene")
    EasyPygame.switchScene("MainScene")
    EasyPygame.run()