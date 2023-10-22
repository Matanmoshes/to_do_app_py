import functions  # Importing the custom 'functions' module which likely contains todo-related functions.
import PySimpleGUI as sg  # Importing the PySimpleGUI library for the graphical user interface.
import time  # Importing the time module to work with time-related functions.
import os  # Importing the os module to interact with the operating system.

# Check if the todos.txt file exists, if not, create an empty file.
if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

# Setting the theme for the GUI window.
sg.theme("Black ")

# GUI Element Definitions:
clock = sg.Text('', key="clock")  # A text element to display the current time.
label = sg.Text("Type in a to-do")  # A label for the input box.
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # An input box for the user to enter todos.
add_button = sg.Button("Add")  # A button that triggers the addition of a new todo.
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])  # A listbox to display current todos.
edit_button = sg.Button("Edit")  # A button that allows the user to edit a selected todo.
complete_button = sg.Button("Complete")  # A button that marks a todo as complete.
exit_button = sg.Button("Exit")  # A button to exit the application.

# Window layout definition.
window = sg.Window('My To-Do App',
                    layout=[[clock],
                            [label], 
                            [input_box, add_button], 
                            [list_box, edit_button, complete_button],
                            [exit_button]], 
                    font=('Helvetice', 20))

# Event Loop
while True:
    event, values = window.read(timeout=200)  # Read events and values from the window.
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))  # Update the clock element with the current time.
    match event:  # Using match-case to handle events.
        case "Add":  # When the 'Add' button is clicked.
            todos = functions.get_todos()  # Retrieve current todos.
            new_todo = values['todo'] + '\n'  # Get the new todo from the input box.
            todos.append(new_todo)  # Add the new todo to the list of todos.
            functions.write_todos(todos)  # Save the updated todos list.
            window['todos'].update(values=todos)  # Update the listbox with the new list of todos.
        case "Edit":  # When the 'Edit' button is clicked.
            try:
                todo_to_edit = values['todos'][0]  # Get the selected todo to edit.
                new_todo = values['todo']  # Get the updated todo text from the input box.
                
                todos = functions.get_todos()  # Retrieve current todos.
                index = todos.index(todo_to_edit)  # Find the index of the todo to edit.
                todos[index] = new_todo  # Replace the old todo with the updated text.
                functions.write_todos(todos)  # Save the updated todos list.
                window['todos'].update(values=todos)  # Update the listbox with the new list of todos.
            except IndexError:  # Handle the case where no todo is selected.
                 sg.popup("please select an item first.", font=("Helvetice", 20))  # Show a popup for user notification.
        case "Complete":  # When the 'Complete' button is clicked.
            try:
                todo_to_complete = values['todos'][0]  # Get the selected todo to mark as complete.
                todos = functions.get_todos()  # Retrieve current todos.
                todos.remove(todo_to_complete)  # Remove the completed todo from the list.
                functions.write_todos(todos)  # Save the updated todos list.
                window['todos'].update(values=todos)  # Update the listbox with the new list of todos.
                window['todo'].update(values='')  # Clear the input box.
            except IndexError:  # Handle the case where no todo is selected.
                sg.popup("please select an item first.", font=("Helvetice", 20))  # Show a popup for user notification.
        case "Exit":  # When the 'Exit' button is clicked.
            break  # Exit the event loop.
        case "todos":  # When an item in the listbox is selected.
            window['todo'].update(value=values['todos'][0])  # Update the input box with the text of the selected todo.
        case sg.WIN_CLOSED:  # When the window is closed.
            break  # Exit the event loop.

window.close()  # Close the window after exiting the event loop.
