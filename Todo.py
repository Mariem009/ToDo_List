
MRA
def check_file():
    try:
        with open("todo.txt", "x") as file:
            pass
    except FileExistsError:
        pass


def add_task():
    with open("todo.txt", 'a') as file:
        task = input("Write your new task: ")
        file.write("\n- " + task)
        print("Task added!")


def view_tasks():
    done = 0
    not_done = 0
    with open("todo.txt", 'r') as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            print("Here is your To-Do list:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")

                if "[x]" in task:
                    done += 1
                else:
                    not_done += 1
            print(f"Done: {done} | Not Done: {not_done}")


def mark_task_done():
    with open("todo.txt", 'r') as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            print("Here is your To-Do list:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")

            while True:
                try:
                    number = int(input("Which task number do you want to mark as done? ")) - 1
                    chosen_task = tasks[number].strip()
                    break
                except ValueError:
                    print("It is not a valid number!")
                except IndexError:
                    print("The task you chose is not in the list!")

            if "[x]" in chosen_task:
                print("You already marked this task as done!")
            else:
                tasks[number] = f"- [x] {chosen_task[2:].strip()}\n"
                with open("todo.txt", 'w') as f:
                    for task in tasks:
                        f.write(task)
                print("Task marked as done!")


def delete_task():
    with open("todo.txt", 'r') as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            print("Here is your To-Do list:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")

            while True:
                try:
                    number = int(input("Which task number do you want to delete? ")) - 1
                    chosen_task = tasks[number].strip()
                    break
                except ValueError:
                    print("It is not a valid number")
                except IndexError:
                    print("The task you chose is not in the list!")

            del tasks[number]
            with open("todo.txt", 'w') as f:
                for task in tasks:
                    f.write(task)
            print(f"Task deleted: {chosen_task}")


def main_menu():
    print("""
1. View tasks
2. Add a task
3. Mark task as done
4. Delete task
5. Exit
    """)


def main():
    check_file()
    while True:
        main_menu()
        try:
            choice = int(input("choose between 1 and 5: "))
        except ValueError:
            print("Invalid input")
            continue

        if choice == 1:
            print("You chose to view tasks")
            view_tasks()
        elif choice == 2:
            print("You chose to add a task")
            add_task()
        elif choice == 3:
            print("You chose to mark task as done")
            mark_task_done()
        elif choice == 4:
            print("You chose to delete task")
            delete_task()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("You have to choose a number from 1 to 5")


main()
