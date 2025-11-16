import streamlit as st
import pandas as pd
import os

# --- Template 0: Placeholder Structure ---
# This function defines the content for the first slide.
def render_template_0(df):
    """
    Renders the structure for the first chart template:
    Chart on top, text explanations below.
    """
    # --- Chart Container ---
    with st.container():
        st.subheader("Chart Placeholder")
        st.write("This is where the first chart will go.")
        st.info("Placeholder for an interactive bar chart of traffic incidents.")

    # --- Text Explanations Container ---
    with st.container():
        st.write("---") # Separator
        st.subheader("Exploring Question: [Question for this chart]")
        st.markdown("""
        **How to Read This Chart:**
        - Bullet point 1
        - Bullet point 2
        - Bullet point 3

        **Observations & Insights:**
        - Bullet point 1
        - Bullet point 2
        - Bullet point 3
        """)

# --- Main Page Rendering Function ---
# This function controls the overall page layout, data loading, and slider navigation.
def render_eda_gallery():
    st.title("Exploratory Data Analysis (EDA) Gallery")
    
    # --- Data Loading ---
    base_path = os.path.dirname(__file__)
    project_root = os.path.join(base_path, "..")
    data_path = os.path.join(project_root, "Data", "Denver_Traffic_Clean.csv")
    
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        st.error(f"Cleaned data file not found at {data_path}. Please run the data cleaning script first.")
        return
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return

    # --- Slider Logic ---
    if 'chart_template_index' not in st.session_state:
        st.session_state.chart_template_index = 0

    templates = [render_template_0]
    num_templates = len(templates)

    # --- New Layout with JavaScript for Styling ---
    st.markdown('<div class="slider-container">', unsafe_allow_html=True)

    # --- Navigation Buttons (defined first, but will be positioned by CSS) ---
    # We use st.columns to place them logically, but CSS will override their visual position.
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ΓÇ╣", key="prev_button_styled"):
            st.session_state.chart_template_index = (st.session_state.chart_template_index - 1) % num_templates
            st.rerun()
    with col2:
        if st.button("ΓÇ║", key="next_button_styled"):
            st.session_state.chart_template_index = (st.session_state.chart_template_index + 1) % num_templates
            st.rerun()

    # --- Main Display Area ---
    current_template_func = templates[st.session_state.chart_template_index]
    current_template_func(df)

    # --- JavaScript to apply CSS classes to the buttons ---
    st.components.v1.html("""
        <script>
            // Find all button elements rendered by Streamlit
            const buttons = window.parent.document.querySelectorAll('.stButton button');
            
            // Find our specific buttons by their inner text (the icon)
            const prevButton = Array.from(buttons).find(btn => btn.innerText === 'ΓÇ╣');
            const nextButton = Array.from(buttons).find(btn => btn.innerText === 'ΓÇ║');

            // Apply the CSS classes
            if (prevButton) {
                prevButton.classList.add('slider-nav-button', 'prev');
            }
            if (nextButton) {
                nextButton.classList.add('slider-nav-button', 'next');
            }
        </script>
    """, height=0)

    st.markdown('</div>', unsafe_allow_html=True)