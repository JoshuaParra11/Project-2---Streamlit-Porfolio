import streamlit as st

def render_future_work():
    st.title("Future Work")

    with st.container(border=True):
        st.write("### Concrete Next Steps")
        st.markdown("""
        - **Implement Advanced EDA Charts:** Expand the EDA Gallery with more interactive visualizations, such
            as geographical heatmaps of incidents, time-series plots of accident frequency, and correlation
            matrices.
        - **Develop Interactive Dashboard:** Create a dedicated dashboard page with key performance indicators
            (KPIs) and filters to allow users to explore specific trends and patterns in the traffic accident data.
        - **Add Accessibility Settings:** Introduce user-configurable accessibility options, including color
            presets (e.g., high-contrast, colorblind-friendly palettes) and font size adjustments, to enhance
            usability for all users.
        - **Integrate Machine Learning Model:** Explore integrating a predictive model to forecast accident hotspots
            or identify contributing factors, providing actionable insights.
        - **Data Enrichment:** Incorporate external datasets (e.g., weather data, demographic information) to
            enrich the analysis and uncover deeper correlations.
        """)

        st.write("---") # Separator
        st.write("### Brief Reflection: From Paper Prototype to Final Build")
        st.markdown("""
        - **Initial Design vs. Implementation:** I did change a lot, I wanted to implement the slider with different templates for the EDA Gallery
                    but got errors that made me simplify the layout to a normal standard page.
        - **Challenges Encountered:** Trying to use AI as little as possible I personally named files pertaining to data and other files
                    that I had no idea github required in a specific way so I had to deal with trouble for a couple of days. I
                    also got some requirements trouble as I learned to work with virtual environments and making sure the linux
                    environment in Streamlit's community cloud had the appropriate resources and modules for the app the work correctly.
        - **Unexpected Discoveries:** Something that I learned was to make my own sidebar with buttons for better custom styling options,
                    I learned to render or display the content using session states and reruns such that the app did
                    not have to reload and refresh the content. This made the user experience smoother for me as I just use one
                    continuous page.
        - **Impact of Streamlit:** Using Streamlit was a bit tedious and hard for me as I had no experience before this project. However, I
                    liked how easily and fast it got a beginner website running. I understood why Streamlit is a good
                    platform to start CS students working on a derivative website workflow. However, I researched other platforms
                    such as node, along with javascript that offer more features that are modern and scalable in a more website
                    developing traditional workflow.
        """)