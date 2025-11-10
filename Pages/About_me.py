import streamlit as st
from PIL import Image

def render_about_me():
    st.title("About Me")

    # Create two columns for layout: one for the image, one for the text
    # The ratio [1, 2] means the image column will be 1/3 of the width, and text column 2/3.
    col_img, col_text = st.columns([1, 2])

    with col_img:
        # Define the path to your image file within the 'assets' folder.
        image_path = "assets/cubes-3d-abstract-5k-wu.jpg"
        
        try:
            # Open the image using Pillow (PIL)
            image = Image.open(image_path)
            
            # Display the image using st.markdown with custom HTML and CSS class.
            # This method is used to apply the custom CSS for circular shape and fading edge.
            # It converts the image to base64 to embed it directly into the HTML.
            st.markdown(
                f"""
                <div class="profile-picture-container">
                    <img src="data:image/jpeg;base64,{st.image(image, use_column_width=True)._repr_html_().split(',')[1].split('"')[0]}" class="profile-picture">
                </div>
                """,
                unsafe_allow_html=True
            )

        except FileNotFoundError:
            st.error(f"Error: Image not found at {image_path}. Please ensure the file exists.")
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