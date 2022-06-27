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

    for event in replay.replay_data:
        # print(event.keys.value)

        # Ignore deadtime (for now?)
        if event.keys.value == 0:
            continue

        # Change variables
        if event.keys.value != current_key:
            last_key = current_key
            current_key = event.keys.value
            print(f"{TAIKO_KEYS.get(last_key)} to {TAIKO_KEYS.get(current_key)}")
        
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

