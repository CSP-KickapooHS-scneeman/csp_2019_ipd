import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'team_alex'
strategy_name = 'passive'
strategy_description = 'betray if betrayed'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) ==0 or len(my_history) == 1: #first and second round collude
        return 'c'
    elif len(my_history) == 1: #if they betrayed first turn then I will betray from then on out
        their_history[-1] == 'b'
        return 'b'
    elif their_history[-1] == 'c' and their_history[-2]== 'c': #if they collude back to back, then collude too
        return 'c'
    elif 'b' in their_history:
        return 'b'
    elif 'b' not in their_history:
        return 'c'
    return 'b'



