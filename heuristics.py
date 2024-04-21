
def base_heuristic(curr_state):
    currPlayer = curr_state.get_curr_player()
    otherPlayer = (curr_state.get_curr_player() % 2) + 1
    if currPlayer == 1:
        p1_moves = len(curr_state.potential_moves())
        curr_state.set_curr_player(otherPlayer)
        p2_moves = len(curr_state.potential_moves())
    else:
        p2_moves = len(curr_state.potential_moves())
        curr_state.set_curr_player(otherPlayer)
        p1_moves = len(curr_state.potential_moves())
    curr_state.set_curr_player(currPlayer)
    return p1_moves - p2_moves

def advanced_heuristic(curr_state):
    return 0
