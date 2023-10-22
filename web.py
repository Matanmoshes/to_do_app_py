import streamlit as st                # Importing the streamlit library, essential for the web app interface.
import functions                      # Importing functions from the local functions script.

todos = functions.get_todos()         # Fetching the current list of todos from the file.

def add_todo():                       # Function to handle the addition of a new todo item.
    todo = st.session_state["new_todo"] + "\n"  # Retrieving the new todo item from the session state.
    todos.append(todo)                # Adding the new todo item to the list of todos.
    functions.write_todos(todos)      # Writing the updated list of todos back to the file.

st.title("My Todo App")               # Setting the title of the web page.
st.subheader("This is my todo app.")  # Adding a subheader to the web page.
st.write("Thus app is to increase your productivity.")  # Providing a description or additional information.

for index, todo in enumerate(todos):  # Looping through each todo item in the list.
    checkbox = st.checkbox(todo, key=f"todo {index}")  # Creating a checkbox for each todo item.
    if checkbox:                      # Checking if the checkbox is selected/checked.
        todos.pop(index)              # If checked, the todo item is removed from the list.
        functions.write_todos(todos)  # The updated list, sans the completed todo, is written back to the file.
        #del st.session_state[todo]
        st.experimental_rerun()       # Rerunning the app to reflect the changes immediately.

st.text_input(label="", placeholder="Add new todo...",  # Creating a text input field for adding new todos.
              on_change=add_todo, key='new_todo')       # Specifying the function to call and the session state key.

