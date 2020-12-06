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

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.key)

                elif event.type == pygame.MOUSEBUTTONUP:
                    print(event.key)

            ms = fpsClock.get_time()
            pygame.display.flip()
            fpsClock.tick(self.FPS)

if __name__ == "__main__":
    window = Window(500, 500, "hehe", FPS=60)
    window.run()
