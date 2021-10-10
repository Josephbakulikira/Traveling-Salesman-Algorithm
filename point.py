import pygame

pygame.font.init()
textColor   = (0, 0, 0)
# textFont    = pg.font.Font("freesansbold.ttf", size)
textFont    = pygame.font.SysFont("Arial", 20)

class Point:
    def __init__(self, x, y):
        self.x      = x
        self.y      = y
        self.radius = 1
        self.alpha  = 150

    def Draw(self, manager, showIndex=False, highlight=False, point_index=0):
        surface = pygame.Surface((self.radius *2, self.radius*2), pygame.SRCALPHA, 32)

        if highlight:
            r, g, b = manager.White
            pygame.draw.circle(surface, (r, g, b, 255), (self.radius, self.radius), self.radius)
            pygame.draw.circle(surface, (r, g, b, 255), (self.radius, self.radius), self.radius, 1)


        manager.screen.blit(surface, (int(self.x-self.radius), int(self.y-self.radius)))

        if showIndex:
            textSurface = textFont.render(str(point_index), True, textColor)
            textRectangle = textSurface.get_rect(center=(self.x, self.y))
            manager.screen.blit(textSurface, textRectangle)

    def GetTuple(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"
