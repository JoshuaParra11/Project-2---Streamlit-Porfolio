import streamlit as st
from PIL import Image
import os

def render_about_me():
    st.title("About Me")

    # Construct the reliable path to the image
    base_path = os.path.dirname(__file__)
    project_root = os.path.join(base_path, "..")
    image_path = os.path.join(project_root, "Assets", "cubes-3d-abstract-5k-wu.jpg")

    # Create two columns for the main content
    col_img, col_text = st.columns([1, 2])

    with col_img:
        try:
            image = Image.open(image_path)
            # Use st.image directly for now, without custom CSS
            st.image(image, use_column_width=True, caption="Profile Image")
        except FileNotFoundError:
            st.error("Error: Profile image not found. Please check the file path.")
        except Exception as e:
            st.error(f"An error occurred while loading the image: {e}")

    with col_text:
        st.write("## Hello there!")
        st.write(
            """
            I'm a passionate individual with a keen interest in data visualization and software development.
            My journey in computer science has led me to explore various technologies, and I particularly
            enjoy building interactive applications that bring data to life.
            """
        )
    
    # This section is now outside the columns
    st.write("---")
    st.write("### Skills")
    st.write("- Python (Pandas, NumPy, Streamlit, Plotly)")
    st.write("- Data Analysis & Visualization")
    st.write("- Web Development Basics")
    st.write("- Git & GitHub")