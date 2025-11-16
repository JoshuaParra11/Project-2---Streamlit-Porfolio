import streamlit as st
import pandas as pd
import os

# --- Template Placeholders ---
# Define a function for each chart template.

def render_template_0(df):
    """Renders the first chart template."""
    with st.container(border=True):
        st.subheader("Template 1: Incidents by Neighborhood")
        st.info("Placeholder for an interactive bar chart.")
        st.markdown("""
        **How to Read This Chart:**
        - Bullet point 1
        - Bullet point 2
        
        **Observations & Insights:**
        - Bullet point 1
        - Bullet point 2
        """)

def render_template_1(df):
    """Renders the second chart template."""
    with st.container(border=True):
        st.subheader("Template 2: Incidents Over Time")
        st.info("Placeholder for an interactive line chart.")
        st.markdown("""
        **How to Read This Chart:**
        - Bullet point 1
        - Bullet point 2
        
        **Observations & Insights:**
        - Bullet point 1
        - Bullet point 2
        """)

def render_template_2(df):
    """Renders the third chart template."""
    with st.container(border=True):
        st.subheader("Template 3: Incident Type Distribution")
        st.info("Placeholder for a pie or donut chart.")
        st.markdown("""
        **How to Read This Chart:**
        - Bullet point 1
        - Bullet point 2
        
        **Observations & Insights:**
        - Bullet point 1
        - Bullet point 2
        """)

def render_template_3(df):
    """Renders the fourth chart template."""
    with st.container(border=True):
        st.subheader("Template 4: Heatmap of Incidents")
        st.info("Placeholder for a geographical heatmap.")
        st.markdown("""
        **How to Read This Chart:**
        - Bullet point 1
        - Bullet point 2
        
        **Observations & Insights:**
        - Bullet point 1
        - Bullet point 2
        """)

# --- Main Page Rendering Function ---
def render_eda_gallery():
    st.title("Exploratory Data Analysis (EDA) Gallery")
    
    # --- Data Loading ---
    base_path = os.path.dirname(__file__)
    project_root = os.path.join(base_path, "..")
    data_path = os.path.join(project_root, "Data", "Denver_Traffic_Clean.csv")
    
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        st.error(f"Cleaned data file not found at {data_path}.")
        return
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return

    # --- Slider Logic ---
    if 'chart_template_index' not in st.session_state:
        st.session_state.chart_template_index = 0

    # This list holds references to the functions that render each template.
    templates = [render_template_0, render_template_1, render_template_2, render_template_3] 
    num_templates = len(templates)

    # --- Layout for Slider Navigation ---
    st.markdown('<div class="slider-container">', unsafe_allow_html=True)
    
    col_prev, col_main, col_next = st.columns([1.5, 10, 1.5])

    with col_prev:
        st.markdown('<div class="slider-button-col prev">', unsafe_allow_html=True)
        if st.button("ΓÇ╣", use_container_width=True, key="prev_styled"):
            st.session_state.chart_template_index = (st.session_state.chart_template_index - 1) % num_templates
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col_main:
        # Call the function for the current template
        current_template_func = templates[st.session_state.chart_template_index]
        current_template_func(df)

    with col_next:
        st.markdown('<div class="slider-button-col next">', unsafe_allow_html=True)
        if st.button("ΓÇ║", use_container_width=True, key="next_styled"):
            st.session_state.chart_template_index = (st.session_state.chart_template_index + 1) % num_templates
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)