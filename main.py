todos=[]

while True:
    user_action = input("Type add, show, edit,complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo=input("Type a todo: ")
            todos.append(todo)
        case "show":
            for index,item in enumerate(todos):
                print(f"{index+1}.{item}")
        case "exit":
            break
        case "edit" :
            number=int(input("Enter the number of the todo to edit: "))
            number=number-1
            new_todo=input("Enter thr new todo: ")
            todos[number]=new_todo
        case 'complete':
            number = int(input("Enter the number of the todo to complete: "))
            number = number - 1
            todos.pop(number)
        case _:
            print("You enter an unknown command")

print("Bye!")
