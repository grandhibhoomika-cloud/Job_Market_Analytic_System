import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Job Analytics Pro",
    layout="wide"
)

# Load CSV
df = pd.read_csv("jobs.csv")

# Remove accidental spaces in column names
df.columns = df.columns.str.strip()

# Title
st.title("💼 Job Market Analytics Dashboard")

# ---------------- Sidebar ----------------
st.sidebar.header("🔍 Filters")

company = st.sidebar.selectbox(
    "Company",
    ["All"] + sorted(df["Company"].unique().tolist())
)

location = st.sidebar.selectbox(
    "Location",
    ["All"] + sorted(df["Location"].unique().tolist())
)

# ---------------- Filtering ----------------
filtered_df = df.copy()

if company != "All":
    filtered_df = filtered_df[
        filtered_df["Company"] == company
    ]

if location != "All":
    filtered_df = filtered_df[
        filtered_df["Location"] == location
    ]

# ---------------- KPI Cards ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Jobs", len(filtered_df))

with col2:
    st.metric(
        "Companies",
        filtered_df["Company"].nunique()
    )

with col3:
    st.metric(
        "Locations",
        filtered_df["Location"].nunique()
    )

st.divider()

# ---------------- Charts ----------------
st.subheader("📊 Top Companies")

st.bar_chart(
    filtered_df["Company"]
    .value_counts()
    .head(10)
)

st.subheader("📍 Top Locations")

st.bar_chart(
    filtered_df["Location"]
    .value_counts()
    .head(10)
)

st.divider()

# ---------------- Table ----------------
st.subheader("📄 Job Listings")

st.dataframe(
    filtered_df,
    use_container_width=True
)
