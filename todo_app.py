import streamlit as st

st.title("todoアプリ")
st.text("タスクを入力")
tasks = []
tasks.append(st.text_input(""))
st.button("追加")
st.title("タスク一覧")
for task in tasks:
    st.checkbox(task)