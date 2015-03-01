from Card import *
import random
from datetime import datetime

#PLAY AGAINST COMPUTER
#from FinalPlayer import Player1, Player2, Player3
#from humanplayer import Player3
#from ljm7b2 import Player



#LEGAL PLAYER FOR DEALER TESTING BASELINE
from BaseClass import Player2, Player3, Player4
from SuitFollower import Player1




startTime = datetime.now()
print("|------------------|")


def PrintProgress(total_freaking_progess):
    
    if total_freaking_progress == (number_games*.10):
        print(" ==",end="")
    if total_freaking_progress == (number_games*.20):
        print("==",end="")
    if total_freaking_progress == (number_games*.30):
        print("==",end="")    
    if total_freaking_progress == (number_games*.40):
        print("==",end="")
    if total_freaking_progress == (number_games*.50):
        print("==",end="")
    if total_freaking_progress == (number_games*.60):
        print("==",end="")
    if total_freaking_progress == number_games*.70:
        print("==",end="")
    if total_freaking_progress == number_games*.80:
        print("==",end="")
    if total_freaking_progress == number_games*.90:
        print("=>",end=" ")


class Dealer(object):
    def _init(self,games=1):
        self.games=games
        self.Hand=[]
        
    def GivePlayerPosition(self):
        position=["North","East","South","West"]
        return position

    def ChangePlayerPosition(self,who_won_trick=0):
        position=["North","East","South","West"]
        if who_won_trick ==0:
            return position

    def DealAHand(self):
        MyDeck=Deck()
        MyDeck.Shuffle()
        for j in range(len(MyDeck.Cards)):
            MyDeck.Cards[j].TurnFaceUp()                   
        return MyDeck.Cards[0:13], MyDeck.Cards[13:26],MyDeck.Cards[26:39],MyDeck.Cards[39:52]

    def TrickWinner(self,trick):
        
        self.trick = trick
        c_suit=self.trick[0][-1].GetSuit()
        #print("\n",c_suit,"This is the suit")
        #print("Trick: ")
        #for i in trick:
            #print(i[-1],end=" ")
        trick_list_NUM_RANK = []
        for card in self.trick:
        
            if card[-1].GetSuit() == c_suit:
                trick_list_NUM_RANK.append( card[-1].NumericRank() )
            else:
                trick_list_NUM_RANK.append(0)
        
        winning_player = self.trick[trick_list_NUM_RANK.index(max(trick_list_NUM_RANK))][0]
        #print("Winner:", winning_player -1)
        return winning_player #1,2,3,4 for player accordingly


t=Dealer()
player1=Player1()
player2=Player2()
player3=Player3()
player4=Player4()####

total_freaking_progress = 0

counter_for_total_games = 0

number_games = 1

P1,P2,P3,P4 = 0,0,0,0

while counter_for_total_games < number_games: #total games

    counter_for_total_games+=1
    total_freaking_progress +=1

    PrintProgress(total_freaking_progress)

    p1,p2,p3,p4=0,0,0,0

    n,s,e,w=t.ChangePlayerPosition(0)
    player1.StartGame(n)
    player2.StartGame(s)
    player3.StartGame(e)
    player4.StartGame(w)

    for Q in range(4): #4 hands in a games
    
##        n,s,e,w=t.ChangePlayerPosition(Q)

