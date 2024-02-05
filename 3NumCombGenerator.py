import tkinter as tk
from tkinter import ttk
from itertools import combinations

class CombinationGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Combination Generator")

        self.user_inputs = []

        # Styling with dark grey theme
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#708090")
        self.style.configure("TButton", background="#454545", foreground="#333")
        self.style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF")
        self.style.configure("TEntry", background="#454545", foreground="#333")

        # Main Frame
        self.main_frame = ttk.Frame(master, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Widgets
        self.label = ttk.Label(self.main_frame, text="Enter a number:")
        self.label.grid(row=0, column=0, pady=(0, 5), sticky=tk.W)

        self.entry = ttk.Entry(self.main_frame)
        self.entry.grid(row=1, column=0, pady=(0, 10), sticky=tk.W + tk.E)

        self.generate_button = ttk.Button(self.main_frame, text="Generate Combinations", command=self.generate_combinations)
        self.generate_button.grid(row=2, column=0, pady=(0, 10), sticky=tk.W + tk.E)

        self.result_text = tk.Text(self.main_frame, height=10, width=40)
        self.result_text.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

    def generate_combinations(self):
        user_input = self.entry.get()

        if user_input.lower() == 'done':
            self.display_combinations()
        else:
            try:
                number = int(user_input)
                self.user_inputs.append(number)
                self.result_text.insert(tk.END, f"{number} added\n")
            except ValueError:
                self.result_text.insert(tk.END, "Invalid input. Please enter a valid integer.\n")

        self.entry.delete(0, tk.END)

    def display_combinations(self):
        if len(self.user_inputs) < 3:
            self.result_text.insert(tk.END, "Insufficient numbers to generate combinations.\n")
        else:
            combinations_list = list(combinations(self.user_inputs, 3))
            count = len(combinations_list)
            self.result_text.insert(tk.END, f"Generated combinations ({count}):\n")
            for combination in combinations_list:
                self.result_text.insert(tk.END, f"{combination}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CombinationGeneratorApp(root)
    root.mainloop()
