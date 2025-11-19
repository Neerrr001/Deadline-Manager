import customtkinter as ctk
import json 
from datetime import datetime

#Load data
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
#Save data
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data,f)

#Calculate days left
def days_left(deadline):
    today= datetime.now().date()
    d = datetime.strptime(deadline, "%Y-%m-%d").date()
    return(d-today).days

#GUI
app = ctk.CTk()
app.geometry("600x400")
app.title("Deadline Tracker")

data = load_data()

#Display Saved Projects
for project in data:
    topic = project["topic"]
    deadline = project["deadline"]
    left= days_left(deadline)

    frame= ctk.CTkFrame(app, width = 300 , height = 80 , corner_radius=15)
    frame.pack(pady=15)

    ctk.CTkLabel(frame, text=topic , font=("Ariel", 16, "bold")).pack(pady=2)
    ctk.CTkLabel(frame, text= f"{left} days left" ).pack(pady=2)

#Add new project
topic_entry= ctk.CTkEntry(app, placeholder_text="Enter project topic")
topic_entry.pack(pady=5)

date_entry = ctk.CTkEntry(app, placeholder_text="Enter deadline (YYYY-MM-DD)")
date_entry.pack(pady=5)

def add_project():
    topic = topic_entry.get()
    deadline= date_entry.get()
    data.append({"topic" : topic , "deadline": deadline})
    save_data(data)
    app.destroy()
    #When you restrart, it will reload with the new project

ctk.CTkButton(app, text="Add Project", command=add_project).pack(pady=10)

app.mainloop()