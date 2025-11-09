import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Streamlit Portfolio", layout="wide")

# --- Session State Initialization ---
# This is the "memory" of your app. It helps remember which page is active
# and whether the sidebar is open, even when the user interacts with widgets.
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True  # Sidebar is open by default
if "page" not in st.session_state:
    st.session_state.page = "Bio"  # Default page is "Bio"

# --- Custom CSS ---
# This block injects CSS to style our custom sidebar and top bar.
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
        background-color: #0E1117; /* Dark background for the top bar */
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
        padding-top: 5rem; /* Pushes content down to avoid being hidden by the top bar */
    }

    /* --- Sidebar --- */
    div[data-testid="stHorizontalBlock"] > div:first-child {
        border-right: 2px solid #30333A; /* Vertical divider */
        background-color: #0E1117; /* Dark background for the sidebar */
    }

    /* --- Sidebar Buttons --- */
    .stButton > button {
        border: none;
        border-bottom: 1px solid #30333A; /* Dividers between buttons */
        background-color: transparent;
        color: white;
        text-align: left;
        font-size: 1rem;
        padding: 0.75rem 1rem;
        width: 100%; /* Makes buttons fill the sidebar width */
    }
    .stButton > button:hover {
        background-color: #1A1D23; /* Highlight on hover */
    }
    .stButton > button:focus {
        background-color: #262730; /* Highlight when active/clicked */
        color: #1DB954; /* A highlight color for the text */
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
</style>
""", unsafe_allow_html=True)


# --- Sidebar Toggle Function ---
# This function is called when the toggle button is clicked.
# It flips the value of 'sidebar_open' in the session state.
def toggle_sidebar():
    st.session_state.sidebar_open = not st.session_state.sidebar_open


# --- Top Bar ---
# We use a container to group the elements of our custom top bar.
with st.container():
    # Columns for layout: [toggle_button, page_title, empty_space]
    col1, col2, col3 = st.columns([1, 5, 1])
    with col1:
        # The icon changes based on whether the sidebar is open or closed.
        icon = "ΓåÉ" if st.session_state.sidebar_open else "Γÿ░"
        # This button calls the toggle_sidebar function when clicked.
        st.button(icon, on_click=toggle_sidebar, key="sidebar_toggle_button")
    with col2:
        # Displays the current page title in the center of the top bar.
        st.markdown(f"<div class='top-bar-center'>{st.session_state.page}</div>", unsafe_allow_html=True)
    # col3 is intentionally left empty for spacing.


# --- Layout with Custom Sidebar ---
# The layout changes based on the 'sidebar_open' state.
if st.session_state.sidebar_open:
    # If open, the sidebar column is wider.
    sidebar_col, main_col = st.columns([1.2, 4])
else:
    # If closed, the sidebar column is very narrow, effectively hiding it.
    sidebar_col, main_col = st.columns([0.05, 4.95])


# --- Sidebar Navigation ---
# This block defines the content of the sidebar.
with sidebar_col:
    if st.session_state.sidebar_open:
        st.markdown("<br>", unsafe_allow_html=True)  # Adds some space at the top.

        # Each button represents a page. When clicked, it updates the session state.
        if st.button("≡ƒôä Bio", use_container_width=True):
            st.session_state.page = "Bio"
            st.rerun()  # Rerun the script to show the new page content.

        if st.button("≡ƒôè Charts Gallery", use_container_width=True):
            st.session_state.page = "Charts Gallery"
            st.rerun()

        if st.button("≡ƒôê Dashboard", use_container_width=True):
            st.session_state.page = "Dashboard"
            st.rerun()

        if st.button("≡ƒº¡ Future Work", use_container_width=True):
            st.session_state.page = "Future Work"
            st.rerun()


# --- Page Rendering Functions ---
# Each function defines the content for a specific page.
def render_bio():
    st.title("≡ƒôä Bio")
    st.write("This is my biography page. Welcome to my portfolio!")
    st.write("Here, I'll share my background, skills, and professional journey.")

def render_charts_gallery():
    st.title("≡ƒôè Charts Gallery")
    st.write("This page will showcase a variety of data visualizations I've created.")
    st.info("Content for the charts gallery is coming soon.")

def render_dashboard():
    st.title("≡ƒôê Dashboard")
    st.write("This page will feature an interactive dashboard with data trends and patterns.")
    st.info("The dashboard is currently under construction.")

def render_future_work():
    st.title("≡ƒº¡ Future Work")
    st.write("This page outlines my plans for future projects and enhancements to this portfolio.")
    st.info("Details about future work will be added here.")

# A dictionary to map page names to their rendering functions.
page_renderer = {
    "Bio": render_bio,
    "Charts Gallery": render_charts_gallery,
    "Dashboard": render_dashboard,
    "Future Work": render_future_work,
}

# --- Render the Selected Page in the Main Column ---
with main_col:
    # Add a div with a class to apply padding, preventing content from being hidden by the top bar.
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    # This line calls the correct rendering function based on the current page in the session state.
    page_renderer[st.session_state.page]()
    st.markdown('</div>', unsafe_allow_html=True)