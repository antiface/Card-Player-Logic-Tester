from Card import *
#from FinalPlayer import Player1, Player2, Player3
#from ljm7b2 import Player
from BaseClass import Player1, Player2, Player3, Player4
import random
from datetime import datetime

startTime = datetime.now()
print("|-----------------|")


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
        position=["North","West","South","East"]
        return position

    def ChangePlayerPosition(self,who_won_trick=0):
        position=["North","East","South","West"]
        if who_won_trick ==0:
            return position
        if who_won_trick ==1:
            position=["East","South","West","North"]
            return position
        if who_won_trick ==2:
            position=["South","West","North","East"]
            return position
        if who_won_trick == 3:
            position=["West","North","East","South"]
            return position

    def DealAHand(self):
        MyDeck=Deck()
        MyDeck.Shuffle()
        for j in range(len(MyDeck.Cards)):
            MyDeck.Cards[j].TurnFaceUp()                   
        return MyDeck.Cards[0:13], MyDeck.Cards[13:26],MyDeck.Cards[26:39],MyDeck.Cards[39:52]

    def TrickWinner(self,trick,trick_win_index):
        #print(trick_win_index)
        self.trick = trick
        c_suit=self.trick[trick_win_index].GetSuit()
        trick_list_NUM_RANK = []
        for card in self.trick:
            if card.GetSuit() == c_suit:
                trick_list_NUM_RANK.append( card.NumericRank() )
            else:
                trick_list_NUM_RANK.append(0)
        
        winning_player = trick_list_NUM_RANK.index(max(trick_list_NUM_RANK))+1
        
        return winning_player #1,2,3,4 for player accordingly


t=Dealer()
player1 = Player1()
player2=Player2()
player3=Player3()
player4=Player4()####

total_freaking_progress = 0

counter_for_total_games = 0

number_games = 1500

P1,P2,P3,P4 = 0,0,0,0
while counter_for_total_games < number_games:
    counter_for_total_games+=1
    total_freaking_progress +=1
    PrintProgress(total_freaking_progress)
    p1,p2,p3,p4=0,0,0,0
    for Q in range(4): #4 hands in a games
    
        n,s,e,w=t.ChangePlayerPosition(Q)

        player1.StartGame(n)
        player2.StartGame(s)
        player3.StartGame(e)
        player4.StartGame(w)

        PastTricks_list=[]
        PastTricks = tuple()
        previous_trick_winner_player_pos = -7
        if player1.GetPosition() =="North":   #gives correct dealing of cards and start position after each trick
            who_won_trick = 1
            b,c,d,a = t.DealAHand()
            starting_position_index = 0
        if player2.GetPosition() =="North":
            who_won_trick = 2
            c,d,a,b = t.DealAHand()
            starting_position_index = 1
        if player3.GetPosition() =="North":
            who_won_trick = 3
            d,a,b,c = t.DealAHand()
            starting_position_index = 2
        if player4.GetPosition() =="North":
            who_won_trick = 4 
            a,b,c,d = t.DealAHand()
            starting_position_index = 3

           
        for X in range(13): #13 tricks in a hand
            
            number_of_tricks_played = 0
            trick=[]
            for_past_trick = []
            stop_this_trick = 0
            for T in range(4): #four cards in a trick
                
                if who_won_trick == 1 or who_won_trick ==  5:
                    pick=player1.PlayCard(a,trick,PastTricks,{})
                    
                    trick.append(a[pick])
                    for_past_trick.insert(0,a[pick])
                    a.remove(a[pick])
                    #print("\nATRICK\n",a,trick)
                    who_won_trick+=1
                    stop_this_trick+=1
                    if stop_this_trick == 4:
                        break

                if who_won_trick == 2 or who_won_trick ==  6:
                    pick=player2.PlayCard(b,trick,PastTricks,{})
                    trick.append(b[pick])
                    for_past_trick.insert(0,b[pick])
                    b.remove(b[pick])
                    #print("\nBTRICK\n",b,trick)
                    who_won_trick+=1
                    stop_this_trick+=1
                    if stop_this_trick == 4:
                        break


                if who_won_trick == 3 or who_won_trick ==  7:
                    pick=player3.PlayCard(c,trick,PastTricks,{})
                    trick.append(c[pick])
                    for_past_trick.insert(0,c[pick])
                    c.remove(c[pick])
                    #print("\nCTRICK\n",c,trick) 
                    who_won_trick+=1
                    stop_this_trick+=1
                    if stop_this_trick == 4:
                        break

                if who_won_trick == 4 or who_won_trick ==  8:
                    pick=player4.PlayCard(d,trick,PastTricks,{})
                    trick.append(d[pick])
                    for_past_trick.insert(0,d[pick])
                    d.remove(d[pick])
                    #print("\nDTRICK\n",d,trick)
                    who_won_trick+=1
                    stop_this_trick+=1
                    if stop_this_trick == 4:
                        break
            #print(trick)
            
            if who_won_trick > 4:
                who_won_trick -=4
            previous_trick_winner = who_won_trick

            


            if previous_trick_winner_player_pos == -7:
                previous_trick_winner_player_pos =0
                who_won_trick=t.TrickWinner(trick,starting_position_index)
                previous_trick_winner_player_pos = who_won_trick
            else:
                who_won_trick=t.TrickWinner(trick,who_won_trick-1)
                previous_trick_winner_player_pos = who_won_trick







            #print("who won the trick",who_won_trick)
            
            if previous_trick_winner == 1 or previous_trick_winner == 5:
                P_T_W = player1.GetPosition()
            if previous_trick_winner == 2 or previous_trick_winner == 6:
                P_T_W = player2.GetPosition()
            if previous_trick_winner == 3 or previous_trick_winner == 7:
                P_T_W = player3.GetPosition()
            if previous_trick_winner == 4 or previous_trick_winner == 8:
                P_T_W = player4.GetPosition()
            else:
                P_T_W = "FAR SOUTH"

            #print(who_won_trick)
            if who_won_trick == 1:
                for_past_trick = trick
                p1+=1
                PastTricks_list.append((trick[0],trick[1],trick[2],trick[3],P_T_W,n))
            if who_won_trick == 2:
                for_past_trick = trick
                p2+=1
                PastTricks_list.append((trick[0],trick[1],trick[2],trick[3],P_T_W,s))
            if who_won_trick == 3:
                for_past_trick = trick
                p3+=1
                PastTricks_list.append((trick[0],trick[1],trick[2],trick[3],P_T_W,e))
            if who_won_trick == 4:
                for_past_trick = trick
                p4+=1
                PastTricks_list.append((trick[0],trick[1],trick[2],trick[3],P_T_W,w))

            
                
                
            

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
