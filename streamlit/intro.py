import streamlit
streamlit.title("Hello World")
streamlit.header("User Details")
streamlit.subheader(" Ur name")
name = streamlit.text_input("Enter ur name")
print(name)