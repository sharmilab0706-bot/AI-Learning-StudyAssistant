import streamlit as st

st.title("🤖 AI Learning & Study Assistant")

st.write("Welcome! Your personal AI learning assistant.")

question = st.text_input("Ask your study question:")

if question:
    st.subheader("📚 Answer")
    st.write(
        "This is a demo response. The AI assistant will provide "
        "a simple explanation for your question."
    )

st.subheader("🎯 Study Tools")

if st.button("Create Study Plan"):
    st.write("Your personalized study plan will be generated here.")

if st.button("Generate Quiz"):
    st.write("Your practice quiz will be generated here.")
