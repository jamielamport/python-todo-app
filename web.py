import streamlit as st
from modules import functions
import os

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


FILEPATH = "todos.txt"

if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w") as file:
        pass

st.title("My To-Do App")
st.subheader("This is my todo App")
st.write("This app will increase your productivity")

todos = functions.get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="add todo", label_visibility="hidden", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

