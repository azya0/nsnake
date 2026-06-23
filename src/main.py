from PygameSnakeApp import SnakeGamePlayByNN


def main() -> None:
    SnakeGamePlayByNN(720, 480, 35, 36, "/home/sokolov-an/code/nsnake/models/result_1000.pt").run()


if __name__ == "__main__":
    main()
