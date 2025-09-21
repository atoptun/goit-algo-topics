

def move_disk(source: str, target: str, towers: dict[str, list[int]]) -> None:
    disk = towers[source].pop()
    towers[target].append(disk)
    print(f"Перемістити диск {disk} з {source} на {target}")
    print(towers)


def hanoi(n: int, source: str, target: str, auxiliary: str, towers: dict[str, list[int]]) -> None:
    if n == 1:
        move_disk(source, target, towers)
        return

    hanoi(n - 1, source, auxiliary, target, towers)
    move_disk(source, target, towers)
    hanoi(n - 1, auxiliary, target, source, towers)


if __name__ == "__main__":
    n = 5
    towers = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": []
    }

    print("Початковий стан:")
    print(towers)
    hanoi(n, "A", "C", "B", towers)
    print("Кінцевий стан:")
    print(towers)
