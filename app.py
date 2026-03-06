import streamlit as st
from generator import generate_caption

st.set_page_config(page_title="AI Social Media Caption Generator")

st.title("📱 AI Social Media Caption Generator")

topic = st.text_input("Enter Topic / Product")

platform = st.selectbox(
    "Select Platform",
    ["Instagram", "LinkedIn", "Twitter", "Facebook"]
)

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Funny", "Inspirational", "Casual"]
)

if st.button("Generate Post"):

    if topic == "":
        st.warning("Please enter a topic")

    else:
        with st.spinner("Generating AI caption..."):
            result = generate_caption(topic, platform, tone)

        st.subheader("Generated Post")
        st.write(result)
