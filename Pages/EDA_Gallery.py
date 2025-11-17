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
        # Ensure injury column is numeric
        df['SERIOUSLY_INJURED'] = pd.to_numeric(df['SERIOUSLY_INJURED'], errors='coerce').fillna(0)
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
            - **Insight:** A small number of neighborhoods account for a disproportionately high number of traffic incidents.
            """
        )
    with right:
        st.subheader("Insights")
        st.markdown(
            """
            - **Concentration:** Incident counts are heavily concentrated in a few central and high-traffic neighborhoods.
            - **Outliers:** Five Points stands out as a significant outlier.
            - **Distribution:** There is a sharp drop-off in incident counts after the top 5-7 neighborhoods.
            """
        )


def incidents_over_time(df):
    st.subheader("Incidents Over Time")
    
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
            - **Seasonality:** Observe peaks and troughs that may correspond to seasonal changes.
            - **Trends:** Look for any long-term upward or downward trends in accident frequency.
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
            """
        )
    with right:
        st.subheader("Insights")
        st.markdown(
            """
            - **Dominance:** General traffic accidents (`TRAF - ACCIDENT`) form the vast majority of incidents.
            - **Hit & Run:** "Hit & Run" incidents represent a significant portion of offenses.
            """
        )


def injuries_by_light_condition(df):
    st.subheader("Distribution of Injuries by Light Condition")

    # Filter out rows where injuries are 0 to make the box plot more readable
    injured_df = df[df['SERIOUSLY_INJURED'] > 0]

    if injured_df.empty:
        st.info("No incidents with serious injuries to display in the box plot.")
        return

    fig = px.box(
        injured_df,
        x='LIGHT_CONDITION',
        y='SERIOUSLY_INJURED',
        color='LIGHT_CONDITION',
        title='Serious Injury Distribution per Light Condition',
        labels={'LIGHT_CONDITION': 'Light Condition', 'SERIOUSLY_INJURED': 'Number of Serious Injuries'}
    )
    
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.subheader("How to Read This Chart")
        st.markdown(
            """
            - **Box:** Represents the interquartile range (IQR), where the middle 50% of the data points lie.
            - **Line in Box:** The median number of injuries.
            - **Whiskers:** Show the range of the data, excluding outliers.
            - **Dots:** Individual data points that are considered outliers.
            """
        )
    with right:
        st.subheader("Insights")
        st.markdown(
            """
            - **Severity:** While 'Daylight' has the most incidents, this chart shows the *distribution* of injury counts for the accidents in each condition.
            - **Median:** The median for most categories is 1, indicating that when an injury occurs, it's typically a single person.
            - **Outliers:** Note the outliers in each category, representing the less common but more severe multi-injury incidents.
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
    injuries_by_light_condition(df)