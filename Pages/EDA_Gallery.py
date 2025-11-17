import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Helper function to load data ---
@st.cache_data
def load_eda_data():
    base_path = os.path.dirname(__file__)
    project_root = os.path.join(base_path, "..")
    data_path = os.path.join(project_root, "Data", "Denver_Traffic_Clean.csv")
    try:
        df = pd.read_csv(data_path)
        df["reported_date"] = pd.to_datetime(df["reported_date"], errors='coerce')
        df.dropna(subset=["reported_date"], inplace=True)
        return df
    except Exception as e:
        st.error(f"Error loading data for EDA Gallery: {e}")
        return pd.DataFrame()

# --- Chart Functions ---

def neighborhood_incidents(df):
    st.subheader("Incidents by Neighborhood")

    if "neighborhood_id" not in df.columns:
        st.error("Column 'neighborhood_id' not found in dataset.")
        return

    # Correctly create and rename the counts DataFrame
    counts = (
        df["neighborhood_id"]
        .dropna()
        .value_counts()
        .nlargest(15)
        .reset_index()
        .rename(columns={"neighborhood_id": "Neighborhood", "count": "Incident Count"})
    )

    fig = px.bar(
        counts,
        x="Incident Count",
        y="Neighborhood",
        orientation="h",
        title="Top 15 Neighborhoods by Traffic Incident Count",
        color="Incident Count",
        color_continuous_scale=px.colors.sequential.Viridis,
    )

    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.subheader("How to Read This Chart")
        st.markdown(
            """
            - **Y-axis:** Top 15 neighborhoods with the most incidents.
            - **X-axis:** Total number of recorded incidents.
            - **Insight:** A small number of neighborhoods, particularly Five Points and Stapleton, account for a disproportionately high number of traffic incidents.
            """
        )
    with right:
        st.subheader("Insights")
        st.markdown(
            """
            - **Concentration:** Incident counts are heavily concentrated in a few central and high-traffic neighborhoods.
            - **Outliers:** Five Points stands out as a significant outlier, suggesting it may be a key area for traffic safety initiatives.
            - **Distribution:** There is a sharp drop-off in incident counts after the top 5-7 neighborhoods.
            """
        )


def incidents_over_time(df):
    st.subheader("Incidents Over Time")
    
    # Resample data by month for a clearer trend
    time_series_df = df.set_index('reported_date').resample('ME').size().reset_index(name='Incident Count')

    fig = px.line(
        time_series_df,
        x='reported_date',
        y='Incident Count',
        title='Monthly Traffic Incidents Over Time',
        labels={'reported_date': 'Month', 'Incident Count': 'Number of Incidents'}
    )
    
    fig.update_traces(mode='lines+markers')
    st.plotly_chart(fig, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.subheader("How to Read This Chart")
        st.markdown(
            """
            - **Y-axis:** Total number of incidents recorded in a given month.
            - **X-axis:** Timeline showing the progression of months.
            - **Line:** Represents the trend of incidents over the selected period.
            """
        )
    with right:
        st.subheader("Insights")
        st.markdown(
            """
            - **Seasonality:** Observe peaks and troughs that may correspond to seasonal changes (e.g., winter weather, summer holidays).
            - **Trends:** Look for any long-term upward or downward trends in accident frequency over the years.
            """
        )


def type_distribution(df):
    st.subheader("Incident Type Distribution")
    
    type_counts = df['top_traffic_accident_offense'].value_counts().nlargest(5).reset_index()
    type_counts.columns = ['Incident Type', 'Count']

    fig = px.pie(
        type_counts,
        names='Incident Type',
        values='Count',
        title='Top 5 Most Common Incident Types',
        hole=0.3
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.subheader("How to Read This Chart")
        st.markdown(
            """
            - **Slices:** Each slice represents a category of traffic offense.
            - **Size:** The size of the slice corresponds to its proportion of the total incidents.
            - **Labels:** Show the percentage and name for each category.
            """
        )
    with right:
        st.subheader("Insights")
        st.markdown(
            """
            - **Dominance:** General traffic accidents (`TRAF - ACCIDENT`) form the vast majority of incidents.
            - **Hit & Run:** "Hit & Run" incidents represent a significant portion, highlighting a common issue of drivers leaving the scene.
            """
        )


def heatmap_incidents(df):
    st.subheader("Geographical Heatmap of Incidents")
    
    map_df = df[['geo_lat', 'geo_lon']].dropna()
    map_df.columns = ['lat', 'lon']

    fig = px.density_mapbox(
        map_df,
        lat='lat',
        lon='lon',
        radius=8,
        center=dict(lat=39.7392, lon=-104.9903),
        zoom=10,
        mapbox_style="carto-positron",
        title="Heatmap of Incident Density"
    )
    
    st.plotly_chart(fig, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.subheader("How to Read This Chart")
        st.markdown(
            """
            - **Map:** A geographical map of Denver.
            - **Color Intensity:** Brighter, "hotter" areas indicate a higher concentration of traffic incidents.
            - **Zoom/Pan:** The map is interactive; you can zoom in to explore specific hotspots.
            """
        )
    with right:
        st.subheader("Insights")
        st.markdown(
            """
            - **Hotspots:** Major highways (like I-25) and central downtown arteries are clear hotspots for accidents.
            - **Corridors:** High-density corridors are visible along major roads such as Colfax Ave and Federal Blvd.
            """
        )


def render_eda_gallery():
    st.title("Exploratory Data Analysis (EDA) Gallery")
    st.write("This gallery presents several visualizations to explore the Denver traffic accident dataset from different perspectives.")
    
    df = load_eda_data()
    if df.empty:
        return

    st.write("---")
    neighborhood_incidents(df)
    
    st.write("---")
    incidents_over_time(df)
    
    st.write("---")
    type_distribution(df)
    
    st.write("---")
    heatmap_incidents(df)