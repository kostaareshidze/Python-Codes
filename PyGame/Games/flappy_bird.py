import pygame
import random
from pygame import mixer

# [0.5pt] Add background image
# [0.5pt] Add bird image
# [0.5pt] Music - Add background music to the game
# [0.5pt] Mute - Add mute option. You can create a button or just use the M key. This one needs Music or
# Crash sound

class App:

    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.movementY = 300
        self.gravity = 10
        self.movementX = 200
        self.jump = False
        self.rectHeightUp = random.randint(300 ,550)
        self.rectHeightUp2 = random.randint(300, 550)
        self.rectHeightUp3 = random.randint(300, 550)
        self.rectHeightDown = random.randint(200, 500)
        self.rectHeightDown2 = random.randint(200, 500)
        pygame.mixer.init()
        mixer.music.load("sherekilebi.wav")
        mixer.music.play(-1)

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("flappy bird")
        icon = pygame.image.load("angry-birds (1).png")
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.jump == False:
                    self.jump = True
                if event.key == pygame.K_m:
                    pygame.mixer.music.pause()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.jump = True







    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.image.load("mount.png"), (0, 0))
        self.screen.blit(pygame.image.load("angry-birds.png"), (self.movementX, self.movementY))
        first = pygame.draw.rect(self.screen, (255, 255, 255),
                                 pygame.Rect(300, 0, 12, self.rectHeightUp ))
        second = pygame.draw.rect(self.screen, (255, 255, 255),
                                 pygame.Rect(500, self.rectHeightDown, 12, 700 ))

        third = pygame.draw.rect(self.screen, (255, 255, 255),
                                 pygame.Rect(700, 0, 12, self.rectHeightUp2))
        forth = pygame.draw.rect(self.screen, (255, 255, 255),
                                  pygame.Rect(900, self.rectHeightDown2, 12, 700))
        fifth = pygame.draw.rect(self.screen, (255, 255, 255),
                                 pygame.Rect(1100, 0, 12, self.rectHeightUp3))

        self.movementX += 1
        self.movementY += 6
        if self.movementY <= 0 or self.movementY >= 664 or self.movementX >= 1200:
            self.running = False
        if self.jump == True:
            self.movementY -= self.gravity
            self.gravity -= 2
            self.movementY -= 10
            if self.gravity < - 10:
                self.jump = False
                self.gravity = 10

        if self.movementX + 32 == first.x:
            if (self.rectHeightUp) + 15 > self.movementY:
                self.running = False

        if self.movementX + 32 == second.x:
            if self.rectHeightDown  < self.movementY:
                self.running = False
        if self.movementX + 32 == third.x:
            if (self.rectHeightUp2) + 15 > self.movementY:
                self.running = False

        if self.movementX + 32 == forth.x:
            if self.rectHeightDown2 - 15 < self.movementY:
                self.running = False
        if self.movementX + 32 == fifth.x:
            if (self.rectHeightUp3) + 15 > self.movementY:
                self.running = False


        pygame.display.flip()
        self.clock.tick()

    def cleanUp(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()
