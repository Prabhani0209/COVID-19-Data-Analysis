import streamlit as plt_st
import pandas as pd
import matplotlib.pyplot as plt

st = plt_st

st.title("COVID-19 Data Analysis Dashboard")

# # Load data (Fixed the file name to match your actual file)
df = pd.read_csv("data/processed/cleaned_covid_data.csv")

# # Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# # Total cases
st.subheader("Total Confirmed Cases")
total_cases = df["Confirmed"].sum()
st.write(f"{total_cases:,}")

# # Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# # Cases over time
st.subheader("COVID-19 Cases Over Time")
fig, ax = plt.subplots(figsize=(10, 5))

# Group by date so the timeline graph looks smooth and professional
daily_data = df.groupby("Date")["Confirmed"].sum()
ax.plot(daily_data.index, daily_data.values, color="#1f77b4", linewidth=2)

ax.set_xlabel("Date")
ax.set_ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
