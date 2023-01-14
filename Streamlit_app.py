import streamlit

streamlit.title(':yum: my parents new healthy dinner')
streamlit.header('breakfast menu')
streamlit.text('omega 3 & blueberry oatmeal')
streamlit.text('kale spinach and rocket smoothie')
streamlit.text('hard-boiled free-range egg')
streamlit.header('build your own fruit smoothie')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruit_to_show)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("SELECT * from fruit_load_list")

my_data_row = my_cur.fetchall()

streamlit.header("the fruit load list contains:")

streamlit.dataframe(my_data_row)
