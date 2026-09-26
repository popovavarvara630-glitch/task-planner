tasks = []

title = input('Введите название задачи: ')
deadline = input('Введите срок задачи: ')
priority = int(input('Введите приоритет задачи: '))

task = {"title": title, "deadline": deadline, "priority": priority}

def get_priority(task):
    return task["priority"]

tasks.append(task)
tasks.sort(key=get_priority)

print(tasks)
