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
    /* This rule now only applies the background color to the first column of stHorizontalBlock */
    /* The border-right is removed from this general rule */
    div[data-testid="stHorizontalBlock"] > div:first-child {
        background-color: #0E1117; /* subtle darker background for sidebar area */
    }

    /* This new rule specifically targets the actual Streamlit sidebar's first column to add the divider */
    /* The Streamlit sidebar itself has a data-testid="stSidebar" */
    div[data-testid="stSidebar"] > div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] > div:first-child {
        border-right: 2px solid #30333A; /* divider between sidebar and main area */
    }

     /* --- Sidebar Buttons --- */
    .stButton > button {
        border: none;
        border-bottom: 1px solid #30333A; /* Dividers between buttons */
        background-color: transparent; /* No background color by default */
        color: white;
        text-align: left;
        font-size: 1rem;
        padding: 0.75rem 1rem;
        /* Remove width: 100%; to allow button to size to content */
        /* width: 100%; */
        display: inline-block; /* Allow button to shrink to content width */
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
    .nav-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding-top: 1rem;
    }

    /* Style for the Streamlit button's parent container */
    .nav-container .stButton {
        margin: 0 1rem; /* Adds space around the buttons */
    }

    /* Style for the actual button element */
    .nav-container .stButton > button {
        width: 40px;
        height: 40px;
        padding: 0;
        border-radius: 50%; /* Makes it circular */
        background-color: #f0f2f6;
        color: #31333F;
        border: 1px solid #dcdcdc;
    }
    .nav-container .stButton > button:hover {
        background-color: #e6e6e6;
    }

    /* Styling for the dot indicators */
    .dot-container {
        display: flex;
        align-items: center;
    }
    .dot {
        height: 10px;
        width: 10px;
        background-color: #bbb;
        border-radius: 50%;
        display: inline-block;
        margin: 0 5px;
    }
    .dot.active {
        background-color: #31333F; /* Darker color for the active dot */
        transform: scale(1.2); /* Make it slightly bigger */
        transition: transform 0.2s ease-in-out; /* Smooth transition */
    }
</style>
""", unsafe_allow_html=True)


# --- Sidebar Toggle Function ---
def toggle_sidebar():
    st.session_state.sidebar_open = not st.session_state.sidebar_open

# --- Top Bar ---
st.markdown('<div class="custom-top-bar">', unsafe_allow_html=True) # Add this wrapper
with st.container():
    col1, col2, col3 = st.columns([1, 5, 1])
    with col1:
        icon = "<<" if st.session_state.sidebar_open else ">>"
        st.button(icon, on_click=toggle_sidebar, key="sidebar_toggle_button")
    with col2:
        st.markdown(f"<div class='top-bar-center'>{st.session_state.page}</div>", unsafe_allow_html=True)
    with col3:
        st.write("")
st.markdown('</div>', unsafe_allow_html=True) # Close the wrapper

# --- Layout with Custom Sidebar ---
if st.session_state.sidebar_open:
    sidebar_col, main_col = st.columns([1.2, 4])
else:
    # When closed, we still create the columns but make the first one very small
    sidebar_col, main_col = st.columns([0.05, 4.95])

# --- Sidebar Navigation ---
with sidebar_col:
    if st.session_state.sidebar_open:
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Home"): # use_container_width=True removed
            st.session_state.page = "Home"
            st.session_state.sidebar_open = False
            st.rerun()

        if st.button("About Me"): # use_container_width=True removed
            st.session_state.page = "About Me"
            st.session_state.sidebar_open = False
            st.rerun()

        if st.button("EDA Gallery"): # use_container_width=True removed
            st.session_state.page = "EDA Gallery"
            st.session_state.sidebar_open = False
            st.rerun()

        if st.button("Dashboard"): # use_container_width=True removed
            st.session_state.page = "Dashboard"
            st.session_state.sidebar_open = False
            st.rerun()

        if st.button("Future Work"): # use_container_width=True removed
            st.session_state.page = "Future Work"
            st.session_state.sidebar_open = False
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