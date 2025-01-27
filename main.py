import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Diot")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.current_input = ""
        self.result = 0
        self.operator = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(
            self.root,
            font=("Arial", 20),
            justify="right",
            bd=10,
            bg="#ffffff",
            insertwidth=4,
        )
        self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4)  
        ]

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            if text == "=":
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 16),
                    command=self.calculate,
                    bg="#4CAF50",
                    fg="white",
                    padx=20,
                    pady=10
                )
                btn.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=5, pady=5)
            else:
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 16),
                    command=lambda t=text: self.button_click(t),
                    bg="#e0e0e0",
                    padx=20,
                    pady=10
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        if value == "C":
            self.clear()
        else:
            self.current_input += str(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_input)

    def clear(self):
        self.current_input = ""
        self.result = 0
        self.operator = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            if self.current_input:
                expression = self.current_input
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_input = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()