import tkinter as tk
from tkinter import messagebox
from game_logic import gameplay
import random
import os

class SOSGui:
    def __init__(self, root, game_logic):
        self.root = root
        self.game_logic = game_logic
        self.buttons = []
        self.create_gui()

    def create_gui(self):
        self.root.title("SOS game")

        main_frame = tk.Frame(self.root, padx=10, pady=10, bg="gray")
        main_frame.pack(expand = True, fill=tk.BOTH)

        title_label = tk.Label(main_frame, text = "SOS", font=("Arial", 20, "bold"), bg ="gray")
        title_label.pack(pady=10)

        mode_size_frame = tk.Frame(main_frame, bg= "gray")
        mode_size_frame.pack(pady=10)


        #gamemode
        tk.Label(mode_size_frame, bg="lightgray").grid(row=0, column=0, sticky=tk.W)
        self.mode_var = tk.StringVar(value = "Simple")
        tk.Radiobutton(mode_size_frame, text="Simple Game", variable=self.mode_var, value = "Simple", bg="gray").grid(row=0, column=1, sticky=tk.W)
        tk.Radiobutton(mode_size_frame, text="General Game", variable=self.mode_var, value = "General", bg="gray").grid(row=0, column=2, sticky=tk.W)

        #board size
        tk.Label(mode_size_frame, text="Board size").grid(row=0, column=3, sticky=tk.W)
        self.size_entry = tk.Entry(mode_size_frame, width = 5)
        self.size_entry.grid(row=0, column=4)

        game_frame = tk.Frame(main_frame, bg="gray")
        game_frame.pack(fill=tk.BOTH, expand=True)
        game_frame.columnconfigure(0, weight=1) 
        game_frame.columnconfigure(1, weight=2)
        game_frame.columnconfigure(2, weight=1)

        # Left side - Blue player
        self.blue_frame = tk.Frame(game_frame, bg="gray")
        self.blue_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.create_player_options(self.blue_frame, "Blue player", "Blue")

        #Center - Grid
        self.grid_frame = tk.Frame(game_frame, bg="lightgrey")
        self.grid_frame.pack(side=tk.LEFT, padx=30, pady=10)

        #Right side - Red
        self.red_frame = tk.Frame(game_frame, bg="gray")
        self.red_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.create_player_options(self.red_frame, "Red player", "Red")

        #Control buttons frames
        control_frame = tk.Frame(main_frame, bg="gray")
        control_frame.pack(side=tk.BOTTOM, pady=10)

        #Tells what turn it is
        self.turn_label = tk.Label(main_frame, text=f"Current turn: {self.game_logic.current_turn}", bg="gray")
        self.turn_label.pack(side=tk.BOTTOM, pady=10)

        #buttons for new game
        tk.Button(control_frame, text="New Game", command=self.gameStart).pack(side=tk.LEFT, padx=5)

    def create_player_options(self, parent_frame, player_label, color):
        player_frame = tk.Frame(parent_frame, bg="gray")
        player_frame.pack(anchor=tk.W, pady=5)


        if color == "Blue":
            self.blue_choice = tk.StringVar(value="S")
            tk.Label(player_frame, text="Blue player", bg="gray").grid(row=2, column=0, pady=5)
            tk.Radiobutton(player_frame, text="S", variable=self.blue_choice, value="S", bg="gray").grid(row=2, column=1)
            tk.Radiobutton(player_frame, text="O", variable=self.blue_choice, value="O", bg="gray").grid(row=2, column=2)

        else:
            self.red_choice = tk.StringVar(value="S")  # Define red_choice properly!
            tk.Label(player_frame, text="Red player", bg="gray").grid(row=2, column=0, pady=5)
            tk.Radiobutton(player_frame, text="S", variable=self.red_choice, value="S", bg="gray").grid(row=2, column=1)
            tk.Radiobutton(player_frame, text="O", variable=self.red_choice, value="O", bg="gray").grid(row=2, column=2)


    def gameGrid(self, size):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.buttons = []
        for r in range(size):
            row = []
            for c in range(size):
                btn = tk.Button(self.grid_frame, text="", width=5, height=2,
                                font=("Arial", 12), command=lambda r=r, c=c: self.on_grid_click(r, c))
                btn.grid(row=r, column=c, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)
        self.grid_frame.pack()

    def on_grid_click(self, row, col):
        current_letter = self.blue_choice.get() if self.gameplay.current_turn == 'Blue' else self.red_choice.get()

        self.buttons[row][col].config(text=current_letter, state=tk.DISABLED)

        self.gameplay.switch_turn()
        self.update_turn_label()

    def gameStart(self):
        try:
            size_input = self.size_entry.get()
            size = int(size_input)
            if size < 3 or size > 10:
                raise ValueError("Size must be between 3 and 10")
            self.gameplay = gameplay(size, self.mode_var.get())
            self.gameGrid(size)
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))

    def update_turn_label(self):
        self.turn_label.config(text=f"Current turn: {self.gameplay.current_turn}")

if __name__ == "__main__":
    root = tk.Tk()
    game_logic = gameplay(3, "Simple")
    app = SOSGui(root, game_logic)
    root.mainloop()
        