####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random

team_name = 'Conner'
strategy_name = "Hesitant forgiveness"
strategy_description = 'I am hesitant to forgive, but I will, eventually.  I become slightly more aggressive after 100 rounds.'
    
def move(my_history, their_history, my_score, their_score):
    
    '''Make my move based on the history with this player.
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    Returns 'c' or 'b' for collude or betray.'''
    
    if len(my_history) == 0 or len(my_history) == 1: # Collude for first round.
        return 'c'
    elif len(my_history) > 99: # Changes strategies after 100 rounds.
        if their_history[99] == 'b': # If their 100th move was to betray, then betray.
            return 'b'
        elif their_history[-1] == 'b': # If their last move was to betray, then betray.
            return 'b'
        elif their_history[-1] == 'c' and their_history[-2] == 'c': # If their last two moves were to collude, then collude.
            return 'c'
        else:
            return 'b'
    elif their_history[-1] == 'b' or their_history[-2] == 'b': # If one of their last two moves was to betray, then betray.
        return 'b'
    elif their_history[-1] == 'c' and their_history[-2] == 'c': # If their last two moves were to collude, then collude.
        return 'c'
    else: # If any other condition, then betray.
        return 'b'