from osrparse import Replay

from algorithm import analyze


def main() -> None:
    index = 5
    replay = Replay.from_path(f"replays/{index}.osr")

    analyze.analyze_for_alternate(replay)
    # print(replay)


if __name__ == "__main__":
    main()
