class Resource:
    def __init__(self, id):
        self.name = self.names[id]
        self.colour = self.colours[self.name]
        self.value = 0
        # maybe the token is a member of the resource class? That would make sense.

    names = {
            0 : "GOLD",
            1 : "SILVER",
            2 : "OIL",
            3 : "BONDS",
            4 : "INDUCT",
            5 : "GRAIN"
    }

    colours = {
        "GOLD"      : (255, 176, 57),   # Orange
        "SILVER"    : (220, 220, 220),  # Grey
        "OIL"       : (255, 217, 158),  # Pale orange
        "BONDS"     : (207, 253, 188),  # Pale green
        "INDUST"    : (255, 196, 218),  # Pale pink
        "GRAIN"     : (253, 233, 146),  # Pale yellow
        "WHITE"     : (250, 250, 250),  # White for line colour
        "BLACK"     : (0, 0, 0)         # Black
    }

'''
    yRow = {
            "GOLD" : ,
            "SILVER",
            "OIL",
            "BONDS",
            "INDUCT",
            "GRAIN"
        }
'''
    


