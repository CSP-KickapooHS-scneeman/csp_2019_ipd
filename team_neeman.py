####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'team_neeman'
strategy_name = 'betray the unloyal'
strategy_description = 'look for patterns, betray against the unloyal'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    if len(my_history)==0:
        return 'c'
    
    #if they always betray
    if look_for_always_betray(their_history):
        return 'b'
    
    #if they always collude
    if look_for_always_collude(their_history):
        return 'c'
    
    
    #look for patterns, beat prediction
    for i in range(2,11):
        if look_for_pattern(their_history, i):
            return beat_theirs(their_history, i)
    
    #count how many betrayals
    count = 0
    for item in their_history:
        if item == 'b':
            count = count + 1
    #if they usually betray, betray
    if count > len(their_history)/2:
        return 'b'
    else:
        if their_history[-1]=='b' and my_history[-1]=='c':
            return 'b'
        elif 'b' in their_history:
            return 'b'
        else:
            return 'c'


#counter a previous move
def beat_theirs(their_history, n):
    if their_history[-n] == 'c':
        return 'b'
    else:
        return 'b'

def look_for_always_betray(their_history):
    if  not 'c' in their_history:
        return True
    else:
        return False
        
def look_for_always_collude(their_history):
    if  not 'b' in their_history:
        return True
    else:
        return False

def look_for_pattern(their_history, n):
    if len(their_history)>3*n:
        #good enough, looks for pattern length n
        #just two previous moves repeated twice
        if their_history[-1]==their_history[-2*n] and their_history[-1] == their_history[-3*n]:
            return True
        else:
            return False
    else:
        return False
