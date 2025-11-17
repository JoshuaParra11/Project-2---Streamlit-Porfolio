import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime, date

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
        df["reported_date"] = pd.to_datetime(df["reported_date"], errors='coerce')
        df.dropna(subset=["reported_date"], inplace=True)
        # Ensure injury/fatality columns are numeric
        df['SERIOUSLY_INJURED'] = pd.to_numeric(df['SERIOUSLY_INJURED'], errors='coerce').fillna(0)
        df['FATALITIES'] = pd.to_numeric(df['FATALITIES'], errors='coerce').fillna(0)
        return df
    except FileNotFoundError:
        st.error(f"Error: Data file not found at {data_path}")
        return pd.DataFrame()
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
        min_overall_date = df["reported_date"].min().date()
        max_overall_date = df["reported_date"].max().date()
        
        selected_date_range = st.slider(
            "Select Date Range",
            min_value=min_overall_date,
            max_value=max_overall_date,
            value=(min_overall_date, max_overall_date),
            format="MM/DD/YYYY"
        )
        start_date, end_date = selected_date_range

        neighborhoods = sorted(df["neighborhood_id"].dropna().unique())
        selected_neighborhoods = st.multiselect(
            "Neighborhoods",
            options=neighborhoods,
            default=neighborhoods[:5]
        )

    # --- Filtering Logic ---
    start_datetime = pd.to_datetime(start_date)
    end_datetime = pd.to_datetime(end_date).replace(hour=23, minute=59, second=59)

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

    total_incidents = filtered_df.shape[0]
    total_serious_injuries = filtered_df['SERIOUSLY_INJURED'].sum()
    
    injury_rate = (total_serious_injuries / total_incidents * 100) if total_incidents > 0 else 0

    with kpi1:
        st.metric(
            label="Total Incidents",
            value=f"{total_incidents:,}"
        )
    with kpi2:
        st.metric(
            label="Serious Injury Rate",
            value=f"{injury_rate:.2f}%"
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
            color_continuous_scale=px.colors.sequential.Viridis # Viridis is color-blind safe
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
        - **Filter Interaction:** Notice how the "Serious Injury Rate" and charts change as you select or deselect neighborhoods, providing localized insights.
        - **Data Limitation:** The map only shows incidents where precise geographic coordinates (latitude/longitude) were successfully recorded.
        """
    )

    st.write("---")

    # --- Reproducibility & Ethics ---
    st.header("Data Source & Ethical Considerations")
    
    st.markdown("Source: [Denver Open Data Catalog - Traffic Accidents](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-traffic-accidents)")
    st.markdown(f"Last refreshed: **{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**")

    with st.container(border=True):
        st.subheader("Ethics Note")
        st.markdown(
            """
            This dataset includes records of real traffic incidents involving people, so results must be interpreted carefully. 
            Because the data comes from official incident reports, it may contain reporting biases and does not capture near-misses or unreported accidents. 
            The visualizations show patterns in the aggregate data but should not be used to make judgments about individual drivers or to generalize about the safety of specific locations without further context.
            """
        )