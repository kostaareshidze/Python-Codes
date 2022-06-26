import math

import pygame
import random


class App:

    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.posX = 370
        self.posY = 480
        self.posX_change = 0
        self.posEnemyX = random.randint(0, 735)
        self.posEnemyY = random.randint(50, 150)
        self.posEnemyX_change = 1.5
        self.posEnemyY_change = 40
        self.posBulletX = 0
        self.posBulletY = 480
        self.posBulletY_change = 10
        self.bulletState = "ready"
        self.score = 0

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space")
        icon = pygame.image.load("kk.png")

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
                if event.key == pygame.K_LEFT:
                    self.posX_change -= 5
                if event.key == pygame.K_RIGHT:
                    self.posX_change += 5
                if event.key == pygame.K_SPACE:
                    if self.bulletState is "ready":
                        self.posBulletX = self.posX
                        self.bulletState = "fire"
                        self.screen.blit(pygame.image.load("bullet.png"), (self.posBulletX + 16, self.posBulletY + 10))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.posX_change = 0

    def render(self):

        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.image.load("background.png"), (0, 0))
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 32)

        # space ship movement
        self.posX += self.posX_change
        if self.posX <= 0:
            self.posX = 0
        elif self.posX >= 736:
            self.posX = 736

        # enemy movement
        self.posEnemyX += self.posEnemyX_change
        if self.posEnemyX <= 0:
            self.posEnemyX_change = 1.5
            self.posEnemyY += self.posEnemyY_change
        elif self.posEnemyX >= 736:
            self.posEnemyX_change = -1.5
            self.posEnemyY += self.posEnemyY_change
        # bullet fire
        if self.posBulletY <= 0:
            self.posBulletY = 480
            self.bulletState = "ready"
        if self.bulletState is "fire":
            self.screen.blit(pygame.image.load("bullet.png"), (self.posBulletX + 16, self.posBulletY + 10))
            self.posBulletY -= self.posBulletY_change
        score = font.render("Score : " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score, (10, 10))

        distance = math.sqrt(
            math.pow(self.posEnemyX - self.posBulletX, 2) + math.pow(self.posEnemyY - self.posBulletY, 2))
        if distance < 27:
            self.posBulletY = 480
            self.bulletState = 'ready'
            self.posEnemyX = random.randint(0, 735)
            self.posEnemyY = random.randint(50, 150)
            self.score += 1
            print(self.score)

        self.screen.blit(pygame.image.load("spaceship.png"), (self.posX, self.posY))
        self.screen.blit(pygame.image.load("alien.png"), (self.posEnemyX, self.posEnemyY))

        pygame.display.flip()
        self.clock.tick()

    def cleanUp(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()

