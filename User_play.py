from display import Display
import os
import pygame
from spaceship import Spaceship

pygame.mixer.init() # sound effect library
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('component', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('component', 'Gun+Silencer.mp3'))

WIN = Display(900, 500)
FPS = 60

MaxHealth = 10
player_width, player_height = 55, 40
playerSpeed = 5

MAX_BULLETS = 3
BulletSpeed = 7

Yellow_Hit = pygame.USEREVENT + 1
Red_Hit = pygame.USEREVENT + 2

def handle_bullets(yellow_bullets, red_bullets, YellowPlayer, RedPlayer):
    for bullet in yellow_bullets:
        bullet.x += BulletSpeed
        if RedPlayer.position.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Red_Hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIN.width:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BulletSpeed
        if YellowPlayer.position.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Yellow_Hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def main():
    YellowPlayer = Spaceship(100, 300, 90, os.path.join('component', 'spaceship_yellow.png'),
                             player_width, player_height, playerSpeed, MaxHealth)
    RedPlayer = Spaceship(700, 300, 270, os.path.join('component', 'spaceship_red.png'),
                          player_width, player_height, playerSpeed, MaxHealth)

    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()  # quit the pygame and close the window
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB and len(yellow_bullets) < MAX_BULLETS:
                    YP = YellowPlayer.position
                    bullet = pygame.Rect(YP.x + YP.width, YP.y + YP.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_END and len(red_bullets) < MAX_BULLETS:
                    RP = RedPlayer.position
                    bullet = pygame.Rect(RP.x, RP.y + RP.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == Red_Hit:
                RedPlayer.health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == Yellow_Hit:
                YellowPlayer.health -= 1
                BULLET_HIT_SOUND.play()
        if not run:
            break
        WIN.draw_window()
        WIN.display_spaceship(YellowPlayer, RedPlayer)
        WIN.display_bullet(yellow_bullets, red_bullets)
        handle_bullets(yellow_bullets, red_bullets, YellowPlayer, RedPlayer)
        WIN.draw_winner(YellowPlayer, RedPlayer)
        pygame.display.update()
        if YellowPlayer.health <= 0 or RedPlayer.health <= 0:
            break
    if run:
        main()


if __name__ == "__main__":
    main()