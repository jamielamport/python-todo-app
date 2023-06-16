import streamlit as st
from modules import functions
import os

FILEPATH = "todos.txt"

if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w") as file:
        pass

st.title("My To-Do App")
st.subheader("This is my todo App")
st.write("This app will increase your productivity")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder="Add new todo...")



