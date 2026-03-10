# Example file showing a circle moving on screen
import pygame

def drawBoard():
    board = pygame.Surface((screen.get_width(), (screen.get_height() // 5)*3))
    board = board.convert() #Ensures the same pizel format as the display seurface.
    board.fill((0, 0, 0))

    drawGrid(board)

    # Display The Background
    screen.blit(board, (0, 0))

def drawGrid(surface):
    WHITE = (250, 250, 250) # White for line colour
    BLACK = (0, 0, 0)

    WIDTH = surface.get_width()//41 #Set the size of the grid block
    HEIGHT = surface.get_height()//7

    GOLD = (255, 176, 57) # Orange
    SILVER = (220,220,220) # Grey
    OIL = (255, 217, 158) # Pale orange
    BONDS = (207, 253, 188) # Pale green
    INDUST = (255, 196, 218) # Pale pink
    GRAIN = (253, 233, 146) # Pale yellow
    colours = [WHITE, GOLD, SILVER, OIL, BONDS, INDUST, GRAIN, WHITE]

    num = 0
    names = ["", "Gold", "Silver", "Oil", "Bonds", "Indust.", "Grain"]

    for x in range(0, surface.get_width(), WIDTH):
        for y in range(0, surface.get_height(), HEIGHT): #In theory we only need 6
            rect = pygame.Rect(x, y, WIDTH, HEIGHT)
            pygame.draw.rect(surface, colours[y//HEIGHT], rect, 0)
            pygame.draw.rect(surface, BLACK, rect, 1)

            if (y==0 and x>0):
                pygame.font.init()
                font = pygame.Font(None, 30)
                text = font.render((f"{num}"), False, BLACK)
                text = pygame.transform.rotate(text, -90)
                surface.blit(text, rect)
                num += 5
    
            if (x==0 and (y//HEIGHT)<7):
                font2 = pygame.Font(None, 25)
                name = font2.render((f"{names[y//HEIGHT]}"), False, BLACK)
                name = pygame.transform.rotate(name, -90)
                surface.blit(name, rect)
            

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1250, 650))
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

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    drawBoard()

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