import streamlit
import pandas
import requests

streamlit.title("My Parents new healthy Diner")
streamlit.header("Breakfast")
streamlit.text(" 🐔 Boiled egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/orange"+ "kiwi")

frutyvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(frutyvice_normalized)
