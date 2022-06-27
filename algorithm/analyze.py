from collections import defaultdict
from osrparse import Replay

TAIKO_KEYS = {
    1: "LD",
    2: "LK",
    4: "RD",
    8: "RK"
}


def analyze_for_alternate(replay: Replay) -> None:
    current_key = 0
    last_key = 0

    time_held = defaultdict(int)

    for event in replay.replay_data:
        # print(event.keys.value)

        # Ignore deadtime (for now?)
        if event.keys.value == 0:
            continue

        # Update holdins / check for new input
        if event.keys.value == current_key:
            # Handle multiinputs
            if current_key not in {1, 2, 4, 8}:
                if current_key >= 8:
                    time_held[8] += event.time_delta
                    current_key -= 8
                if current_key >= 4:
                    time_held[4] += event.time_delta
                    current_key -= 4
                if current_key >= 2:
                    time_held[2] += event.time_delta
                    current_key -= 2
                if current_key >= 1:
                    time_held[1] += event.time_delta
                    current_key -= 1
                current_key = event.keys.value
            else: # Single key press
                time_held[current_key] += event.time_delta
        else: # Change variables
            last_key = current_key
            current_key = event.keys.value
            print(f"{TAIKO_KEYS.get(last_key)} to {TAIKO_KEYS.get(current_key)}")

            # Reset time held for released keys
            if last_key not in {1, 2, 4, 8}:
                key_difference = last_key^current_key
                if key_difference >= 8:
                    time_held[8] = 0
                    key_difference -= 8
                if key_difference >= 4:
                    time_held[4] = 0
                    key_difference -= 4
                if key_difference >= 2:
                    time_held[2] = 0
                    key_difference -= 2
                if key_difference >= 1:
                    time_held[1] = 0
                    key_difference -= 1
            else:
                if not (current_key > last_key and current_key not in {1, 2, 4, 8}):
                    time_held[last_key] = 0
        
        # Handle for holdin playstyle (later)

        # Handle with alternate checking for kddk/dkkd
        match current_key:
            case 1: 
                if last_key == 2:
                    print(f"Found misalternate: {TAIKO_KEYS.get(last_key)} to {TAIKO_KEYS.get(current_key)}")
            case 2: 
                if last_key == 1:
                    print(f"Found misalternate: {TAIKO_KEYS.get(last_key)} to {TAIKO_KEYS.get(current_key)}")
            case 4: 
                if last_key == 8:
                    print(f"Found misalternate: {TAIKO_KEYS.get(last_key)} to {TAIKO_KEYS.get(current_key)}")
            case 8: 
                if last_key == 4:
                    print(f"Found misalternate: {TAIKO_KEYS.get(last_key)} to {TAIKO_KEYS.get(current_key)}")
        
        print(time_held)

