"""איקס עיגול — שני שחקנים בטרמינל."""

WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def print_board(board: list[str]) -> None:
    def cell(i: int) -> str:
        return board[i] if board[i] else str(i + 1)

    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)}")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)}")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)}")
    print()


def winner(board: list[str]) -> str | None:
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def board_full(board: list[str]) -> bool:
    return all(board)


def ask_move(board: list[str], mark: str) -> int:
    while True:
        raw = input(f"תור של {mark} — בחר משבצת (1-9): ").strip()
        if not raw.isdigit():
            print("צריך מספר בין 1 ל-9.")
            continue
        pos = int(raw)
        if pos < 1 or pos > 9:
            print("צריך מספר בין 1 ל-9.")
            continue
        index = pos - 1
        if board[index]:
            print("המשבצת תפוסה, בחר אחרת.")
            continue
        return index


def play_once() -> None:
    board: list[str] = [""] * 9
    mark = "X"
    print("איקס עיגול")
    print("שחקן X מתחיל. בחר מספר משבצת לפי הלוח.")

    while True:
        print_board(board)
        index = ask_move(board, mark)
        board[index] = mark

        who = winner(board)
        if who:
            print_board(board)
            print(f"{who} ניצח!")
            return
        if board_full(board):
            print_board(board)
            print("תיקו!")
            return

        mark = "O" if mark == "X" else "X"


def main() -> None:
    while True:
        play_once()
        again = input("עוד משחק? (כ/ל): ").strip()
        if again not in ("כ", "כן", "y", "Y", "yes"):
            print("ביי!")
            break


if __name__ == "__main__":
    main()
