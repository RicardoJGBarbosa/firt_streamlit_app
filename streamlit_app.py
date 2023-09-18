import streamlit
import pandas

streamlit.title("My Parents new healthy dinner")
streamlit.header("Breakfast")
streamlit.text(" 🐔 Boiled egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.dataframe("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

