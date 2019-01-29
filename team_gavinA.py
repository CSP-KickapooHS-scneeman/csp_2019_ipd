team_name ='GavinA'
strategy = 'collude'
startegy = 'betray if both betray, if my_history b and their history c betray, collide if neither'

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'b'
    elif len(their_history)>8:
        return 'b'
    elif my_history[-1]=='b' and their_history=='c':
        return 'b'
    else:
        return 'c'