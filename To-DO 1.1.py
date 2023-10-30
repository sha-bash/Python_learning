import random

HELP = """
help - Напечатать справку по программе
add - Добавить задачу
random - Добавить случайную задачу
show - Показать все запланированные задачи
exit - Завершение работы.
"""

tasks = {}
random_tasks = ["написать программу", "перенести программу в бота", "Закончить мини-курс"]
run = True

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]
    print("Задача: ", task, " Добавлена на дату: ", date)
    

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("На данную дату нет задач")
    elif command == "add":
        date = input("Введите дату выполнения задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(random_tasks)
        add_todo("сегодня", tasks)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        run = False
    else:
        print("Неизвестная команда")
        run = False