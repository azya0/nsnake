from PygameSnakeApp import SnakeGamePlayByUser, SnakeGamePlayByNN


def main() -> None:
    SnakeGamePlayByNN(720, 480, 8, 9, "/home/sokolov-an/code/nsnake/models/result_3000.pt").run()
    # SnakeGamePlayByUser(720, 480, 35, 36).run()


if __name__ == "__main__":
    main()
