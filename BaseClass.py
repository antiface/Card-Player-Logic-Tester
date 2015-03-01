class Player1(object):#BUILD 1 LEGAL GAME
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

        if len(self.ThisTrick) == 0:
            return 0
        else:
            Suit=ThisTrick[0].GetSuit()
            x=0
            for card in self.Hand:
                
                if card.GetSuit()==Suit:               
                    return x
                x+=1
            return 0 
class Player2(object):#BUILD 1 LEGAL GAME
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

        if len(self.ThisTrick) == 0:
            return 0
        else:
            Suit=ThisTrick[0].GetSuit()
            x=0
            for card in self.Hand:
                
                if card.GetSuit()==Suit:               
                    return x
                x+=1
            return 0 
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

        if len(self.ThisTrick) == 0:
            return 0
        else:
            Suit=ThisTrick[0].GetSuit()
            x=0
            for card in self.Hand:
                
                if card.GetSuit()==Suit:               
                    return x
                x+=1
            return 0 
class Player4(object):#BUILD 1 LEGAL GAME
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

        if len(self.ThisTrick) == 0:
            return 0
        else:
            Suit=ThisTrick[0].GetSuit()
            x=0
            for card in self.Hand:
                
                if card.GetSuit()==Suit:               
                    return x
                x+=1
            return 0 
