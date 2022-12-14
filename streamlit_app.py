import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError


def get_fruityvice_data(this_fruit_choice):
    fruityvice_response= requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
    
    
streamlit.header('Fruityvice Fruit advice')
try:
    fruit_choice=streamlit.text_input('what fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information. ")
    
    else:
        back_from_function=get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
