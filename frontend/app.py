import streamlit as st
import requests

st.set_page_config(
    page_title="PUSTI TUSTI",
    layout="wide"
)

st.title("🍱 PUSTI TUSTI")
st.subheader("AI-Powered Mid-Day Meal Monitoring System")

uploaded_file = st.file_uploader(
    "Upload Meal Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:

    st.image(uploaded_file, caption="Uploaded Image")

    if st.button("Analyze"):

        with st.spinner("Analyzing Meal & Student Data..."):

            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                files={
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type
                    )
                }
            )

            data = response.json()

            st.success("Analysis Completed ✅")

            # Student Details
            st.markdown("## 👤 Student Details")
            st.write(data['student'])

            # Detected Foods
            st.markdown("## 🍱 Detected Foods")
            st.write(data['foods'])

            # Nutrition
            st.markdown("## 🥗 Nutrition")
            st.write(data['nutrition'])

            # Attendance
            st.markdown("## ✅ Attendance")
            st.success("Attendance Marked Successfully")

            # Meal Allocation
            st.markdown("## 🍽️ Meal Allocation")

            if data["meal_allocated_today"] == "Yes":
                st.success("Meal Allocated for Today ✅")

            else:
                st.error("Meal Not Allocated ❌")

            st.balloons()