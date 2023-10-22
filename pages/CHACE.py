import streamlit as st
import openai

openai.api_key = "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"

user_input = st.text_input("Ask CHACE: ")
try:
    if user_input:
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=50  # Adjust the maximum response length as needed
        )
        chatgpt_response = response.choices[0].text

    if chatgpt_response:
        st.write("CHACE's Response:")
        st.write(chatgpt_response)
except:
    st.write("Not enough tokens.")