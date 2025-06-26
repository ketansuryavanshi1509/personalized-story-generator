import streamlit as st # type: ignore
from story_generator import generate_story
from utils import save_as_pdf, save_as_txt

st.title("🧚 Personalized Children's Story Generator")

name = st.text_input("Child's Name")
age = st.slider("Child's Age", 3, 12, 6)
animal = st.text_input("Favorite Animal")
theme = st.selectbox("Select Theme", ["Adventure", "Friendship", "Fantasy", "Mystery", "Science"])
length = st.radio("Story Length", ["short", "medium", "long"])

if st.button("Generate Story"):
    if name and animal:
        story = generate_story(name, age, animal, theme, length)
        st.text_area("Generated Story", story, height=300)

        save_as_pdf(story)
        save_as_txt(story)

        with open("story.pdf", "rb") as pdf:
            st.download_button("Download as PDF", pdf, file_name="story.pdf")

        with open("story.txt", "rb") as txt:
            st.download_button("Download as TXT", txt, file_name="story.txt")
    else:
        st.warning("Please fill in all required fields.")
