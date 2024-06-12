from PIL import Image
import json
import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title="The Gyatt", page_icon= ":🐺:", layout="wide")
#lottie files
    
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
#Use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True )    
local_css('Website with streamlit\style/style.css') 

        #loading assets

lottie_coding = load_lottiefile("Website with streamlit\lottie files/coding.json")
allah_secend = Image.open("Website with streamlit\imiges/Allah beutifull.jpg")
allah_first = Image.open("Website with streamlit\imiges/Alah beutifull piture.jpg")
red_truck = Image.open('Website with streamlit\imiges/Red truck.jpg')
#Header section
with st.container():
    st.subheader("Hi, I am Forelax :🤩:")
    st.title("This World shall know pain :🥶:")
    st.write("I am trying to get better at coding. I am using online resourses to make learn about python :🫥:")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """ 
            I am a highschool kid whose trying to learn how to program and code!
            - I havent made any projects public.
            - I have been using online resourses to learn.
            - I like the idea of getting rich from programing.
            - I would be happy to learn more and grow.
            - I find programing very fun.

            Go follow my mom on tiktok if your muslim and you love alah :😊:
            """
        )
st.write("[My Moms TikTok](https://www.tiktok.com/@umarhayat3626?lang=en)")
with right_column:
    st_lottie(lottie_coding, height = "300", key = "coding")

#projects
with st.container():
    st.write('---')
    st.header("My work")
    st.write('###')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(allah_first)
    with text_column:
         st.subheader("I dont have many projects under my belt yet but I plan to do alot of stuff with python")
         st.write(
             """
             This website is build in Phython I just figured out what libaries are.
             I want to automate tasks with python and also make cool stuff.
             I like using math and writing my own things its kind of fun.     
                  
             """
            )
st.markdown("[Follow my mom if you love alah](https://www.tiktok.com/@umarhayat3626?lang=en)" )
with st.container():
    st.write('---')
    st.header("I like this")
    st.write('###')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(allah_secend)
    with text_column:
         st.subheader("I Like that we can just copy old code")
         st.write(
             """
             I like alah and if you like allah why dont you visit my moms tiktok.
             I had a lot of freetime during sumer break so why not build a website.
             I do phython as a hoby but I probally will not go very far with phython.
             This website was made using a totorial by the way.
             """
            )
st.markdown("[click it please](https://www.tiktok.com/@umarhayat3626?lang=en)" )
"---"
with st.container():
    st.write('---')
    st.header("Dads Bussness")
    st.write('###')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(red_truck)
    with text_column:
         st.subheader("May as well permote right")
         st.write(
             """
            My dad runs a truck shiping busness right now hes a one man team.
            but if your interested then I would apriciate you contaction him.
            Like maybe you can be the driver and will pay you.
            You can rent the truck but remember this is just me he might say no.
            his email is umarhayat3626@gmail.com and his name is Umar.
             """
            )
#---contacts---
with st.container():
    st.write("---")
    st.header("Get in touch my dad!!")
    st.write("##")
contact_form ="""
<form action="https://formsubmit.co/umarhayat3626@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Youremail" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
                