#this is my file

team_name = 'team_joshua'
strategy_name = 'Tri-n-Err'
strategy_description = ''

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    elif their_history[-1]=='c' and my_history[-1]=='b':
        return 'b'
    elif  their_history[-1]=='b' and my_history[-1]=='b':
        return 'b'
    elif  their_history[-1]=='b' and my_history[-1]=='c':
        return 'b'
    elif  their_history[-1]=='c' and my_history[-1]=='c':
        return 'c'
    