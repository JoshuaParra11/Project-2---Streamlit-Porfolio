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

    # --- Navigation Buttons (defined before the content) ---
    # We use columns here simply to get the buttons onto the page.
    # Their visual position will be entirely controlled by CSS and JavaScript.
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ΓÇ╣", key="prev_button_final"):
            st.session_state.chart_template_index = (st.session_state.chart_template_index - 1) % num_templates
            st.rerun()
    with col2:
        if st.button("ΓÇ║", key="next_button_final"):
            st.session_state.chart_template_index = (st.session_state.chart_template_index + 1) % num_templates
            st.rerun()

    # --- Main Display Area with a specific ID ---
    # We wrap the content in a div with a unique ID so our script can find it.
    st.markdown('<div id="slider-content-wrapper">', unsafe_allow_html=True)
    current_template_func = templates[st.session_state.chart_template_index]
    current_template_func(df)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- JavaScript to Reposition and Style Buttons ---
    st.components.v1.html("""
        <script>
            const wrapper = window.parent.document.getElementById('slider-content-wrapper');
            if (wrapper) {
                // Find all button elements rendered by Streamlit
                const buttons = window.parent.document.querySelectorAll('.stButton button');
                
                // Find our specific buttons by their inner text (the icon)
                const prevButton = Array.from(buttons).find(btn => btn.innerText === 'ΓÇ╣');
                const nextButton = Array.from(buttons).find(btn => btn.innerText === 'ΓÇ║');

                if (prevButton && nextButton) {
                    // Move the button's parent div into our wrapper
                    wrapper.appendChild(prevButton.closest('.stButton'));
                    wrapper.appendChild(nextButton.closest('.stButton'));

                    // Apply the CSS classes
                    prevButton.classList.add('slider-nav-button', 'prev');
                    nextButton.classList.add('slider-nav-button', 'next');
                }
            }
        </script>
    """, height=0)