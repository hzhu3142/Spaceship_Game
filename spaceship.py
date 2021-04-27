import pygame

class Spaceship:
    def __init__(self, x, y, rotate, image, WIDTH, HIGHT, SPEED, health):
        im = pygame.transform.scale(pygame.image.load(image), (WIDTH, HIGHT))
        self.image = pygame.transform.rotate(im, rotate)
        self.position = pygame.Rect(x, y, WIDTH, HIGHT)
        self.SPEED = SPEED
        self.health = health

    def movement(self, left, right, up, down, area):
        SPEED = self.SPEED
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[left] and self.position.x - SPEED > area.x:  # LEFT
            self.position.x -= SPEED
        if keys_pressed[right] and self.position.x + self.position.width < area.width:  # RIGHT
            self.position.x += SPEED
        if keys_pressed[up] and self.position.y - SPEED > 0:  # up
            self.position.y -= SPEED
        if keys_pressed[down] and self.position.y + self.position.height < area.height - 15:  # DOWN
            self.position.y += SPEED






