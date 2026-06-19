import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(page_title="Job Analytics Pro", layout="wide")

st.title("💼 Job Market Analytics Dashboard")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql123",
    database="job_market_db"
)

query = "SELECT * FROM job_listings"
df = pd.read_sql(query, conn)

# Sidebar
st.sidebar.header("Filters")

company = st.sidebar.selectbox(
    "Company",
    ["All"] + sorted(df["company"].unique().tolist())
)

location = st.sidebar.selectbox(
    "Location",
    ["All"] + sorted(df["location"].unique().tolist())
)

# Filtering
filtered_df = df.copy()

if company != "All":
    filtered_df = filtered_df[
        filtered_df["company"] == company
    ]

if location != "All":
    filtered_df = filtered_df[
        filtered_df["location"] == location
    ]

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Jobs", len(filtered_df))

with col2:
    st.metric("Companies", filtered_df["company"].nunique())

with col3:
    st.metric("Locations", filtered_df["location"].nunique())

st.divider()

# Charts
st.subheader("Top Companies")
st.bar_chart(
    filtered_df["company"].value_counts().head(10)
)

st.subheader("Top Locations")
st.bar_chart(
    filtered_df["location"].value_counts().head(10)
)

st.divider()

st.subheader("Job Listings")
st.dataframe(filtered_df, use_container_width=True)