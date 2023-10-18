import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)

with col2:
    st.title("Km Shiwangi")
    content = """
    I'm a passionate software engineer with a strong love for coding and problem-solving.
With a background in computer science, I thrive on writing clean, efficient, and scalable code to create innovative software solutions. My goal is to make a positive impact through technology and to continuously improve my skills in pursuit of excellence in software engineering.
 """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in python and they are amazing
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():   #first 10 rows
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():   #last 10 rows
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code]({row['url']})")

