import tkinter as tk
from tkinter import messagebox
import random

class QuestLog:
    def __init__(self, root):
        self.root = root
        self.root.title("QuestLog")
        self.hp, self.en_hp, self.lvl = 100, 50, 0
        self.monsters = [["Goblin", "🧌"], ["Skeleton", "💀"], ["Dragon", "🐲"]]

        # 1. Inputs for Age and Subject
        tk.Label(root, text="Age:").pack()
        self.age_in = tk.Entry(root); self.age_in.insert(0, "10"); self.age_in.pack()
        tk.Label(root, text="Subject:").pack()
        self.sub_in = tk.Entry(root); self.sub_in.insert(0, "Math"); self.sub_in.pack()
        
        # 2. Game Display (Monster, Stats, Question)
        self.img = tk.Label(root, text="🧌", font=("Arial", 60))
        self.img.pack()
        self.stats = tk.Label(root, text="", font=("Courier", 10))
        self.stats.pack()
        self.q_lbl = tk.Label(root, text="", font=("Arial", 12, "bold"), wraplength=300)
        self.q_lbl.pack(pady=10)
        
        # 3. Answer Box and Attack Button
        self.ans_in = tk.Entry(root, font=("Arial", 16)); self.ans_in.pack()
        tk.Button(root, text="ATTACK", command=self.battle, bg="#E94560", fg="white").pack(pady=10)
        
        self.ask()

    def ask(self):
        # Update HP display and get user settings
        sub, age = self.sub_in.get().lower(), int(self.age_in.get() or 10)
        self.stats.config(text=f"Hero HP: {self.hp} | Enemy HP: {self.en_hp}")
        
        # Determine if the question is Math or Text
        if sub == "math":
            limit = 10 if age < 10 else 50
            n1, n2 = random.randint(1, limit), random.randint(1, limit)
            self.goal, msg = str(n1 + n2), f"Solve: {n1} + {n2}"
        else:
            self.goal, msg = "TEXT", f"Explain {sub} (Age {age}):"
        
        self.q_lbl.config(text=msg)

    def battle(self):
        # Check the answer
        ans, age = self.ans_in.get().strip(), int(self.age_in.get() or 10)
        
        # Logic: Math must be exact. Text must meet a minimum length based on age.
        hit = (ans == self.goal) if self.goal != "TEXT" else (len(ans) > (5 if age < 10 else 15))
        
        if hit:
            self.en_hp -= 25 # You damage the enemy
            messagebox.showinfo("BATTLE", "DIRECT HIT! -25 Enemy HP")
        else:
            self.hp -= 20    # Enemy damages you
            messagebox.showwarning("BATTLE", "MISS! -20 Your HP")

        self.ans_in.delete(0, 'end')
        
        # Check Win/Loss conditions
        if self.en_hp <= 0: 
            self.win_lvl()
        elif self.hp <= 0: 
            messagebox.showerror("DEFEAT", "You fainted!"); self.root.destroy()
        else: 
            self.ask()

    def win_lvl(self):
        # Move to the next monster
        self.lvl += 1
        if self.lvl < 3:
            self.en_hp = 50 + (self.lvl * 20)
            self.img.config(text=self.monsters[self.lvl][1])
            messagebox.showinfo("VICTORY", f"Next Level: {self.monsters[self.lvl][0]}")
            self.ask()
        else:
            messagebox.showinfo("CHAMPION", "You conquered the Dungeon!"); self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    QuestLog(root)
    root.mainloop()
