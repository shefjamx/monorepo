import pygame
from scenes.generic_scene import GenericScene
from scenes.play import PlayScene

class ConnectScene(GenericScene):
    def __init__(self, screen, main_loop) -> None:
        super().__init__(screen, main_loop)
        self.background_image = pygame.image.load("assets/images/home_background.png")
        self.main_loop.change_scene(PlayScene, "anybody-can-find-love")

    def tick(self):
        # Background
        rect = self.background_image.get_rect()
        self.display.blit(self.background_image, rect)

        return super().tick()