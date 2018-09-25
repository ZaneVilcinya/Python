print("Welcome to the TODO task management program.")

todo_dict = {}

while True:
    task = input("Please enter a TODO task: ")
    status = input("Was the task completed? (yes/no) ")
    print("Your task is: " + task)

    if status == "yes":
        todo_dict[task] = True
    else:
        todo_dict[task] = False

    new = input("Would you like to enter new task? (yes/no) ")

    if new.lower() == "no":
        break

file = open('todo.txt', 'w+')
print("All tasks that have been added: " % todo_dict)

numbering = 1
for task in todo_dict:
    print('{} - {} Done: {}' .format(numbering, task, todo_dict[task]))
    file.write('{} - {} Done: {}\n'.format(numbering, task, todo_dict[task]))
    numbering = numbering + 1
file.close()