import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("COVID-19 Data Analysis Dashboard")

# Load data
df = pd.read_csv("data/covid_19_clean_complete.csv")

# Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Total cases
st.subheader("Total Confirmed Cases")

total_cases = df["Confirmed"].sum()

st.write(total_cases)


# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])


# Cases over time
st.subheader("COVID-19 Cases Over Time")

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(df["Date"], df["Confirmed"])

ax.set_xlabel("Date")
ax.set_ylabel("Confirmed Cases")

plt.xticks(rotation=45)

st.pyplot(fig)