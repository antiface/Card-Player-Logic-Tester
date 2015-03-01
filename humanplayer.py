class Player3(object):#BUILD 1 LEGAL GAME
    def __init__(self,ID="ljm7b2"):
        self.ID = ID

    def GetID(self):
        """Returns ID."""
        return self.ID

    def StartGame(self, Pos):
        """accepts string that records where you are at table-> north,south"""
        self.Pos = Pos

    def GetPosition(self):
        """returns position of that was set in StartGame"""
        return self.Pos

    def PlayCard(self, Hand : tuple, ThisTrick :tuple, PastTricks : tuple, PastHands : dict):
        self.Hand = Hand
        self.ThisTrick = ThisTrick
        self.PastTricks = PastTricks
        self.PastHands = PastHands
        print("\nYour Hand: ")
        for card in range(len(self.Hand)):
            print("("+str(card),self.Hand[card],")",end=" ")
        print("\nThe Tricks: ")
        for card in self.ThisTrick:
            print(card,end=" ")

        card_to_play =int(input("\nWhat is the index of the card you would like to play?\n---->"))
        return card_to_play


