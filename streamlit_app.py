import streamlit as st
import openai
from langchain_openai import ChatOpenAI

# Set your OpenAI API key here
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Function to convert number to roman numeral equivalent 
def roman_numeral(number):
    llm = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature = 0.5)
    prompt=f"Give the roman numeral of {number}"
    response = llm.stream(prompt)
    return (response)

# Streamlit App
st.title('Roman Numeral')

# User input
# Prompt the user to enter an integer
user_input = st.text_area("Enter an integer for which you need the roman numeral equivalent: ")

#try:
    # Convert the input to an integer
number = int(user_input)
if type(user_input) == int:
    st.write(f"You entered the integer: {number}")
#except ValueError:
else:
    st.write("That's not a valid integer. Please try again.")

# Convert text to local slang
if st.button('Roman Numeral'):
    roman = roman_numeral(number)
    st.write('Roman Numeral Equivalent:', roman)
else:
    st.write('Please Press the button.')
