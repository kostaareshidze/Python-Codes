import math
import pygame
import random
from pygame import mixer

# [0.5pt] Background - Use image for background
# [0.5pt] Food - Use image for food.
# [0.5pt] Music - Add background music to the game
# [1pt] Score - Add scoring system to the game. Every time snake eats food player earns some points which
# should be displayed at the upper part of the screen.

class App:

    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.score = 0
        self.appleX = random.randint(100, 1184)
        self.appleY = random.randint(50, 684)
        self.snakeX = random.randint(0, 1184)
        self.snakeY = random.randint(0, 684)

        self.body = [(self.snakeX-16, self.snakeY),(self.snakeX-32, self.snakeY),(self.snakeX-48, self.snakeY),(self.snakeX-64, self.snakeY),(self.snakeX-80, self.snakeY)]
        self.snakeX_change = 6
        self.snakeY_change = 0
        pygame.mixer.init()
        mixer.music.load("nokia.wav")
        mixer.music.play(-1)
    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Snake")
        icon = pygame.image.load("snake.png")
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
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if self.snakeX_change != +6:
                        self.snakeX_change = 0
                        self.snakeY_change = 0
                        self.snakeX_change -= 6
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.snakeX_change != -6:
                        self.snakeX_change = 0
                        self.snakeY_change = 0
                        self.snakeX_change += 6
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.snakeY_change != +6:
                        self.snakeX_change = 0
                        self.snakeY_change = 0
                        self.snakeY_change -= 6
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.snakeY_change != -6:
                        self.snakeX_change = 0
                        self.snakeY_change = 0
                        self.snakeY_change += 6

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.image.load("back.png"), (0, 0))
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 32)
        score = font.render("Score : " + str(self.score), True, (255, 255, 255))
        self.body.append((self.snakeX, self.snakeY))

        pygame.draw.rect(self.screen, (255, 255, 255), [self.snakeX, self.snakeY, 16, 16])
        for (x, y) in self.body:
            pygame.draw.rect(self.screen, (255, 255, 255), [x, y, 16, 16])

        self.screen.blit(score, (10, 10))

        self.screen.blit(pygame.image.load("apple.png"), (self.appleX, self.appleY))
        self.snakeX += self.snakeX_change
        self.snakeY += self.snakeY_change
        distance = math.sqrt(pow(self.snakeX - self.appleX, 2) + pow(self.snakeY - self.appleY, 2))
        if self.snakeX >= 1200 or self.snakeX <= 0:
            self.collisionSound()
            self.running = False
        if self.snakeY >= 700 or self.snakeY <= 0:
            self.collisionSound()
            self.running = False
        if distance < 16:
            self.appleX = random.randint(100, 1184)
            self.appleY = random.randint(50, 684)
            self.score += 1
        else:
            self.body.pop(0)

        if (self.snakeX, self.snakeY) in self.body:
            self.collisionSound()
            self.running = False
        pygame.display.flip()
        self.clock.tick()

    def cleanUp(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()
