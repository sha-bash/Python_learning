HELP = """
help - Напечатать справку по программе
add - Добавить задачу
show - Показать все запланированные задачи
exit - Завершение работы.
"""

tasks = []
today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Введите название задачи: ")
        tasks.append(task)
        date = input("Введите дату выполнения задачи: ")
        if date.lower() == "сегодня":
            today.append(task)
        elif date.lower() == "завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print("Задача добавлена")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        run = False
    else:
        print("Неизвестная команда")

