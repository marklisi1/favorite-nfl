import tkinter as tk
import random

# List of 32 teams
teams = [f"Team {i}" for i in range(1, 33)]

# Dictionary to store team preferences
team_preferences = {team: 0 for team in teams}

class TeamPreferenceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Team Preference App")
        
        self.label = tk.Label(root, text="Choose your preferred team:")
        self.label.pack(pady=20)
        
        self.button1 = tk.Button(root, text="", command=self.choose_team1)
        self.button1.pack(side="left", padx=20)
        
        self.button2 = tk.Button(root, text="", command=self.choose_team2)
        self.button2.pack(side="right", padx=20)
        
        self.next_pairing()

    def next_pairing(self):
        self.pairing = random.sample(teams, 2)
        self.button1.config(text=self.pairing[0])
        self.button2.config(text=self.pairing[1])
        
    def choose_team1(self):
        self.update_preference(self.pairing[0])
        
    def choose_team2(self):
        self.update_preference(self.pairing[1])
        
    def update_preference(self, team):
        team_preferences[team] += 1
        self.next_pairing()
    
    def show_results(self):
        result_window = tk.Toplevel(self.root)
        result_window.title("Final Preferences")
        
        result_label = tk.Label(result_window, text="Final preferences:")
        result_label.pack(pady=10)
        
        for team, count in team_preferences.items():
            tk.Label(result_window, text=f"{team}: {count}").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = TeamPreferenceApp(root)
    root.protocol("WM_DELETE_WINDOW", app.show_results)
    root.mainloop()
