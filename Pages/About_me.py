import streamlit as st
from PIL import Image
import os
import base64

def render_about_me():
    st.title("About Me")

    # --- Top Section Container ---
    with st.container():
        def get_image_as_base64(path):
            with open(path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()

        base_path = os.path.dirname(__file__)
        project_root = os.path.join(base_path, "..")
        image_path = os.path.join(project_root, "Assets", "cubes-3d-abstract-5k-wu.jpg")

        col_img, col_text = st.columns([1, 2])

        with col_img:
            try:
                image_base64 = get_image_as_base64(image_path)
                
                st.markdown(
                    f"""
                    <div class="profile-picture-container">
                        <img src="data:image/jpeg;base64,{image_base64}" class="profile-picture" alt="Profile picture of the portfolio owner">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.caption("A picture of me, the portfolio owner.")

            except FileNotFoundError:
                st.error("Error: Profile image not found. Please check the file path.")
            except Exception as e:
                st.error(f"An unexpected error occurred while loading the image: {e}")

        with col_text:
            st.write("## Hi, I'm Joshua Parra!")
            st.write(
                """
                I'm a senior at MSU Denver majoring in Computer Science with a minor in Mathematics. I am currently learning
                to use Streamlit to create a portfolio and be able to show current coursework from my CS39AE Data 
                Visualization class. Some hobbies of mine are playing guitar, video games and learning about 3d
                modeling and printing. I'm also focusing on graduating this semester while job hunting and earning
                certification in CS fields like IT, Data Analysis, and Cloud Computing.

                Feel free to explore the different sections of this portfolio to see my charts, dashboards,
                and future aspirations.
                """
            )

    # --- Bottom Section (Skills) Container ---
    with st.container():
        st.write("---") # Separator line
        st.write("### Skills") # Main title for the section

        # Create two columns for "Courses" and "Tools"
        col_courses, col_tools = st.columns(2)

        with col_courses:
            st.write("#### Courses")
            st.markdown("""
            - CS39AE Data Visualization
            - CS4050 Algorithms & Algorithm Analysis
            - CS3600 Operating Systems
            - CS3100 Operating Systems
            - MTH 2410 Calculus 2
            - MTH 3210 Probability & Statistics
            """)

        with col_tools:
            st.write("#### Tools")
            st.markdown("""
            - Python (Pandas, NumPy, Streamlit)
            - mySQL
            - Git & GitHub
            - VS Code
            - MS Azure
            """)

    # --- Visualization Philosophy Statement Container ---
    with st.container():
        st.write("---") # Separator line
        st.write("### Visualization Philosophy Statement")
        st.write(
            """
            In this project, my visualization philosophy is centered on **Clarity, Accessibility, and Ethics**.

            **Clarity:** Every visualization aims to convey information directly and efficiently. Complex
            datasets are broken down into understandable components, using appropriate chart types and minimal
            visual clutter to ensure the message is immediately apparent to the viewer. The goal is to transform
            raw data into actionable insights without ambiguity.

            **Accessibility:** I strive to make all visualizations accessible to a broad audience, regardless of
            their technical background or visual abilities. This includes thoughtful use of color palettes
            (considering color blindness), clear labeling, and providing context where necessary. The design
            prioritizes readability and ease of interpretation for everyone.

            **Ethics:** Data visualization carries a significant ethical responsibility. In this project, I
            commit to presenting data truthfully and without manipulation. Care is taken to avoid misleading
            representations, misinterpretations, or the perpetuation of biases. The source and limitations of data
            will be acknowledged, fostering trust and promoting responsible data storytelling.
            """
        )