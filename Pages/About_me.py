import streamlit as st
from PIL import Image
import os

def render_about_me():
    st.title("About Me")

    col_img, col_text = st.columns([1, 2])

    with col_img:
        base_path = os.path.dirname(__file__)
        project_root = os.path.join(base_path, "..")
        image_path = os.path.join(project_root, "Assets", "cubes-3d-abstract-5k-wu.jpg")
        
        # --- Start of new debug code ---
        # Check if the file exists at the given path
        if not os.path.exists(image_path):
            st.error(f"Image not found. I am looking for it at this path: {os.path.abspath(image_path)}")
        else:
            st.success(f"Image found at: {os.path.abspath(image_path)}")
        # --- End of new debug code ---

        try:
            image = Image.open(image_path)
            
            st.markdown(
                f"""
                <div class="profile-picture-container">
                    <img src="data:image/jpeg;base64,{st.image(image, use_column_width=True)._repr_html_().split(',')[1].split('"')[0]}" class="profile-picture">
                </div>
                """,
                unsafe_allow_html=True
            )

        except FileNotFoundError:
            # This part is now somewhat redundant due to the check above, but we'll keep it for safety.
            st.error(f"Error: Image could not be opened. Please ensure the file exists at {image_path}.")
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
        st.write("---")
        st.write("### Skills")
        st.write("- Python (Pandas, NumPy, Streamlit, Plotly)")
        st.write("- Data Analysis & Visualization")
        st.write("- Web Development Basics")
        st.write("- Git & GitHub")