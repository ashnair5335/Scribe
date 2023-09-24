import streamlit as st

def add_video(vid_title, link):
    st.subheader(vid_title)
    st.markdown('<iframe width="700" height="400" src="' + link + '" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

add_video("Tips for Common and Supplemental Essays", "https://www.youtube.com/embed/E5SmMV9-UbM?si=hxPLDLg7melR5Owq")