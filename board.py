import pygame

class Board:
    def __init__(self):
        self.drawn = False
        
    boardHeight = 0
    boardWidth = 0 
    cellYratio = 7

    WHITE = (250, 250, 250) # White for line colour
    BLACK = (0, 0, 0)       # Black colour to keep on hand


    def drawGrid(self, surface):
        WIDTH = surface.get_width() // 41   # Set the size of the grid block
        HEIGHT = surface.get_height() // self.cellYratio # Set height of grid block

        GOLD = (255, 176, 57) # Orange
        SILVER = (220,220,220) # Grey
        OIL = (255, 217, 158) # Pale orange
        BONDS = (207, 253, 188) # Pale green
        INDUST = (255, 196, 218) # Pale pink
        GRAIN = (253, 233, 146) # Pale yellow
        colours = [self.WHITE, GOLD, SILVER, OIL, BONDS, INDUST, GRAIN, self.WHITE]

        num = 0
        names = ["", "Gold", "Silver", "Oil", "Bonds", "Indust.", "Grain"]

        # I want to rebuild this so we draw the baord with row rects for each colour and then draw lines instead of rects for the grid
        # But that is a later problem
        # We could alos maintain the small black rects and just do coloured rows. Either one.
        for x in range(0, surface.get_width(), WIDTH):
            for y in range(0, surface.get_height(), HEIGHT): # In theory we only need 6
                space = pygame.Rect(x, y, WIDTH, HEIGHT)
                row = pygame.Rect(0, y, surface.get_width(), HEIGHT)
                print(f"For row {y//HEIGHT}, the y is {y}, and the cel height is {HEIGHT}\n")
                if (x == 0):
                    pygame.draw.rect(surface, colours[y//HEIGHT], row, 0) # Draw 
                pygame.draw.rect(surface, self.BLACK, space, 1)
                
                if (y==0 and x>0):
                    pygame.font.init()
                    font = pygame.Font(None, 30)
                    text = font.render((f"{num}"), False, self.BLACK)
                    text = pygame.transform.rotate(text, -90)
                    surface.blit(text, space)
                    num += 5
        
                if (x==0 and (y//HEIGHT)<7):
                    font2 = pygame.Font(None, 25)
                    name = font2.render((f"{names[y//HEIGHT]}"), False, self.BLACK)
                    name = pygame.transform.rotate(name, -90)
                    surface.blit(name, space)

        self.drawn = True

    def drawBoard(self, screen):
        self.boardWidth = screen.get_width()
        self.boardHeight = (screen.get_height() // 5)*3  # Make the board take up 3 fifths of the screen
        self.boardHeight -= self.boardHeight % self.cellYratio
        board = pygame.Surface((self.boardWidth, self.boardHeight))
        board = board.convert() #Ensures the same pixel format as the display seurface.
        board.fill(self.BLACK)

        self.drawGrid(board)

        # Display The Background
        screen.blit(board, (0, 0))