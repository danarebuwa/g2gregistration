import streamlit as st
import datetime 
import pandas as pd
import numpy as np

st.title("g2G")
st.header("Registration Form")

first_name,last_name = st.columns(2)

first_name = first_name.text_input("First Name")
last_name = last_name.text_input("Last Name")

#define d
d = st.columns(1)
#select date of birth
d = st.date_input(
        "Date of Birth",
        datetime.date(2000,7,5))


#input address 1
st.write("Address")
hn,sr,se = st.columns(3)
hn = hn.text_input("House Address")
sr = sr.text_input("City") #add dropdown list
#create a dropdown list for state of all states in nigeria
se = se.selectbox("State",["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"])

#create email and phone number
email,mob = st.columns([3,1])
email = email.text_input("Email ID")
mob = mob.text_input("Phone")


#create user type
#py = 'Player'
#co = 'Coach'
#ag = 'Agent'
#ay = 'Admin'
#st.write("User Type")
#ut = st.radio("User Type",[py,co,ag,ay])
#st.radio('User Type', ['Player','Coach','Agent','Academy'])
ut = st.selectbox("User Type",["Player","Coach","Agent","Academy"])

#create username and password
user,pw,pw2 = st.columns(3)
user = user.text_input("Username")
pw = pw.text_input("Password",type = "password")
pw2 = pw2.text_input("Confirm password",type = "password")

#upload your player headshot
#im = st.columns(1)
#im = st.file_uploader("Upload a Headshot")

#upload image to the same folder as playereg.csv with first name and last name
image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
if image_file is not None:
    file_details = {"FileName":first_name.name}

    st.write(file_details)

#data from form into dataframe
ch,bl,sub = st.columns(3)
ch.checkbox("I Agree")
if sub.button("Submit"):
    to_add = {"First Name":[first_name],"Last Name":[last_name],"Date of Birth":[d],"House Address":[hn],"City":[sr],"State":[se],"Email ID":[email],"Phone":[mob],"User Type":[ut],"Password":[pw],"Confirm Password":[pw2]}
    to_add = pd.DataFrame(to_add)
    to_add.columns = ["First Name","Last Name","Date of Birth","House Address","City","State","Email ID","Phone","User Type","Password","Confirm Password"]
    to_add.to_csv("playereg.csv",mode='a',header = False)

    st.success("Submitted")









    