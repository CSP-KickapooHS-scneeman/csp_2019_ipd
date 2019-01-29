team_name = 'Team_Aiden'
strategy_name = 'Undecided'
strategy_description = '''\
Collude first round. Collude, unless betrayed; then retaliate. Resume collusion.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(their_history) < 5:
        return 'c'
    elif their_history[-1] == their_history[-3] and their_history[-3] == their_history[-5] and their_history[-1] != their_history[-2] and their_history[-2] == their_history[-4]:
            return 'b'
    else:
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'