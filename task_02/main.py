from pathlib import Path

def get_cats_info(path):
    cats_info = []

    if not path.exists():
        print(f"Файл {path} не знайдено")
        return cats_info

    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                parts = line.strip().split(',')
                
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_info)
                else:
                    print(f"Некоректний формат рядка: {line.strip()}")

    return cats_info

path = Path(__file__).parent.joinpath('cats.txt')
cats_info = get_cats_info(path)
print(cats_info)