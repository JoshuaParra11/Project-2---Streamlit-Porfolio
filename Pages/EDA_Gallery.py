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

    # This list holds references to the functions that render each template.
    # We will add more functions (render_template_1, render_template_2, etc.) here later.
    templates = [render_template_0] 
    num_templates = len(templates)

    # --- Layout for Slider Navigation ---
    # This outer column provides a positioning context for the buttons.
    _, center_col, _ = st.columns([1, 10, 1])

    with center_col:
        # The slider-container div is targeted by our custom CSS in app.py
        st.markdown('<div class="slider-container">', unsafe_allow_html=True)

        # --- Main Display Area ---
        # Call the function for the current template, passing the DataFrame to it.
        current_template_func = templates[st.session_state.chart_template_index]
        current_template_func(df)

        # --- Navigation Buttons ---
        # These divs are positioned by the CSS to act as button containers.
        st.markdown('<div class="slider-button-container slider-button-prev">', unsafe_allow_html=True)
        if st.button("ΓÇ╣", key="prev_button_styled"):
            st.session_state.chart_template_index = (st.session_state.chart_template_index - 1) % num_templates
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="slider-button-container slider-button-next">', unsafe_allow_html=True)
        if st.button("ΓÇ║", key="next_button_styled"):
            st.session_state.chart_template_index = (st.session_state.chart_template_index + 1) % num_templates
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)