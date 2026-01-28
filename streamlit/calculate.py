import streamlit
#addition
number1 =streamlit.number_input("Enter the first number")
number2 = streamlit.number_input("Enter the secound number")
if streamlit.button("Add numbers"):
    result = number1+number2
    streamlit.info(f"The sum is {result}")
elif streamlit.button("Subtract"):
    result = number1-number2
    streamlit.info(f"The sub is {result}")


