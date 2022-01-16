class BrakMonetDoWydania(Exception):

    def __init__(self):
        super().__init__("Brak monet do wydania")