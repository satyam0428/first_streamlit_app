import streamlit
import requests
import snowflake.connector
import pandas 
from urllib.error import URLError
streamlit.title(':yum: my parents new healthy dinner')
streamlit.header('breakfast menu')
streamlit.text('omega 3 & blueberry oatmeal')
streamlit.text('kale spinach and rocket smoothie')
streamlit.text('hard-boiled free-range egg')
streamlit.header('build your own fruit smoothie')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruit_to_show)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json()) --removing this line as it is required to load text part into json
#fruit_choice=streamlit.text_input('What fruit would you like information about?','kiwi')
#streamlit.write('the user entered:',fruit_choice)
#use of try and cache now

#creating function to use again and again 

def get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
         streamlit.error("please select one fruit")
  #else:
     # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
     # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      #streamlit.dataframe(fruityvice_normalized)
  else:
        back_from_function=get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
      
except URLError as e:
     streamlit.error()
# write your own comment -what does the next line do?
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)
#below code kiwi is default value in case no value is supplied)

#stop is used for troubleshooting purpose only
#streamlit.stop() 


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

#my_cur = my_cnx.cursor()

#my_cur.execute("SELECT * from fruit_load_list")

#my_data_row = my_cur.fetchall()

#streamlit.header("the fruit load list contains:")

#streamlit.dataframe(my_data_row)

#add_my_fruit= streamlit.text_input('What fruit would you like to add?')
#streamlit.write('Thanks for adding ', add_my_fruit)


#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

streamlit.header("View our fruit list - Add your favourites")
def get_fruit_load_list():
       with my_cnx.cursor() as my_cur:
           my_cur.execute("SELECT * from fruit_load_list")
           return my_cur.fetchall()
#adding a button to load the fruit
if streamlit.button('get fruitlist'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_row = get_fruit_load_list()
     my_cnx.close()
     streamlit.dataframe(my_data_row)
add_my_fruit= streamlit.text_input('What fruit would you like to add?')
#def insert_row_snowflake(new_fruit):
        #with my_cnx.cursor() as my_cur:
             #my_cur.execute("insert into fruit_load_list values ('from streamlit')")
             #return "thanks for adding" + new_fruit
#if streamlit.button('add new fruit'):
     #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     #data = insert_row_snowflake(add_my_fruit)
     #streamlit.text(data)
     
     #below passing variable in select statement
def insert_row_snowflake(new_fruit):
        with my_cnx.cursor() as my_cur:
             my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
             return "thanks for adding" + new_fruit
if streamlit.button('add new fruit'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     data = insert_row_snowflake(add_my_fruit)
     streamlit.text(data)
