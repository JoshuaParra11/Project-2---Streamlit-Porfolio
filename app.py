import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

# Import render functions from the pages directory
from Pages.Home import render_home
from Pages.About_me import render_about_me
from Pages.EDA_Gallery import render_eda_gallery
from Pages.Dashboard import render_dashboard
from Pages.Future_Work import render_future_work

# --- Page Setup ---
st.set_page_config(page_title="Streamlit Portfolio", layout="wide")

# --- Session State Initialization ---
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True
if "page" not in st.session_state:
    st.session_state.page = "Home"  # Default page is now "Home"

# --- Custom CSS ---
st.markdown("""
<style>
    /* Hides the default Streamlit hamburger menu */
    button[title="View fullscreen"] {
        visibility: hidden;
    }
    .css-15zrgzn {
        display: none;
    }

    /* --- Top Bar --- */
    .top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #0E1117;
        padding: 0.75rem 1.5rem;
        border-bottom: 1px solid #30333A;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
    }
    .top-bar-center {
        flex: 1;
        justify-content: center;
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
        text-align: center;
    }

    /* --- Main content area padding --- */
    .main-content {
        padding-top: 5rem;
    }

    /* --- Sidebar --- */
    div[data-testid="stHorizontalBlock"] > div:first-child {
        border-right: 2px solid #30333A;
        background-color: #0E1117;
    }

    /* --- Sidebar Buttons --- */
    .stButton > button {
        border: none;
        border-bottom: 1px solid #30333A;
        background-color: transparent;
        color: white;
        text-align: left;
        font-size: 1rem;
        padding: 0.75rem 1rem;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #1A1D23;
    }
    .stButton > button:focus {
        background-color: #262730;
        color: #1DB954;
    }

    /* --- Toggle Button --- */
    .sidebar-toggle {
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0;
        margin: 0;
    }
    
    /* --- Slider Navigation Styling --- */
    #slider-content-wrapper {
        position: relative; /* This is the anchor for our buttons */
    }

    .stButton > button.slider-nav-button {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background-color: rgba(255, 255, 255, 0.7);
        color: #0E1117;
        border: 1px solid rgba(0, 0, 0, 0.1);
        z-index: 100;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0;
    }
    .stButton > button.slider-nav-button:hover {
        background-color: white;
    }

    .stButton > button.slider-nav-button.prev {
        left: 5px; /* Positioned just inside the left edge */
    }

    .stButton > button.slider-nav-button.next {
        right: 5px; /* Positioned just inside the right edge */
    }
</style>
""", unsafe_allow_html=True)


# --- Sidebar Toggle Function ---
def toggle_sidebar():
    st.session_state.sidebar_open = not st.session_state.sidebar_open


# --- Top Bar ---
with st.container():
    col1, col2, col3 = st.columns([1, 5, 1])
    with col1:
        icon = "»" if st.session_state.sidebar_open else "«"
        st.button(icon, on_click=toggle_sidebar, key="sidebar_toggle_button")
    with col2:
        st.markdown(f"<div class='top-bar-center'>{st.session_state.page}</div>", unsafe_allow_html=True)


# --- Layout with Custom Sidebar ---
if st.session_state.sidebar_open:
    sidebar_col, main_col = st.columns([1.2, 4])
else:
    sidebar_col, main_col = st.columns([0.05, 4.95])

# --- Sidebar Navigation ---
with sidebar_col:
    if st.session_state.sidebar_open:
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Home", use_container_width=True):
            st.session_state.page = "Home"
            st.session_state.sidebar_open = False # Add this line
            st.rerun()

        if st.button("About Me", use_container_width=True):
            st.session_state.page = "About Me"
            st.session_state.sidebar_open = False # Add this line
            st.rerun()

        if st.button("EDA Gallery", use_container_width=True):
            st.session_state.page = "EDA Gallery"
            st.session_state.sidebar_open = False # Add this line
            st.rerun()

        if st.button("Dashboard", use_container_width=True):
            st.session_state.page = "Dashboard"
            st.session_state.sidebar_open = False # Add this line
            st.rerun()

        if st.button("Future Work", use_container_width=True):
            st.session_state.page = "Future Work"
            st.session_state.sidebar_open = False # Add this line
            st.rerun()

# --- Page Rendering Dictionary ---
# The dictionary is updated to include "Home" and use "About Me"
page_renderer = {
    "Home": render_home,
    "About Me": render_about_me,
    "EDA Gallery": render_eda_gallery,
    "Dashboard": render_dashboard,
    "Future Work": render_future_work,
}

# --- Render the Selected Page in the Main Column ---
with main_col:
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    # This calls the correct render function based on the current page in session state
    page_renderer[st.session_state.page]()
    st.markdown('</div>', unsafe_allow_html=True)