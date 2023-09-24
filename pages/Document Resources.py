import streamlit as st
from pdf2image import convert_from_path

st.title("Document Resources")
st.write("This page contains some links to guides for essay writing, as well as some excellent \
         essay examples that were accepted into the Ivy League. Enjoy!")

st.subheader("Tutorials")
st.markdown("[Writing a Good College Essay](https://www.mtsac.edu/eops/tutoring/Writing_A_Good_College_Application_Essay.pdf) - Sara Harberson")

st.subheader("Example Essays")
st.markdown("[27 Amazing College Essays](https://www.collegeessayguy.com/blog/college-essay-examples) - Ethan Sawyer AKA College Essay Guy")
