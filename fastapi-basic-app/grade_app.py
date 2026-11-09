
import streamlit as st
import pandas as pd

# --------------------------------
# 1. Page Configuration
# --------------------------------

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------
# 2. Application Title
# --------------------------------

st.title("🎓 Student Grade Manager")
st.write("Manage student marks and calculate grades.")

st.divider()

# --------------------------------
# 3. Initialize Session State
# --------------------------------

if "students" not in st.session_state:
    st.session_state.students = []

# --------------------------------
# 4. Grade Calculation Function
# --------------------------------

def calculate_grade(mark):

    if mark >= 90 and mark <= 100:
        return "A"

    elif mark >= 80 and mark < 90:
        return "B"

    elif mark >= 70 and mark < 80:
        return "C"

    elif mark >= 60 and mark < 70:
        return "D"

    else:
        return "E"

# --------------------------------
# 5. Add Student Form
# --------------------------------

st.header("Add Student Details")

with st.form("student_form"):

    student_name = st.text_input("Enter Student Name")

    student_mark = st.number_input(
        "Enter Student Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submit_button = st.form_submit_button("Add Student")

    if submit_button:

        if student_name.strip() == "":
            st.error("Please enter student name.")

        elif student_mark < 0 or student_mark > 100:
            st.error("Marks must be between 0 and 100.")

        else:

            student = {
                "Name": student_name.strip(),
                "Mark": student_mark,
                "Grade": calculate_grade(student_mark)
            }

            st.session_state.students.append(student)

            st.success(
                f"{student_name} added successfully!"
            )

# --------------------------------
# 6. Display Student Results
# --------------------------------

st.divider()

st.header("Student Results")

if len(st.session_state.students) > 0:

    df = pd.DataFrame(st.session_state.students)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------
    # 7. Calculate Class Statistics
    # --------------------------------

    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    average_mark = sum(marks) / len(marks)

    highest_mark = max(marks)

    lowest_mark = min(marks)

    # --------------------------------
    # 8. Display Class Performance
    # --------------------------------

    st.divider()

    st.header("Class Performance")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label="Class Average",
        value=f"{average_mark:.2f}"
    )

    col2.metric(
        label="Highest Mark",
        value=highest_mark
    )

    col3.metric(
        label="Lowest Mark",
        value=lowest_mark
    )

    # --------------------------------
    # 9. Clear Student Records
    # --------------------------------

    st.divider()

    if st.button("Clear All Student Records"):

        st.session_state.students = []

        st.rerun()

else:

    st.info(
        "No student records available. "
        "Please add student details."
    )

# --------------------------------
# 10. Application Footer
# --------------------------------

st.divider()

st.caption("Student Grade Manager | Developed using Python and Streamlit")
