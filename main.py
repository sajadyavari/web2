import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1,empty_1, col2 = st.columns([1,0.5,1.5])
col3,empty_2, col4 = st.columns([1,0.5,1.5])

with col1:
    st.image("image/photo.png")
    content2 = """"
    اله اینه که وقتی خدایگان یونیکس تصمیم گرفتن روشی برای زمان‌سنجی اختراع کنن، ")
    """
    st.write(content2)

with col2:
    st.title("About title")
    content = """
    
مساله اینه که وقتی خدایگان یونیکس تصمیم گرفتن روشی برای زمان‌سنجی اختراع کنن، 
با خودشون گفتن «ما تعداد ثانیه‌های گذشته از ۱ ژانویه ۱۹۷۰ رو می‌شمریم» 
و برای اینکار از یه عدد ۳۲ بیتی علامت‌دار استفاده کردن و این متغیر در ۲۰۳۸ پر خواهد شد و زمان ریست می‌شه (: 
راه حل احتمالی؟ مهاجرت همه لینوکس‌ها، بی اس دی‌ها، یونیکس‌ها،‌ دیتابیس‌ها و همه دوستاشون به زمان سنج‌های ۶۴ بیتی.
    
    """

    st.info(content)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/" + row["image"])
        st.write(f"[source]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/" + row["image"])
        st.write(f"[source]({row['url']})")

