import streamlit as st
from PIL import Image
import os
import base64 # Ensure base64 is imported

def render_about_me():
    st.title("About Me")

    # Helper function to get image as base64
    def get_image_as_base64(path):
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Construct the reliable path to the image
    base_path = os.path.dirname(__file__)
    project_root = os.path.join(base_path, "..")
    image_path = os.path.join(project_root, "Assets", "cubes-3d-abstract-5k-wu.jpg")

    # Create two columns for the main content
    col_img, col_text = st.columns([1, 2])

    with col_img:
        try:
            # Get the image as a base64 string
            image_base64 = get_image_as_base64(image_path)
            
            # Display the image using st.markdown with custom HTML and CSS class.
            # This embeds the base64 image directly into the HTML <img> tag.
            st.markdown(
                f"""
                <div class="profile-picture-container">
                    <img src="data:image/jpeg;base64,{image_base64}" class="profile-picture">
                </div>
                """,
                unsafe_allow_html=True
            )

        except FileNotFoundError:
            st.error("Error: Profile image not found. Please check the file path.")
        except Exception as e:
            st.error(f"An unexpected error occurred while loading the image: {e}")

    with col_text:
        st.write("## Hello there!")
        st.write(
            """
            I'm a passionate individual with a keen interest in data visualization and software development.
            My journey in computer science has led me to explore various technologies, and I particularly
            enjoy building interactive applications that bring data to life.

            This portfolio is a collection of my work, showcasing projects from my coursework in CS39AE
            Data Visualization. I believe in continuous learning and applying theoretical knowledge to
            practical, real-world problems.

            Feel free to explore the different sections of this portfolio to see my charts, dashboards,
            and future aspirations.
            """
        )
    
    # This section is now outside the columns
    st.write("---")
    st.write("### Skills")
    st.write("- Python (Pandas, NumPy, Streamlit, Plotly)")
    st.write("- Data Analysis & Visualization")
    st.write("- Web Development Basics")
    st.write("- Git & GitHub")