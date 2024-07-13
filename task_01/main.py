from pathlib import Path

path = Path(__file__).parent.joinpath('salary_file.txt')

def total_salary(path):
    total = 0
    average = 0

    if not path.exists():
        print(f"Файл {path} не знайдено")
        return total, average   
    
    with open(path, 'r', encoding='utf-8') as salary_file:
        lines = salary_file.readlines()
    
        for line in lines:
            if line.strip():
                parts_line = line.strip().split(',')
                if len(parts_line) != 2 or not parts_line[1].isdigit():
                    print(f"Некоректний формат рядка: {parts_line}: повині бути два значення через кому, а саме ПІБ та заробітна плата")
                else:
                    total += int(parts_line[1])
        
    average = int(total / len(lines))
    return total, average

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")