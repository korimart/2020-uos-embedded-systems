import sys
import pygame

class Window:
    def __init__(self, width, height, caption, FPS=200):
        # window
        self.FPS = FPS
        self.width = width
        self.height = height
        self.caption = caption
        self.displaySurface = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.HWSURFACE)
        pygame.display.set_caption(self.caption)

    def run(self, inputManager, sceneManager, renderer):
        fpsClock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    inputManager.register(event.key)

                elif event.type == pygame.KEYUP:
                    inputManager.unregister(event.key)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    inputManager.register(event.button)

                elif event.type == pygame.MOUSEBUTTONUP:
                    inputManager.unregister(event.button)

            ms = fpsClock.get_time()
            pygame.display.flip()
            fpsClock.tick(self.FPS)
