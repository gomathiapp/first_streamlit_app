import snowflake.connector
import streamlit
import pandas
import requests
from urllib.error import URLError

streamlit.title('My parents new healthy dinner')
streamlit.title('hello world !!')
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

streamlit.header('Fruityvice Fruit Advice!')
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
#streamlit.text(fruityvice_response.json())
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())  # normalize the json data
    return fruityvice_normalized
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error("Please select a fruit to get information")
   else:
       back_from_function=get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)  # display data in table format
       #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
       #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())  # normalize the json data
       #streamlit.dataframe(fruityvice_normalized)  # display data in table format
except URLError as e:
    streamlit.error()

 #streamlit.write('The user entered ', fruit_choice)

streamlit.header("View our Fruit List - Add your Favorites!")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()
# Add button
if streamlit.button('Get fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()   
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('"+new_fruit+"')")
        return "Thanks for adding "+ new_fruit

add_my_fruit=streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function=insert_row_snowflake(add_my_fruit)
   my_cnx.close()
   streamlit.text(back_from_function)

#fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
#streamlit.write('Thanks for adding ', fruit_choice)

streamlit.stop()
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")


fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
