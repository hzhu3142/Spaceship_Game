import pygame

pygame.font.init()
RGB = {
    'grey':(104, 105, 110),
    'black':(0, 0, 0),
    'red':(255, 0, 0),
    'yellow':(255, 255, 0),
    'white': (255, 255, 255)
}

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Enjoy the Game!")

    def draw_window(self):
        self.window.fill(RGB['grey'])

        # display board
        BOARDER = pygame.Rect(self.width // 2 - 5, 0, 10, self.height)
        pygame.draw.rect(self.window, RGB['black'], BOARDER)

    def display_spaceship(self, leftPlayer, rightPlayer):
        # display spaceships
        self.window.blit(leftPlayer.image, (leftPlayer.position.x, leftPlayer.position.y))
        self.window.blit(rightPlayer.image, (rightPlayer.position.x, rightPlayer.position.y))

        left_area = pygame.Rect(0, 0, self.width//2, self.height)
        leftPlayer.movement(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, left_area)

        right_area = pygame.Rect(self.width//2 + 5, 0, self.width, self.height)
        rightPlayer.movement(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, right_area)

        # display health text
        right_health_text = HEALTH_FONT.render(
            'Health: ' + str(rightPlayer.health), 1, RGB['black'])
        left_health_text = HEALTH_FONT.render(
            'Health: ' + str(leftPlayer.health), 1, RGB['black'])
        self.window.blit(right_health_text, (self.width - right_health_text.get_width() - 10, 10))
        self.window.blit(left_health_text, (10, 10))

    def display_bullet(self, yellow_bullets, red_bullets):
        for bullet in yellow_bullets:
            pygame.draw.rect(self.window, RGB['yellow'], bullet)

        for bullet in red_bullets:
            pygame.draw.rect(self.window, RGB['red'], bullet)

    def draw_winner(self, YellowPlayer, RedPlayer):
        winner_text = ''
        if YellowPlayer.health <= 0:
            winner_text = 'Red wins!'
        if RedPlayer.health <= 0:
            winner_text = 'Yellow wins!'

        if winner_text:
            draw_text = WINNER_FONT.render(winner_text, 1, RGB['white'])
            self.window.blit(draw_text, (self.width // 2 - draw_text.get_width() // 2,
                                 self.height // 2 - draw_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)  # delay 5 seconds

