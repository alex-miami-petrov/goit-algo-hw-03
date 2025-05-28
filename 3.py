def solve_hanoi(n_disks: int, source_rod: str, destination_rod: str, auxiliary_rod: str, rods_state: dict):
    """
    Рекурсивно вирішує головоломку "Вежі Ханоя" і логує кожен крок.

    Args:
        n_disks (int): Кількість дисків для переміщення.
        source_rod (str): Назва початкового стрижня (наприклад, 'A').
        destination_rod (str): Назва цільового стрижня (наприклад, 'C').
        auxiliary_rod (str): Назва допоміжного стрижня (наприклад, 'B').
        rods_state (dict): Словник, що відображає поточний стан стрижнів.
                           Наприклад: {'A': [3, 2, 1], 'B': [], 'C': []}
    """
    # Базовий випадок: якщо потрібно перемістити лише один диск
    if n_disks == 1:
        # Переміщуємо найменший диск з початкового стрижня на цільовий
        disk = rods_state[source_rod].pop() # Знімаємо диск з верхівки початкового стрижня
        rods_state[destination_rod].append(disk) # Кладемо диск на цільовий стрижень
        
        # Логуємо крок і стан
        print(f"Перемістити диск з {source_rod} на {destination_rod}: {disk}")
        print(f"Проміжний стан: {rods_state}")
        return

    # Рекурсивний крок:

    # 1. Перемістити n-1 дисків з початкового стрижня на допоміжний
    #    (використовуючи цільовий стрижень як тимчасовий допоміжний)
    solve_hanoi(n_disks - 1, source_rod, auxiliary_rod, destination_rod, rods_state)

    # 2. Перемістити n-й (найбільший) диск, що залишився на початковому стрижні, на цільовий
    disk = rods_state[source_rod].pop()
    rods_state[destination_rod].append(disk)
    
    # Логуємо крок і стан
    print(f"Перемістити диск з {source_rod} на {destination_rod}: {disk}")
    print(f"Проміжний стан: {rods_state}")

    # 3. Перемістити n-1 дисків з допоміжного стрижня на цільовий
    #    (використовуючи початковий стрижень як тимчасовий допоміжний)
    solve_hanoi(n_disks - 1, auxiliary_rod, destination_rod, source_rod, rods_state)


def main():
    """
    Основна функція програми для запуску Веж Ханоя.
    Запитує кількість дисків і відображає послідовність кроків.
    """
    try:
        n = int(input("Введіть кількість дисків (n): "))
        if n < 1:
            print("Кількість дисків повинна бути натуральним числом (більше 0).")
            return
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    # Ініціалізуємо стрижні:
    # Диски розміщені у порядку зменшення розміру зверху вниз,
    # тобто list(range(n, 0, -1)) дасть [n, n-1, ..., 1]
    rods = {
        'A': list(range(n, 0, -1)), 
        'B': [],
        'C': []
    }

    print(f"Початковий стан: {rods}")

    # Запускаємо рекурсивне рішення
    solve_hanoi(n, 'A', 'C', 'B', rods)

    print(f"Кінцевий стан: {rods}")

if __name__ == "__main__":
    main()