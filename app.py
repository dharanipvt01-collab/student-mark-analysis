import streamlit as st

st.title("📊 Student Marks Analysis")

st.write(
    "This application calculates the total, average, highest, "
    "and lowest marks of students."
)

# Student marks
marks = [85, 72, 90, 65, 78, 88, 95, 60, 82, 75]

# Calculations
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

# Display marks
st.subheader("Student Marks")
st.write(marks)

# Display results
st.subheader("Analysis Results")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Marks", total)
    st.metric("Highest Mark", highest)

with col2:
    st.metric("Average Marks", average)
    st.metric("Lowest Mark", lowest)