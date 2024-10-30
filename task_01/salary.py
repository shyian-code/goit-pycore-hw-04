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
            average = salary_total / count_developers if count_developers else 0
            return salary_total, average

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0

# Використання функції
salary_total, average = total_salary("task_01/salary_file.txt")
print(f"Загальна сума заробітної плати: {salary_total}, Середня заробітна плата: {average}")
