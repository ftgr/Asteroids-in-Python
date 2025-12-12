import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 #delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x, y)
    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # Must draw before flip()
        for member in drawable:
            member.draw(screen)

        # clock.tick(60)
        dt = clock.tick(60) / 1000
        for member in updatable:
            member.update(dt)

        pygame.display.flip()
        #print(dt)
   # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
   # print(f"Screen width: {SCREEN_WIDTH}")
   # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
