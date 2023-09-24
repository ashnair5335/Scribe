import streamlit as st

def add_video(vid_title, link):
    with st.expander(vid_title):
        st.markdown('<iframe width="670" height="400" src="' + link + '" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.write("")

st.title("Video Resources")
st.write("This page is a collection of video resources to aid writers on their path to success.")
st.write("Please explore these videos to get a general feel and some tips on how to write a winning essay!")

st.subheader("From Students")
add_video("Tips for Common and Supplemental Essays", "https://www.youtube.com/embed/E5SmMV9-UbM?si=t9bg46hnjzgGDgdv")
add_video("How to Write a Common Application Essay", "https://www.youtube.com/embed/B2aMtCm__k4?si=oC01deg_C62kY5is")
add_video("How to Write a Common Application Essay (continued)", "https://www.youtube.com/embed/cu1KJiLBaMM?si=D7Iff5LJZ1Bk6QY9")

st.write("---")

st.subheader("From Counselors")
add_video("7 College Essay Tips", "https://www.youtube.com/embed/nhtfrSO8GWo?si=S9Kcmv9b9m4zLpN-")
add_video("Starting the College Essay", "https://www.youtube.com/embed/8_-C9B4GxR0?si=QlZbMMENbVTOFdsw")
add_video("Brainstorming an Essay Topic", "https://www.youtube.com/embed/Dz9aqJWIlOE?si=KeNzHcUe9_91Xq5U")
add_video("7 Personal Statement Ideas", "https://www.youtube.com/embed/BPnl5AeSw_w?si=htw_qHwL5F-D_9Jl")
add_video("Writing Essays on Common Topics", "https://www.youtube.com/embed/2-Sf20y72P0?si=F9k1aJ817eNGvCJA")
