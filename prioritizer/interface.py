import streamlit as st  # type: ignore
import csv

global task_list
if "task_list" not in st.session_state:
    st.session_state.task_list = []

def l_interface():
    task = st.text_input("Task 📝", help = "The name of the task.")
    time = st.number_input("Estimated Time 🕞", min_value = 0, max_value = 1440, icon = "⌚", help = "The estimated time a task takes, in minutes.")
    return task, time

def r_interface():
    difficulty = st.slider("Difficulty 🏔️", min_value = 0, max_value = 5, help = "The difficulty of the task.")
    due_date = st.date_input("Due date 🗓️", format = "MM/DD/YYYY", help = "The due date of a task.")
    return difficulty, due_date

def button(name, time, difficulty, due_date):
    add_event = st.button("Add Event", width = "stretch")
    if add_event and not name == "":
        with open("memory.csv", "a", newline = "") as file:
            fieldnames = ["name", "time", "difficulty", "due_date"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            if file.tell == 0:
                writer.writeheader()
            writer.writerow({"name": name, "time": time, "difficulty": difficulty, "due_date": due_date})
        st.toast("Your event has been added", duration = 1, icon = "👈")
    


def main():
    st.title("Smart Prioritizer 🧠")
    col1, col2 = st.columns(2)
    with col1:
       na,ti = l_interface()
    with col2:
       di,da = r_interface()
    st.space("xxsmall")
    button(na,ti,di,da)
    st.space("small")
    with st.container(border = True):
        with open("memory.csv", "r") as file:
            fieldnames = ["name","time", "difficulty", "due_date"]
            reader = csv.DictReader(file, fieldnames = fieldnames)
            for row in reader:
                col1, col2, col3, col4 = st.columns([1.5, 1, 1, 1])
                col1.markdown(f"📋 **Task:** :blue-badge[{row['name']}]")
                col2.markdown(f"⏳ **Time:** :orange-badge[{row['time']}]")
                col3.markdown(f"🏔️ **Difficulty:** :red-badge[{row['difficulty']}]")
                col4.markdown(f"📅 **Due:** :primary-badge[{row['due_date']}]")
                

                
if __name__ == "__main__":
    main()