import streamlit as st  # type: ignore
import csv
import time
from datetime import date
from datetime import datetime

global task_list
if "task_list" not in st.session_state:
    st.session_state.task_list = []

global priority_list
if "priority_list" not in st.session_state:
    st.session_state.priority_list = []

if "show_border" not in st.session_state:
    st.session_state.show_border = False

def l_interface():
    task = st.text_input("Task 📝", help = "The name of the task.")
    time = st.number_input("Estimated Time 🕞", min_value = 0, max_value = 1440, icon = "⌚", help = "The estimated time a task takes, in minutes.")
    return task, time

def r_interface():
    difficulty = st.slider("Difficulty 🏔️", min_value = 0, max_value = 5, help = "The difficulty of the task.")
    due_date = st.date_input("Due date 🗓️", format = "MM/DD/YYYY", help = "The due date of a task.")
    return difficulty, due_date

def button(name, time, difficulty, due_date):
    add_event = st.button("Add Event", width = "stretch", key = "add")
    if add_event and not name == "":
        with open("memory.csv", "a", newline = "") as file:
            fieldnames = ["name", "time", "difficulty", "due_date"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            if file.tell == 0:
                writer.writeheader()
            writer.writerow({"name": name, "time": time, "difficulty": difficulty, "due_date": due_date})
        st.toast("Your event has been added", duration = 1, icon = "👈")
    
def calculate_function():
    calc = st.button("Calculate Priority", width = "stretch", type = "primary", key = "calculate")
    with st.container(border = st.session_state.show_border, key = "container"):
        if calc:
            st.session_state.show_border = True 
            with st.spinner("Calculating Numbers...", width = "stretch"):
                time.sleep(5)
            with open("memory.csv", "r") as file:
                fieldnames = ["name", "time", "difficulty", "due_date"]
                reader = csv.DictReader(file, fieldnames = fieldnames)
                st.session_state.priority_list = []
                for row in reader:
                    today = date.today()
                    d1 = datetime.strptime(row["due_date"], "%Y-%m-%d")
                    diff = d1.date() - today
                    priority_num = int(row["difficulty"]) + int(row["time"]) - int(diff.days)
                    st.session_state.priority_list.append(priority_num)
                top1 = algorithm()
                top2 = algorithm()
                top3 = algorithm()
            with open("memory.csv", "r") as file:
                fieldnames = ["name", "time", "difficulty", "due_date"]
                reader = csv.DictReader(file, fieldnames = fieldnames)
                data = list(reader)
                first_priority = data[top1]["name"]
                second_priority = data[top2]["name"]
                third_priority = data[top3]["name"]
            st.header("**Top Priorities for Today** 🏆")
            st.space("xxsmall")
            st.write(f"1. {first_priority}")
            st.write(f"2. {second_priority}")
            st.write(f"3. {third_priority}")

def algorithm():
    top1 = 0
    max = st.session_state.priority_list[0]
    for i in range(len(st.session_state.priority_list)):
        if st.session_state.priority_list[i] > max:
            max = st.session_state.priority_list[i]
            top1 = i    
    st.session_state.priority_list[top1] = float("-inf")
    return top1

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
                col1, col2, col3, col4 = st.columns([1.5, 1.5, 1.5, 1.5])
                col1.markdown(f"📋 **Task:** :blue-badge[{row['name']}]")
                col2.markdown(f"⏳ **Time:** :orange-badge[{row['time']} minutes]")
                col3.markdown(f"🏔️ **Difficulty:** :red-badge[{row['difficulty']}]")
                col4.markdown(f"📅 **Due:** :primary-badge[{row['due_date']}]")
    st.space("small")
    calculate_function()

                
if __name__ == "__main__":
    main()