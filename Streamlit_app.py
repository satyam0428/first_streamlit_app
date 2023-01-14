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

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json()) --removing this line as it is required to load text part into json

# write your own comment -what does the next line do?
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
#below code kiwi is default value in case no value is supplied)
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("SELECT * from fruit_load_list")

my_data_row = my_cur.fetchall()

streamlit.header("the fruit load list contains:")

streamlit.dataframe(my_data_row)

add_my_fruit= streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding ', add_my_fruit)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")

