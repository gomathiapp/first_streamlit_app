
import streamlit
import pandas
streamlit.title('My parents new healthy dinner')
streamlit.title('hello world')
streamlit.header('first header for menu details')
streamlit.text(' 🥣 Omega 3 Bluberry oatmeal')
streamlit.text(' 🥗 strawberry smoothy ')
streamlit.text(' 🐔 boiled egg ')
streamlit.text(' 🥑avacodo toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
