import streamlit as st
import pandas as pd
import altair as alt

# Sample data (Player performance split into 3 parts)
data = {
    "Player": ["Khanh", "Cong", "Tai", "Duy", "Hung"],
    "Pure Fiction": [40, 30, 50, 20, 35],   # First segment
    "Apocalyptic Shadow": [30, 25, 35, 20, 30], # Second segment
    "Moc": [15, 15, 10, 20, 15]   # Third segment
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate total score for sorting
df["Total Score"] = df["Pure Fiction"] + df["Apocalyptic Shadow"] + df["Moc"]

# Sort players by total score (highest first)
df = df.sort_values(by="Total Score", ascending=False)

# Convert to long format for stacked bar chart
df_melted = df.melt(id_vars=["Player", "Total Score"], var_name="Category", value_name="Score")

# Streamlit UI
st.title("🏆 Honkai Star Rail Leaderboard")
st.write("test")

# Define colors for each segment
color_scale = alt.Scale(domain=["Pure Fiction", "Apocalyptic Shadow", "Moc"], range=["#3498db", "#2ecc71", "#e74c3c"])

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

# Simple ranking bar chart (Total Score only)
# Simple vertical ranking bar chart (Total Score only)
st.subheader("Rolls Counting")

rank_chart = alt.Chart(df).mark_bar().encode(
    y=alt.Y("Total Score:Q", title="Total Score"),
    x=alt.X("Player:N", sort="-y", title="Player"),
    color=alt.value("#3498db"),  # Keep it one color (blue)
    tooltip=["Player", "Total Score"]
).properties(
    width=600,
    height=400
)

# Display the ranking chart
st.altair_chart(rank_chart, use_container_width=True)

# Create three side-by-side text boxes
col1, col2, col3 = st.columns(3)

with col1:
    st.text_input("Box 1", "")

with col2:
    st.text_input("Box 2", "")

with col3:
    st.text_input("Box 3", "")



