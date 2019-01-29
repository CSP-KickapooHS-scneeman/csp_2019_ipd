#this will be my team file

team_name = 'team_chris'
strategy_name = 'Brutal Betrayal'
strategy_description = 'Betrayal'
    
def move(my_history, their_history, my_score, their_score):
    '''Nothing but bretrayal no matter what.
    '''
    # This player always betrays no matter what..
    if len(my_history) == 0:
        return 'b'
    elif my_history[-1]=='c' and their_history[0]=='b':
        return 'b'
    elif my_history[0]=='b' and their_history[-1]=='c':
        return 'b'
    else:
        return 'b'