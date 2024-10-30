def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            salary_total = 0
            count_developers = 0

            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salary_total += float(salary)
                    count_developers += 1
                except ValueError:
                    print(f"Неправильний формат даних у рядку: {line.strip()}")
            average = total / count_developers if count_developers else 0
            return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0

# Використання функції
path_to_file = "path/to/salary_file.txt"
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
