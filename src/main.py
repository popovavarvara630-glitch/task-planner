tasks = []

def get_priority(task):
    return task["Приоритет"]

while True:
    title = input('Введите название задачи: ')
    deadline = input('Введите срок задачи: ')
    priority = int(input('Введите приоритет задачи: '))

    task = {"Задача": title, "Срок": deadline, "Приоритет": priority}

    tasks.append(task)

    while True:
        choice = input('Вы хотите ввести еще одну задачу? ').strip().lower()
        if choice in ['да', 'нет']:
            break  

        print('Напиши нормально: да или нет!')

    if choice == 'нет':
        break
tasks.sort(key=get_priority)

print('\nВаш список задач:')
for i, task in enumerate(tasks, 1):
    print(f"{i}. Задача: {task['Задача']} | Срок: {task['Срок']} | Приоритет: {task['Приоритет']}")