import streamlit as st
import pandas as pd
import altair as alt

# Sample data (Player performance split into 3 parts)
data = {
    "Player": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Kills": [40, 30, 50, 20, 35],   # First segment
    "Assists": [30, 25, 35, 20, 30], # Second segment
    "Deaths": [15, 15, 10, 20, 15]   # Third segment
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate total score for sorting
df["Total Score"] = df["Kills"] + df["Assists"] + df["Deaths"]

# Sort players by total score (highest first)
df = df.sort_values(by="Total Score", ascending=False)

# Convert to long format for stacked bar chart
df_melted = df.melt(id_vars=["Player", "Total Score"], var_name="Category", value_name="Score")

# Streamlit UI
st.title("🏆 Game Leaderboard")
st.write("A stacked horizontal bar chart showing performance breakdown with actual scores.")

# Define colors for each segment
color_scale = alt.Scale(domain=["Kills", "Assists", "Deaths"], range=["#3498db", "#2ecc71", "#e74c3c"])

# Create the stacked horizontal bar chart with actual values
chart = alt.Chart(df_melted).mark_bar().encode(
    x=alt.X("Score:Q", title="Total Score"),
    y=alt.Y("Player:N", sort="-x", title="Player"),
    color=alt.Color("Category:N", scale=color_scale, title="Category"),
    tooltip=["Player", "Category", "Score"]
).properties(
    width=600,
    height=300
)

# Display the chart
st.altair_chart(chart, use_container_width=True)
