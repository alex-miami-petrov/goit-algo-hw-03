import argparse
import os
import shutil
from pathlib import Path

def rec_copy_and_sort(s_path: Path, d_path: Path):
    try:
        if not s_path.exists():
            print(f"Шляху не існує: {s_path}")
        
        if s_path.is_dir():
            print(f"Обробка директорії: '{s_path}'")
            for i in s_path.iterdir():
                rec_copy_and_sort(i, d_path)
        
        elif s_path.is_file():
            print(f"  Знайдено файл: '{s_path.name}'")
            file_ext = s_path.suffix.lstrip(".")

            if not file_ext:
                file_ext = "no_ext"

            target_dir = d_path / file_ext

            try:
                target_dir.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                print(f"  Помилка: Не вдалося створити директорію '{target_dir}': {e}")
                return
            
            try:
                shutil.copy2(s_path, target_dir / s_path.name)
                print(f"  Скопійовано '{s_path.name}' до '{target_dir}'")
            except shutil.Error as e:
                print(f"  Помилка копіювання файлу '{s_path.name}': {e}")
            except OSError as e:
                print(f"  Системна помилка під час копіювання '{s_path.name}': {e}")
        else:
            print(f"  Пропущено невідомий тип об'єкта: '{s_path}'")

    except PermissionError as e:
        print(f"Помилка доступу:  '{s_path}'")
    except Exception as e:
        print(f"Неочікувана помилка при обробці '{s_path}': {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=str, help="Шлях до вихідної директорії (джерела файлів).")
    parser.add_argument("-d", type=str, default="dist", help="Шлях до директорії призначення. Якщо не вказано, використовується 'dist'.")

    args = parser.parse_args()

    s_path = Path(args.source_dir)
    d_path = Path(args.d)

    if not s_path.is_dir():
        print(f"Помилка: Вихідна директорія '{s_path}' не існує або не є директорією.")
        return
    
    try:
        d_path.mkdir(parents=True, exist_ok=True)
        print(f"Директорія призначення: '{d_path}'")
    except OSError as e:
        print(f"Помилка: Не вдалося створити директорію призначення '{d_path}': {e}")
        return


    print(f"\nПочинаємо копіювання та сортування з '{s_path}' до '{d_path}'...")
    rec_copy_and_sort(s_path, d_path)


if __name__=="__main__":
    main()
