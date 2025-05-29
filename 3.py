def solve_hanoi(n_disks: int, source_rod: str, destination_rod: str, auxiliary_rod: str, rods_state: dict):

    if n_disks == 1:
        disk = rods_state[source_rod].pop()
        rods_state[destination_rod].append(disk)
        print(f"Перемістити диск з {source_rod} на {destination_rod}: {disk}")
        print(f"Проміжний стан: {rods_state}")
        return

   
    solve_hanoi(n_disks - 1, source_rod, auxiliary_rod, destination_rod, rods_state)

    
    disk = rods_state[source_rod].pop()
    rods_state[destination_rod].append(disk)
    print(f"Перемістити диск з {source_rod} на {destination_rod}: {disk}")
    print(f"Проміжний стан: {rods_state}")


    solve_hanoi(n_disks - 1, auxiliary_rod, destination_rod, source_rod, rods_state)


def main():
    try:
        n = int(input("Введіть кількість дисків (n): "))
        if n < 1:
            print("Кількість дисків повинна бути натуральним числом (більше 0).")
            return
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    
    rods = {
        'A': list(range(n, 0, -1)), 
        'B': [],
        'C': []
    }

    print(f"Початковий стан: {rods}")

    solve_hanoi(n, 'A', 'C', 'B', rods)

    print(f"Кінцевий стан: {rods}")

if __name__ == "__main__":
    main()