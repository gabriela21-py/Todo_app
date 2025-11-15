import functions
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo",key="todo")
add_button=sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box,add_button]],
                   font=('Arial',18))
while True:
    event,values=window.read() #display the window
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close() #close the window