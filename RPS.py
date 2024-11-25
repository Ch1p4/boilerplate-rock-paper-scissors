from typing import Dict, List, Optional


def player(
    opponent_prev_play: str,
    opponent_play_hist: List[str] = [],
    opponent_play_hist_combos: Dict[str, int] = {},
    combo_length: int = 5,
) -> str:
    """
    Using Markov strategy based on Abbey's,
    with several improvents, mainly the combo lenght.
    It predicts the opponent's next move and plays the ideal counter move.
    """
    
    opponent_play_hist.append(opponent_prev_play)
       
    if len(opponent_play_hist) >= combo_length:
        # Update play history combos frequencies for the last x moves
        last_x_moves = "".join(opponent_play_hist[-combo_length:])
        opponent_play_hist_combos[last_x_moves] = (
            opponent_play_hist_combos.get(last_x_moves, 0) + 1
        )
        
        predicted_play = get_next_play_prediction(
            last_x_moves, opponent_play_hist_combos
        )
    else:
        predicted_play = "R" # Default best

    # Clear lists after each opponent
    if len(opponent_play_hist) == 1000:
        opponent_play_hist.clear()
        opponent_play_hist_combos.clear()

    return get_counter_move(predicted_play)
    

def get_next_play_prediction(
    last_x_moves: str,
    opponent_play_hist_combos: Dict[str, int] = {},
) -> str:
    potential_plays = [last_x_moves[1:] + move for move in "RPS"]
    potential_play_counts = {
        key: opponent_play_hist_combos.get(key, 0) for key in potential_plays
    }
    return max(potential_play_counts, key=potential_play_counts.get)[-1]


def get_counter_move(predicted_play: str) -> str:    
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_play]