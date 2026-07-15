import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="COVID-19 Data Analysis Dashboard",
    page_icon="🦠",
    layout="wide"
)

# Title
st.title("🦠 COVID-19 Data Analysis Dashboard")
st.markdown(
    "Interactive analysis of COVID-19 cases, recoveries, deaths and trends using data visualization."
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/covid_19_clean_complete.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Sidebar
st.sidebar.header("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country/Region"].unique(),
    default=list(df["Country/Region"].unique())[:5]
)

filtered_df = df[df["Country/Region"].isin(countries)]

# Summary metrics
st.subheader("📊 Overall Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Confirmed Cases",
        f"{filtered_df['Confirmed'].sum():,}"
    )

with col2:
    st.metric(
        "Total Recoveries",
        f"{filtered_df['Recovered'].sum():,}"
    )

with col3:
    st.metric(
        "Total Deaths",
        f"{filtered_df['Deaths'].sum():,}"
    )


# Time trend
st.subheader("📈 COVID-19 Trend Over Time")

trend = (
    filtered_df.groupby("Date")[["Confirmed", "Recovered", "Deaths"]]
    .sum()
    .reset_index()
)

fig = px.line(
    trend,
    x="Date",
    y=["Confirmed", "Recovered", "Deaths"],
    title="COVID-19 Cases Trend"
)

st.plotly_chart(fig, use_container_width=True)


# Country comparison
st.subheader("🌍 Country-wise Analysis")

country_data = (
    filtered_df.groupby("Country/Region")[["Confirmed","Recovered","Deaths"]]
    .max()
    .reset_index()
)

fig2 = px.bar(
    country_data,
    x="Country/Region",
    y="Confirmed",
    title="Confirmed Cases by Country"
)

st.plotly_chart(fig2, use_container_width=True)


# Show data
st.subheader("📄 Dataset Preview")
st.dataframe(filtered_df.head(20))