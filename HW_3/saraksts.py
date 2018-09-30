import os


def print_menu():
    print("\n\n")
    print("Welcome to the TODO task management program.")
    print('[1] - List current tasks')
    print('[2] - Add a new task')
    print('[3] - Delete all tasks')
    print('[4] - Quit (and write to file)')
    print('[5] - Delete a single task')
    return True


def read_from_file(filename):
    try:
        tasks = []
        file_handle = open(filename, "r", encoding="utf-8")
        lines = file_handle.read().splitlines()
        for line in lines:
            task_data = line.split(";;")
            task = {}
            task['title'] = task_data[0]
            task['status'] = (task_data[1] == "True")
            tasks.append(task)
        file_handle.close()
        return tasks
    except IOError:
        return []


def write_to_file(filename, tasks):
    if len(tasks) > 0:
        file_handle = open(filename, "w+", encoding="utf-8")
        for task in tasks:
            task_line = "%s;;%s\n" % (task['title'], task['status'])
            file_handle.write(task_line)
        file_handle.close()
    return True


def add_new_task(tasks, task_title, task_status):
    task = {}
    task['title'] = task_title
    task['status'] = (task_status == 'd')
    tasks.append(task)


def list_all_tasks(tasks, numbered = False):
    for i, task in enumerate(tasks):
        if numbered:
            print('\nTASK: %s' % (i+1))
        else:
            print('\nTASK')
        print('Title: %s ' % task['title'])
        print('Status: %s ' % task['status'])
    return True


def remove_all_tasks(filename):
    os.remove(filename)
    return []

def delete_task(task_number):
    del(tasks[task_number-1])
    return True

FILE_NAME = 'todo.txt'
tasks = read_from_file(FILE_NAME)

while True:
    print_menu()
    action = input('Pick an action ^')
    if action == '4':
        write_to_file(FILE_NAME, tasks)
        break
    if action == '1':
        list_all_tasks(tasks)
    if action == '2':
        task_title = input('Enter task name: ')
        task_status = input('Enter [d], if done: ')
        add_new_task(tasks, task_title, task_status.lower())
    if action == '3':
        tasks = remove_all_tasks(FILE_NAME)
    if action == '5':
        list_all_tasks(tasks, numbered=True)
        task_to_delete = input('Please enter task number: ')
        task_to_delete = int(task_to_delete) # parversam uz INT
        delete_task(task_to_delete)

print('\nSee you later!')
