import streamlit as st

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Prediction System")
st.write("Enter student details to view performance and recommendations.")

st.divider()
st.markdown("""
<style>
.stApp {
    background-color: #f0f5ff;
}
h1 {
    color: #173b70;
}
h2, h3 {
    color: #245b8f;
}
div.stButton > button {
    background-color: #1769aa;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #0d4778;
    color: white;
}
</style>
""", unsafe_allow_html=True)
student_name = st.text_input("Student Name")
attendance = st.number_input(
    "Attendance Percentage (%)",
    min_value=0.0, max_value=100.0, value=75.0
)
study_hours = st.number_input(
    "Daily Study Hours",
    min_value=0.0, max_value=24.0, value=2.0
)
previous_marks = st.number_input(
    "Previous Exam Marks",
    min_value=0.0, max_value=100.0, value=60.0
)

if st.button("Predict Performance"):
    if not student_name.strip():
        st.warning("Please enter the student name.")
    else:
        st.subheader("📊 Student Performance Report")
        st.write("**Student Name:**", student_name)
        st.write("**Attendance:**", f"{attendance}%")
        st.write("**Daily Study Hours:**", study_hours)
        st.write("**Previous Marks:**", previous_marks)

        if previous_marks >= 75 and attendance >= 75:
            st.success("Performance: Good")
            st.info("Recommendation: Practice advanced questions.")
        elif previous_marks >= 50:
            st.warning("Performance: Average")
            st.info("Recommendation: Revise lessons and practice daily.")
        else:
            st.error("Performance: Needs Improvement")
            st.info(
                "Recommendation: Follow a daily study plan "
                "and ask for teacher support."
            )
            st.divider()

st.subheader("📊 Student Performance Dashboard")

chart_data = {
    "Category": ["Attendance (%)", "Previous Marks (%)"],
    "Value": [attendance, previous_marks]
}

import pandas as pd
st.bar_chart(
    pd.DataFrame(chart_data).set_index("Category")
)

st.subheader("📚 Study Analysis")
if study_hours >= 3:
    st.write("Good study habit! Keep it up.")
else:
    st.write("Try to study at least 3 hours daily.")