##        player1.StartGame(n)
##        player2.StartGame(s)
##        player3.StartGame(e)
##        player4.StartGame(w)

        PastTricks_list=[]
        PastTricks = tuple()
        if Q == 0:
        #if player1.GetPosition() =="North":   #gives correct dealing of cards and start position after each trick            
            b,c,d,a = t.DealAHand()
            starting_position_index = 0
            who_won_trick = 1
            p1p,p2p,p3p,p4p=0,1,2,3
            #print("player1 deals")
        if Q == 1:
        #if player2.GetPosition() =="North":            
            c,d,a,b = t.DealAHand()
            starting_position_index = 1
            who_won_trick = 2
            p1p,p2p,p3p,p4p=0,1,2,3
            #print("player2 deals")
        if Q == 2:
        #if player3.GetPosition() =="North":            
            d,a,b,c = t.DealAHand()
            starting_position_index = 2
            who_won_trick = 3
            p1p,p2p,p3p,p4p=0,1,2,3
            #print("player3 deals")
        if Q == 3:            
        #if player4.GetPosition() =="North":            
            a,b,c,d = t.DealAHand()
            starting_position_index = 3
            who_won_trick = 4
            p1p,p2p,p3p,p4p=0,1,2,3
            #print("player4 deals")
        for X in range(13): #13 tricks in a hand

            number_of_tricks_played = 0
            stop_this_trick = 0
            trick=[]
            for_past_trick = []
            trick_FOR_score = []
            for T in range(4):
                

                if who_won_trick == 1 or who_won_trick ==  5:
                    pick=player1.PlayCard(a,trick,PastTricks,{})                    
                    trick.append(a[pick])
                    trick_FOR_score.append((1,a[pick]))
                    for_past_trick.insert(p1p,a[pick])
                    a.remove(a[pick])            
                    stop_this_trick+=1
                    if len(trick)==1:
                        played_first_in_trick = player1.GetPosition()
                    if stop_this_trick == 4:
                        break
                    who_won_trick+=1
                if who_won_trick == 2 or who_won_trick ==  6:
                    pick=player2.PlayCard(b,trick,PastTricks,{})
                    trick.append(b[pick])
                    trick_FOR_score.append((2,b[pick]))
                    for_past_trick.insert(p2p,b[pick])
                    b.remove(b[pick])                    
                    stop_this_trick+=1
                    if len(trick)==1:
                        played_first_in_trick = player2.GetPosition()                    
                    if stop_this_trick == 4:
                        break
                    who_won_trick+=1
                if who_won_trick == 3 or who_won_trick ==  7:
                    pick=player3.PlayCard(c,trick,PastTricks,{})
                    trick.append(c[pick])
                    trick_FOR_score.append((3,c[pick]))
                    for_past_trick.insert(p3p,c[pick])
                    c.remove(c[pick]) 
                    stop_this_trick+=1
                    if len(trick)==1:
                        played_first_in_trick = player3.GetPosition()
                    if stop_this_trick == 4:
                        break
                    who_won_trick+=1
                if who_won_trick == 4 or who_won_trick == 8:
                    pick=player4.PlayCard(d,trick,PastTricks,{})
                    trick.append(d[pick])
                    trick_FOR_score.append((4,d[pick]))
                    for_past_trick.insert(p4p,d[pick])
                    d.remove(d[pick])                    
                    stop_this_trick+=1
                    if len(trick)==1:
                        played_first_in_trick = player4.GetPosition()
                    if stop_this_trick == 4:
                        break
                    who_won_trick+=1


            if X == 0:                
                Winner_Trick = t.TrickWinner(trick_FOR_score)
                past_trick_winner = Winner_Trick
                who_won_trick = Winner_Trick
            else:
                Winner_Trick = t.TrickWinner(trick_FOR_score)
                past_trick_winner = Winner_Trick
                who_won_trick = Winner_Trick
            #finds which player won the trick
            if Winner_Trick == 1:
                P_T_W = player1.GetPosition()
                trick = for_past_trick
                p1+=1
                PastTricks_list.append((trick[0],trick[1],trick[2],trick[3],played_first_in_trick,P_T_W))                
            if Winner_Trick == 2:
                P_T_W = player2.GetPosition()
                trick = for_past_trick
                p2+=1
                PastTricks_list.append((trick[0],trick[1],trick[2],trick[3],played_first_in_trick,P_T_W))
            if Winner_Trick == 3:
                P_T_W = player3.GetPosition()
                trick = for_past_trick
                p3+=1
                PastTricks_list.append((trick[0],trick[1],trick[2],trick[3],played_first_in_trick,P_T_W))                
            if Winner_Trick == 4:
                P_T_W = player4.GetPosition()
                trick = for_past_trick
                p4+=1
                PastTricks_list.append((trick[0],trick[1],trick[2],trick[3],played_first_in_trick,P_T_W))                
            else:
                P_T_W = "FAR SOUTH" #should never be this

            #print()
            #print("PastTricks entry:")
            #for m66 in PastTricks_list[-1]:
                    #print(m66,end=" ")
            #print()       
            
            len_PastTricks=len(PastTricks_list)
            PastTricks=tuple(PastTricks_list[:len_PastTricks])
    winnings_list=[p1,p2,p3,p4]
    
    if p1 == max(winnings_list):
        P1 +=1
    if p2 == max(winnings_list):
        P2 +=1
    if p3 == max(winnings_list):
        P3 +=1
    if p4 == max(winnings_list):
        P4 +=1
                
print("Complete.\n")
print("Total Time: ",datetime.now()-startTime)
print("Number of Wins:")
print("\nPlayer 1: ",P1,"\nPlayer 2: ",P2,"\nPlayer 3: ",P3,"\nPlayer 4: ",P4)
print("\nTotal Games Played: ",number_games)
