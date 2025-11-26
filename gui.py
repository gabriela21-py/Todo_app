import functions
import FreeSimpleGUI as sg


sg.theme("TanBlue")

HEADER_BG = "#f4d7b5"

header = [
    [sg.Text(
        "📝 My cozy To-Do list",
        font=("Arial", 24, "bold"),
        background_color=HEADER_BG,
        justification="center",
        expand_x=True,
        pad=(0, 10)
    )]
]

label = sg.Text(
    "Type in a to-do:",
    font=("Arial", 14),
    pad=((0, 0), (10, 5))
)

input_box = sg.InputText(
    tooltip="Enter todo",
    key="todo",
    size=(35, 1)
)

add_button = sg.Button(
    "➕ Add",
    key="Add",
    size=(8, 1),
    mouseover_colors=("white", "#c4884b")
)

edit_button = sg.Button(
    "✏️ Edit",
    key="Edit",
    size=(8, 1),
    mouseover_colors=("white", "#c4884b"),
)
complete_button = sg.Button(
    "Complete",
    key="Complete",
    size=(8, 1),
    mouseover_colors=("white", "#c4884b"),
)
clear_button = sg.Button(
    "🗑 Clear all",
    key="Clear",
    size=(10, 1),
    mouseover_colors=("white", "#b34b4b")
)

list_label = sg.Text(
    "Things to do:",
    font=("Arial", 14)
)

list_box = sg.Listbox(
    values=functions.get_todos(),
    key="todos",
    enable_events=True,
    size=(45, 10),
)

helper_text = sg.Text(
    "Tip: select an item from the list to edit it 💡",
    font=("Arial", 10, "italic"),
    text_color="#704214"
)

status_text = sg.Text(
    "",
    key="status",
    font=("Arial", 10),
    text_color="#006400",
)
exit_button = sg.Button(
    "Exit",
    size=(10, 1)
)
layout = [
    [sg.Column(header, background_color=HEADER_BG, expand_x=True)],
    [label, sg.Push()],
    [input_box, add_button, edit_button,complete_button ,clear_button],
    [exit_button],
    [list_label, sg.Push()],
    [list_box, sg.Push()],
    [helper_text, sg.Push()],
    [status_text, sg.Push()]
]

window = sg.Window(
    "My To-Do App",
    layout=layout,
    font=("Arial", 12),
    element_justification="center",
    finalize=True,
)

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)

    match event:
        case "Add":
            if values["todo"].strip():
                todos = functions.get_todos()
                new_todo = values["todo"].strip() + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["status"].update("✅ Good job! Task added.")
            else:
                sg.popup_no_titlebar(
                    "Please type something first 🙂",
                    auto_close=True,
                    auto_close_duration=1.3,
                    keep_on_top=True
                )

        case "Edit":
            if values["todos"]:
                todo_to_edit = values["todos"][0]
                if values["todo"].strip():
                    new_todo = values["todo"].strip() + "\n"

                    todos = functions.get_todos()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todos(todos)
                    window["todos"].update(values=todos)
                    window["status"].update("✏️ Task updated.")
                else:
                    sg.popup_no_titlebar(
                        "Write the new text for the task first 🙂",
                        auto_close=True,
                        auto_close_duration=1.2,
                        keep_on_top=True
                    )
            else:
                sg.popup_no_titlebar(
                    "Select a task from the list to edit it.",
                    auto_close=True,
                    auto_close_duration=1.2,
                    keep_on_top=True
                )
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "Clear":
            todos = functions.get_todos()
            if not todos:
                sg.popup_no_titlebar(
                    "There is nothing to clear 🙂",
                    auto_close=True,
                    auto_close_duration=1.2,
                    keep_on_top=True
                )
            else:
                answer = sg.popup_yes_no(
                    "Are you sure you want to delete ALL tasks?",
                    title="Confirm delete",
                    keep_on_top=True
                )
                if answer == "Yes":
                    functions.write_todos([])
                    window["todos"].update(values=[])
                    window["todo"].update("")
                    window["status"].update("🗑 All tasks cleared.")

        case "todos":
            if values["todos"]:
                window["todo"].update(value=values["todos"][0].strip())

        case sg.WIN_CLOSED:
            break

window.close()
