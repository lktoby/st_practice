import streamlit as st

st.title("挨拶アプリ")
st.write("名前を入力")
name = st.text_input("")
if st.button("挨拶する"):
    st.write("こんにちは、", name, "！")