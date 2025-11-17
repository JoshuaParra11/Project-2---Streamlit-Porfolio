import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime, date # Import date from datetime

# --- Data Loading and Caching ---
@st.cache_data
def load_data():
    """
    Loads, cleans, and caches the traffic accident data.
    Converts 'reported_date' to datetime objects.
    """
    base_path = os.path.dirname(__file__)
    project_root = os.path.join(base_path, "..")
    data_path = os.path.join(project_root, "Data", "Denver_Traffic_Clean.csv")
    
    try:
        df = pd.read_csv(data_path)
        # Convert date column to datetime, coercing errors to NaT (Not a Time)
        df["reported_date"] = pd.to_datetime(df["reported_date"], errors='coerce')
        # Drop rows where date conversion failed
        df.dropna(subset=["reported_date"], inplace=True)
        return df
    except FileNotFoundError:
        st.error(f"Error: Data file not found at {data_path}")
        return pd.DataFrame() # Return empty dataframe on error
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return pd.DataFrame()

# --- Main Render Function ---
def render_dashboard():
    """
    Renders the entire interactive dashboard page.
    """
    st.title("Denver Traffic Accidents Dashboard")

    df = load_data()
    if df.empty:
        st.warning("Dashboard cannot be displayed because the data could not be loaded.")
        return

    # --- Main Page Filters ---
    with st.expander("Dashboard Filters", expanded=True):
        # Date Range Slider
        min_overall_date = df["reported_date"].min().date()
        max_overall_date = df["reported_date"].max().date()
        
        # Ensure default value is within min/max range
        default_start_date = min_overall_date
        default_end_date = max_overall_date

        selected_date_range = st.slider(
            "Select Date Range",
            min_value=min_overall_date,
            max_value=max_overall_date,
            value=(default_start_date, default_end_date),
            format="MM/DD/YYYY"
        )
        start_date, end_date = selected_date_range

        # Neighborhood Multiselect Filter
        neighborhoods = sorted(df["neighborhood_id"].dropna().unique())
        selected_neighborhoods = st.multiselect(
            "Neighborhoods",
            options=neighborhoods,
            default=neighborhoods[:5] # Default to first 5 for demonstration
        )

    # --- Filtering Logic ---
    # Convert start_date and end_date from slider (date objects) to datetime for comparison
    start_datetime = pd.to_datetime(start_date)
    end_datetime = pd.to_datetime(end_date).replace(hour=23, minute=59, second=59) # End of the selected day

    # Apply filters to the DataFrame
    filtered_df = df[
        (df["reported_date"] >= start_datetime) &
        (df["reported_date"] <= end_datetime) &
        (df["neighborhood_id"].isin(selected_neighborhoods))
    ]

    if filtered_df.empty:
        st.warning("No data available for the selected filters. Please expand your selection.")
        return

    # --- Key Performance Indicators (KPIs) ---
    st.header("Key Metrics")
    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric(
            label="Total Incidents",
            value=f"{filtered_df.shape[0]:,}"
        )
    with kpi2:
        st.metric(
            label="Total Serious Injuries",
            value=f"{int(filtered_df['SERIOUSLY_INJURED'].sum()):,}"
        )
    with kpi3:
        st.metric(
            label="Total Fatalities",
            value=f"{int(filtered_df['FATALITIES'].sum()):,}"
        )

    st.write("---")

    # --- Linked Visualizations ---
    st.header("Linked Visuals")
    col1, col2 = st.columns([2, 1.5])

    with col1:
        st.subheader("Incident Map")
        # Drop rows with missing lat/lon for mapping
        map_data = filtered_df[['geo_lat', 'geo_lon']].dropna()
        map_data.rename(columns={'geo_lat': 'lat', 'geo_lon': 'lon'}, inplace=True)
        if not map_data.empty:
            st.map(map_data, zoom=10)
        else:
            st.info("No location data to display for the selected filters.")

    with col2:
        st.subheader("Incidents by Light Condition")
        light_counts = filtered_df["LIGHT_CONDITION"].value_counts().reset_index()
        light_counts.columns = ["Light Condition", "Incident Count"]
        
        fig = px.bar(
            light_counts,
            x="Incident Count",
            y="Light Condition",
            orientation='h',
            title="Traffic Incidents by Light Condition",
            color="Incident Count",
            color_continuous_scale=px.colors.sequential.Viridis
        )
        fig.update_layout(
            yaxis={'categoryorder':'total ascending'},
            margin=dict(l=10, r=10, t=40, b=10)
        )
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")

    # --- Narrative & Insights ---
    st.header("Narrative & Insights")
    st.markdown(
        """
        - **Geographic Concentration:** Incidents are heavily concentrated in the selected neighborhoods, with hotspots often visible near major intersections or commercial zones.
        - **Time Sensitivity:** Use the date filter to explore seasonal trends. You may notice shifts in incident frequency during holidays or different seasons.
        - **Lighting Conditions Matter:** The bar chart reveals the distribution of accidents under different lighting. 'Daylight' typically has the highest raw count, but analyzing incidents during 'Dawn/Dusk' or 'Darkness' relative to traffic volume could reveal higher risk periods.
        - **Filter Interaction:** Notice how the "Incidents by Light Condition" chart changes as you select or deselect neighborhoods, providing localized insights.
        - **Data Limitation:** The map only shows incidents where precise geographic coordinates (latitude/longitude) were successfully recorded.
        """
    )

    st.write("---")

    # --- Reproducibility Section ---
    st.header("Reproducibility")
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("Source: [Denver Open Data Catalog - Traffic Accidents](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-traffic-accidents)")
    with col_right:
        st.markdown(f"Last refreshed: **{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**")