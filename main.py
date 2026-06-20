import streamlit as st
from supabase import client , create_client
import supabase
from dotenv import load_dotenv
import os
load_dotenv()
URL=os.getenv("SUP_URL")
key=os.getenv("SUP_KEY")

supabase: client=create_client(URL,key)

def task_list():
    response=supabase.table('todo').select('*').execute()
    return response.data
def insert_task(itask):
    supabase.table('todo').insert({'task':itask}).execute()

def remove_task(rtask):
    supabase.table('todo').delete().eq('task',rtask).execute()
    
st.header("To Do task app")
itask=st.text_input("Enter the task")
col1,col2=st.columns(2);
with col1:
    add=st.button("add task")
with col2:
    delete=st.button("remove task")
if add:
    insert_task(itask)
if delete:
    remove_task(itask)
st.write('### To Do list')
todos=task_list()
if todos:
    for todo in todos:
        st.write(f"{todo['task']}")
else:
    st.write("No Task to do")
