# python-smart-prioritizer

## Introduction
A small Python app built with Streamlit that helps you decide what to work on next by scoring and sorting tasks based on configurable criteria (e.g. difficulty, urgency, time required). It’s built to be simple to run and easy to tweak.

### Project Structure (The Core Parts)
- **prioritizer.py**: (Core logic for scoring and sorting task)
* **memory.csv**: (Helps store persistant task data) 
+ **config.toml**: (Configuration for themes)
- **README.md**:  (Instructions for the program)
* **requirements.txt**: (The file that contains the required libraries for this program)

### Requirements
* A usable computer that can browse
* Python 3.9+
* The libraries required

#### Libraries 
* Only the streamlit library is needed, all others additional functionality is built into python.

### Installation 
```
# Clone the repository
git clone https://github.com/<your-username>/python-smart-prioritizer.git
cd prioritizer/

# Install dependencies
pip install -r requirements.txt
```
### Task Format
In memory.csv, by default tasks look something like...
```
"Gym",45,3,2026-05-22
"Preformance",60,4,2012-11-23
"Soccer Game",120,4,2026-03-11
```
The first column represents the task name, for example the name for the first task is "Gym". The second column represents the estimates time it takes to complete the task (in minutes). In this case, our first task is estimated to take 45 minutes. The third column is the estimated difficulty of the task. This difficulty ranges from 0 (piece of cake) to 5 (hardest thing ever). For example in our first task, the difficulty is 3, so roughly in the middle. The fourth and final column represents the due date, written in the format YYYY-MM-DD. In this case, our first task is due on 2026-05-22

### Valid Inputs
For each of the inputs, we have a set range. For the task name, there is no restriction on how long the string can be, only it can't be empty. For the estimated time, anything above 1440 is not allowed, and anything below 0 is also not allowed (they also must be integers, so not floating points). For difficulty, it is also strictly integers within the range of 0 to 5 inclusive. And for date, the range is dependent on the day, based on streamlit requirements. 

### How it works
1. Loads task from memory.csv
2. Apply scoring formula using weights (in the settings page)
3. Sort tasks from highest to lowest score
4. Display results to UI

Priority = Weight1 * (estimated time) + Weight2 * (difficulty) - Weight3 * (days until due date)

### The settings page
The settings page controls the weights, and the number of tasks that are displayed in the rankings list. The weights are initally each set to 3, but each weight can be in the range of -7 to 7, inclusive (they also must be integers). And for how many are displayed, the default is max, but you can choose any integer as long as it is greater than 0. 

### License
This project is licensed under the MIT lisence see the LICENSE file for more details.


## Last Updated

<!-- TIMESTAMP_START -->
_Last updated: 2026-09-03 18:04 UTC_
<!-- TIMESTAMP_END -->
