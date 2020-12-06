import sys
import pygame
from controller.CarImp.RealCar import RealCar
from controller.ControllerImp.KeyboadController import KeyboardController

class Window:
    def __init__(self, width, height, caption, FPS=200):
        # window
        self.FPS = FPS
        self.width = width
        self.height = height
        self.caption = caption
        self.displaySurface = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.HWSURFACE)
        pygame.display.set_caption(self.caption)

        self.car = RealCar(None)
        self.controller = KeyboardController(self.car)

    def run(self):
        fpsClock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP4:
                        self.controller.onLeftDown()
                    if event.key == pygame.K_KP6:
                        self.controller.onRightDown()

            ms = fpsClock.get_time()
            self.car.update(ms)

            pygame.display.flip()
            fpsClock.tick(self.FPS)

if __name__ == "__main__":
    window = Window(500, 500, "hehe", FPS=60)
    window.run()
