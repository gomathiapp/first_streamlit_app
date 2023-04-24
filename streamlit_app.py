
import streamlit
import pandas
import snowflake.connector
streamlit.title('My parents new healthy dinner')
streamlit.title('hello world')
streamlit.header('first header for menu details')
streamlit.text(' 🥣 Omega 3 Bluberry oatmeal')
streamlit.text(' 🥗 strawberry smoothy ')
streamlit.text(' 🐔 boiled egg ')
streamlit.text(' 🥑avacodo toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
import requests
streamlit.header('Fruityvice Fruit Advice!')
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
#streamlit.text(fruityvice_response.json())

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

# normalize the json data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display data in table format
streamlit.dataframe(fruityvice_normalized)


