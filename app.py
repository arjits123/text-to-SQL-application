from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

# function for to load gemini model and provide response
def get_gemini_response(question, prompt ):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

# funciton to retreive query from SQL database
def get_query_from_db(sql_query, db):
    conn = sqlite3.connect(db)
    cusor = conn.cursor()
    cusor.execute(sql_query)
    rows = cusor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

sample_prompt = """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name students and has the following columns - id,name, age, 
    and grade \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM students ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM students 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """

## Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ",key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question,sample_prompt)
    print(response)

    final_response = get_query_from_db(response,"student.db")

    st.subheader("The Response is")
    
    for row in final_response:
        print(row)
        st.header(row)
