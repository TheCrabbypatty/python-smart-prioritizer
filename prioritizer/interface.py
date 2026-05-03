import streamlit as st

def l_interface():
    task = st.text_input("Task 📝", help = "The name of the task.")
    time = st.number_input("Estimated Time 🕞", min_value = 0, max_value = 1440, icon = "⌚", help = "The estimated time a task takes, in minutes.")

def r_interface():
    difficulty = st.slider("Difficulty 🏔️", min_value = 0, max_value = 5, help = "The difficulty of the task.")
    due_date = st.date_input("Due date 🗓️", format = "MM/DD/YYYY", help = "The due date of a task.")

def main():
    st.title("Smart Prioritizer 🧠")
    col1, col2 = st.columns(2)
    with col1:
        l_interface()
    with col2:
        r_interface()
    st.space("xxsmall")
    st.button("Add Event", width = "stretch")
    st.space("small")
    with st.container(border = True):
        ...



if __name__ == "__main__":
    main()