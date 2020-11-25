import sys
import pygame

class Window:
    def __init__(self, width, height, caption, FPS=200):
        self.FPS = FPS
        self.width = width
        self.height = height
        self.caption = caption
        self.displaySurface = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.HWSURFACE)
        pygame.display.set_caption(self.caption)

    def run(self):
        fpsClock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    print(event.key)

                elif event.type == pygame.KEYUP:
                    print(event.key)

            ms = fpsClock.get_time()
            fpsClock.tick(self.FPS)
            pygame.display.update()

    @staticmethod
    def dispatchArrowKeys(key):
        if key == pygame.K_RIGHT:
            pass

        if key == pygame.K_LEFT:
            pass

        if key == pygame.K_UP:
            pass

        if key == pygame.K_DOWN:
            pass
