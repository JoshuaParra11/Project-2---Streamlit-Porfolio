import streamlit as st
import pandas as pd
import plotly.express as px
import os


def neighborhood_incidents(df):
    st.subheader("Incidents by Neighborhood")

    if "neighborhood_id" not in df.columns:
        st.error("Column 'neighborhood_id' not found in dataset.")
        return

    counts = (
        df["neighborhood_id"]
        .dropna()
        .value_counts()
        .nlargest(15)
        .reset_index()
        .rename(columns={"index": "Neighborhood", "neighborhood_id": "Incident Count"})
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
            - **Y-axis:** Top 15 neighborhoods.
            - **X-axis:** Total recorded incident count.
            - **Bar length and color:** Longer + lighter = more incidents.
            - **Hover:** Shows exact values.
            """
        )

    with right:
        st.subheader("Insights")
        st.markdown(
            """
            - A few neighborhoods account for most incidents.
            - **Five Points, Stapleton, CBD** consistently lead.
            - Sharp drop after the top 5–7 areas.
            - **Five Points** appears as an outlier.
            """
        )


def incidents_over_time(df):
    st.subheader("Incidents Over Time")
    st.info("Placeholder for an interactive time series chart.")
    st.markdown(
        """
        **How to Read This Chart:**
        - Bullet point 1  
        - Bullet point 2

        **Insights:**
        - Bullet point 1  
        - Bullet point 2
        """
    )


def type_distribution(df):
    st.subheader("Incident Type Distribution")
    st.info("Placeholder for a pie or donut chart.")
    st.markdown(
        """
        **How to Read This Chart:**
        - Bullet point 1  
        - Bullet point 2

        **Insights:**
        - Bullet point 1  
        - Bullet point 2
        """
    )


def heatmap_incidents(df):
    st.subheader("Heatmap of Incidents")
    st.info("Placeholder for a geographical heatmap.")
    st.markdown(
        """
        **How to Read This Chart:**
        - Bullet point 1  
        - Bullet point 2

        **Insights:**
        - Bullet point 1  
        - Bullet point 2
        """
    )


def render_eda_gallery():
    st.title("Exploratory Data Analysis (EDA) Gallery")

    base_path = os.path.dirname(__file__)
    project_root = os.path.join(base_path, "..")
    data_path = os.path.join(project_root, "Data", "Denver_Traffic_Clean.csv")

    try:
        df = pd.read_csv(data_path)
    except Exception as e:
        st.error(f"Error loading data at {data_path}: {e}")
        return

    neighborhood_incidents(df)
    st.write("---")

    incidents_over_time(df)
    st.write("---")

    type_distribution(df)
    st.write("---")

    heatmap_incidents(df)
