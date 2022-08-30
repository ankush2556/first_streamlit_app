import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError
streamlit.header('Fruityvice Fruit advice')
try:
    fruit_choice=streamlit.text_input('what fruit would you like information about?, 'kiwi')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information, ")
    else
        fruityvice_response= requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
        fruityvice_normalized=pandas.json.normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized
        
except URLError as e;
    streamlit.error()
