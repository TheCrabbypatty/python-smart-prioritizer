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

global due_weight
if "due_weight" not in st.session_state:
    st.session_state.due_weight = None

global difficulty_weight
if "difficulty_weight" not in st.session_state:
    st.session_state.difficulty_weight = None

global time_weight
if "time_weight" not in st.session_state:
    st.session_state.time_weight = None

global toggle
if "toggle" not in st.session_state:
    st.session_state.toggle = False

global display_num
if "display_num" not in st.session_state:
    st.session_state.toggle = 0

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
    if add_event and not name == "" and not time == 0:
        with open("memory.csv", "a", newline = "") as file:
            fieldnames = ["name", "time", "difficulty", "due_date"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            if file.tell == 0:
                writer.writeheader()
            writer.writerow({"name": name, "time": time, "difficulty": difficulty, "due_date": due_date})
        st.toast("Your event has been added", duration = 1, icon = "👈")

def change():
    st.session_state.toggle = True
    
def calculate_function():
    calc = st.button("Calculate Priority", width = "stretch", type = "primary", key = "calculate", on_click = change)
    with st.container(border = st.session_state.toggle, key = "container"):
        if calc:
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
                    priority_num = (st.session_state.difficulty_weight * int(row["difficulty"])) + (st.session_state.time_weight * int(row["time"])) - (st.session_state.due_weight * int(diff.days))
                    st.session_state.priority_list.append(priority_num)
                i = 0
                while i in range(st.session_state.display_num):
                    ...
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
            st.subheader("**Top Priorities for Today** 🏆")
            st.space("xxsmall")
            header_cols = st.columns([3, 2, 2, 3])
            with header_cols[0]:
                st.markdown("**📋 Task**")
                st.markdown(f"1. :blue-badge[{first_priority}]")
                st.markdown(f"2. :blue-badge[{second_priority}]")
                st.markdown(f"3. :blue-badge[{third_priority}]")
            with header_cols[1]:
                st.markdown("**⏳ Time**")
                st.markdown(f":orange-badge[{data[top1]["time"]} minutes]")
                st.markdown(f":orange-badge[{data[top2]["time"]} minutes]")
                st.markdown(f":orange-badge[{data[top3]["time"]} minutes]")
            with header_cols[2]:
                st.markdown("**🏔️ Difficulty**")
                st.markdown(f":red-badge[{data[top1]["difficulty"]}]")
                st.markdown(f":red-badge[{data[top2]["difficulty"]}]")
                st.markdown(f":red-badge[{data[top3]["difficulty"]}]")
            with header_cols[3]:
                st.markdown("**📅 Due**")
                st.markdown(f":primary-badge[{data[top1]["due_date"]}]")
                st.markdown(f":primary-badge[{data[top2]["due_date"]}]")
                st.markdown(f":primary-badge[{data[top3]["due_date"]}]")

def settings():
    with st.container(border = True):
        st.subheader("Settings ⚙️")
        st.segmented_control("**Theme** 🎨",options = ["Dark", "Light", "Ocean", "Warmth", "Forest", "Galaxy"], default = "Dark", required = True)
        st.session_state.due_weight = st.session = st.slider("Due date weight ⏰", min_value = -7, max_value = 7, value = 3, help = "The weight that you wish to put on the due date, the larger the value, the more impactful it is towards the priority value.")
        st.session_state.difficulty_weight = st.slider("Difficulty weight 😮‍💨", min_value = -7, max_value = 7, value = 3, help = "The weight that you wish to put on the difficulty, the larger the value, the more impactful it is towards the priority value.")
        st.session_state.time_weight = st.slider("Time weight ⏲️", min_value = -7, max_value = 7, value = 3, help = "The weight that you wish to put on the estimated time, the larger the value, the more impactful it is towards the priority value.")
        st.session_state.display_num = st.number_input("Priorities displayed 📌", min_value = 0, max_value = len(st.session_state.priority_list), value = len(st.session_state.priority_list), help = "The number of priorities displayed in the ranking of top priorities.")
        st.space("xxsmall")



def algorithm():
    top1 = 0
    max = st.session_state.priority_list[0]
    for i in range(len(st.session_state.priority_list)):
        if st.session_state.priority_list[i] > max:
            max = st.session_state.priority_list[i]
            top1 = i    
    st.session_state.priority_list[top1] = float("-inf")
    return top1

def task_box():
    with st.container(border = True):
        col1, col2 = st.columns([10,1])
        with col1:
            st.subheader("Your tasks ⌚")
        with col2:
            st.button("🗑️", type = "primary")
        st.space("xxsmall")
        with open("memory.csv", "r") as file:
            fieldnames = ["name","time", "difficulty", "due_date"]
            reader = csv.DictReader(file, fieldnames = fieldnames)
            for row in reader:
                col1, col2, col3, col4 = st.columns([1.5, 1.5, 1.5, 1.5])
                col1.markdown(f"📋 **Task:** :blue-badge[{row['name']}]")
                col2.markdown(f"⏳ **Time:** :orange-badge[{row['time']} minutes]")
                col3.markdown(f"🏔️ **Difficulty:** :red-badge[{row['difficulty']}]")
                col4.markdown(f"📅 **Due:** :primary-badge[{row['due_date']}]")


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
    task_box()
    st.space("xxsmall")
    calculate_function()
    st.space("xxsmall")
    settings()


                
if __name__ == "__main__":
    main()