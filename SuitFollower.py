class Player1(object):   #Plain Jane
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

            ##### BUILDING DATA SETS IN THIS SECTION #####

        #hand data set
        hand_info = [(i.NumericRank(),i.GetSuit(),self.Hand.index(i),i) for i in self.Hand]
        hand_info.sort(reverse=True)


        #trick data set
        trick_info = [(i.NumericRank(), i.GetSuit(), self.ThisTrick.index(i),i) for i in self.ThisTrick]
        trick_info.sort(reverse=True)


        #finds largest suit in hand
        largest_s = [i.GetSuit() for i in self.Hand]
        largest_suit = [(largest_s.count("H"),"H"),(largest_s.count("S"),"S"),\
                        (largest_s.count("D"),"D"),(largest_s.count("C"),"C")]        
        largest_suit.sort(reverse=True)


        #seperate hands based on suit
        Hand_of_H = [(i[0],i[2]) for i in hand_info if i[1] == "H"]
        if len(Hand_of_H)==0:
            Hand_of_H=[(0,0)]
        Hand_of_S = [(i[0],i[2]) for i in hand_info if i[1] == "S"]
        if len(Hand_of_S)==0:
            Hand_of_S=[(0,0)]
        Hand_of_D = [(i[0],i[2]) for i in hand_info if i[1] == "D"]
        if len(Hand_of_D)==0:
            Hand_of_D=[(0,0)]
        Hand_of_C = [(i[0],i[2]) for i in hand_info if i[1] == "C"]
        if len(Hand_of_C) == 0:
            Hand_of_C = [(0,0)]

        Hand_of_H.sort(reverse=True),Hand_of_S.sort(reverse=True)
        Hand_of_D.sort(reverse=True),Hand_of_C.sort(reverse=True)


        #all of past tricks numeric rank
        past_trick_info=[]
        for i in self.PastTricks:
            
            for tup in i:
                
                if type(tup) != str:
                    past_trick_info.append(tup.NumericRank())
        past_trick_info.sort(reverse=True)


        #data of trick leading suit from past tricks
        past_trick_info_suit =[]
        
        if len(self.ThisTrick) != 0 and len(past_trick_info) >0:
            for i in self.PastTricks:
                for tup in i:
                    if type(tup) != str:
                        if tup.GetSuit() == ThisTrick[0].GetSuit():
                            past_trick_info_suit.append(tup.NumericRank())
        past_trick_info_suit.sort(reverse=True)


        #4 hands of highest card from past tricks by suit
        hearts_t,spades_t,diamonds_t,club_t=[],[],[],[]
        if len(past_trick_info)>0 and len(self.ThisTrick) == 0:
            for i in self.PastTricks:
                for tup in i:
                    if type(tup) != str:
                        if tup.GetSuit() == "H" and tup.NumericRank() > Hand_of_H[0][0]:
                            hearts_t.append(tup.NumericRank())
                        if tup.GetSuit() == "S" and tup.NumericRank() > Hand_of_S[0][0]:
                            spades_t.append(tup.NumericRank())
                        if tup.GetSuit() == "D" and tup.NumericRank() > Hand_of_D[0][0]:
                            diamonds_t.append(tup.NumericRank())
                        if tup.GetSuit() == "C" and tup.NumericRank() > Hand_of_C[0][0]:
                            club_t.append(tup.NumericRank())
            hearts_t.sort(reverse=True),spades_t.sort(reverse=True)        
            diamonds_t.sort(reverse=True),club_t.sort(reverse=True)

        #build hands for each player based on what suits they have played
        compass_index = ["North","East","South","West"]
        suit_follow_dict = {}
        
        for PT in self.PastTricks:
            suit_lead_T = PT[4]
            suit_lead_T_Index = compass_index.index(suit_lead_T)
            WIN_SUIT = PT[suit_lead_T_Index].GetSuit()
            for SI in range(4):
                if SI in suit_follow_dict: 
                    if PT[SI].GetSuit() != WIN_SUIT:
                        suit_follow_dict[SI].append(0) ##0 no more of that suit
                    else:
                        suit_follow_dict[SI].append(99) ##99 has more or was last of suit
            
                else:
                    if PT[SI].GetSuit() != WIN_SUIT:
                        suit_follow_dict[SI]=[0] ##0 no more of that suit
                    else:
                        suit_follow_dict[SI]=[99] ##99 has more or was last of suit                    





        print(suit_follow_dict)

        ##GAMPLAY##         ##GAMEPLAY##        ##GAMEPLAY##

        if len(self.ThisTrick)==0 and len(past_trick_info)==0: #if no cards have been played
            if hand_info[0][0] == 14:
                return hand_info[0][2]
            else:
                return hand_info[-1][2]

        if len(self.ThisTrick)==0 and len(past_trick_info) > 0:

            if len(hearts_t) == 14 - Hand_of_H[0][0]: #if my highest card is the highest to be played
                return Hand_of_H[0][-1]

            elif len(spades_t) == 14 - Hand_of_S[0][0]:                
                return Hand_of_S[0][-1]

            elif len(diamonds_t) == 14 - Hand_of_D[0][0]:                                       
                return Hand_of_D[0][-1]

            elif len(club_t) == 14 - Hand_of_C[0][0]:               
                return Hand_of_C[0][-1]
            else:
                hand_info.sort() #return lowest of that suit#####
                for card in hand_info:                    
                    if card[1] == largest_suit[0][-1]:#
                        
                        return card[2]
        else:  #if any card exists in trick
            
            Suit=ThisTrick[0].GetSuit()
            highest_trick=[i[0] for i in trick_info if i[1] == Suit]
            
            for card in hand_info:
                if card[1] == Suit and card[0] > highest_trick[0]:
                    
                    top_tricks = [i for i in past_trick_info_suit if i > card[0]]
                    
                    if len(self.ThisTrick) == 3: 
                        return card[2]
                    if len(top_tricks) == 14 - card[0]:
                        
                        return card[2]


                    else:
                        hand_info.sort()
                        for t in hand_info:
                            if t[1] == Suit:
                                return t[2]
            
                if card[1] == Suit and card[0] < highest_trick[0]: #if my hands highest is lower than trick highest
                    hand_info.sort()
                    for i in hand_info:
                        if i[1] == Suit:
                            return i[2] #return lowest card in suit

            


            return hand_info[-1][2] #return absolute lowest if no suit in hand

