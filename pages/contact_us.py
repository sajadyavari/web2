import streamlit as st
from send_email import send_email


st.header("Contact Me!")

with st.form(key="contact-us"):
    email = st.text_input("Enter Your E-Mail Address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: Contact From {email}

From: {email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent Now!")