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

    templates = [render_template_0, render_template_1, render_template_2, render_template_3] 
    num_templates = len(templates)

    # --- Main Display Area ---
    # This container will hold the currently selected chart template
    with st.container():
        current_template_func = templates[st.session_state.chart_template_index]
        current_template_func(df)

    # --- Navigation Controls Container ---
    # This container holds the buttons and dot indicators below the chart
    with st.container():
        # Wrap everything in a div with our custom class for styling
        st.markdown('<div class="nav-container">', unsafe_allow_html=True)

        # Use columns *inside* the nav-container to lay out the buttons and dots
        col_btn_prev, col_dots, col_btn_next = st.columns([1, 3, 1])

        with col_btn_prev:
            if st.button("ΓÇ╣", key="prev_nav", use_container_width=True):
                st.session_state.chart_template_index = (st.session_state.chart_template_index - 1) % num_templates
                st.rerun()

        with col_dots:
            dots_html = '<div class="dot-container">'
            for i in range(num_templates):
                if i == st.session_state.chart_template_index:
                    dots_html += '<span class="dot active"></span>'
                else:
                    dots_html += '<span class="dot"></span>'
            dots_html += '</div>'
            st.markdown(dots_html, unsafe_allow_html=True)

        with col_btn_next:
            if st.button("ΓÇ║", key="next_nav", use_container_width=True):
                st.session_state.chart_template_index = (st.session_state.chart_template_index + 1) % num_templates
                st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)