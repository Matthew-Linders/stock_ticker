# Example file showing a circle moving on screen
import pygame
import board 

# https://chatgpt.com/share/69fd572c-9f04-83ea-a39d-acd1b886c1db -> Do this next time
# Currently the baord is redrawing every frame. 
# And everything is being drawn on the same surface (screen)
# So if you only draw the board once, then the circle (or eventual pieces) are being drawn permenantly on it each frame.
# And that is really not good.
# So the path is:
#   Make the board drawing part of board's init
#   Put the background and the tokens and the board on different layers/surfaces

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1260, 650))
# SHould be able to use get_desktop_sizes() to make the screen the same size as the user's actual screen
gameBoard = board.Board()
pygame.display.set_caption("Stock Ticker")
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color to wipe away anything from last frame and draw the board
    screen.fill("white")
    gameBoard.drawBoard(screen)

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()