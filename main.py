from osrparse import Replay

def main() -> None:
    index = 1
    replay = Replay.from_path(f"replays/{index}.osr")

    print(replay)

if __name__ == "__main__":
    main()