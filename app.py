import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.configure(bg='black')
        self.maxsize(500, 600)
        self.geometry("+%d+%d" % ((self.winfo_screenwidth() - 500) // 2, (self.winfo_screenheight() - 600) // 2))

        # Configure the grid layout to resize columns and rows
        self.grid_columnconfigure(0, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        # Entry widget to display the numbers and results
        self.display = tk.Entry(self, width=25, font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for numbers and operations
        button_text = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        self.buttons = []
        for i in range(len(button_text)):
            button = tk.Button(self, text=button_text[i], width=5, height=2, font=('Arial', 15))
            button.grid(row=i//4+1, column=i%4, padx=5, pady=5)
            self.buttons.append(button)

        # Set up event handlers for buttons
        for button in self.buttons:
            button.bind('<Button-1>', self.button_click)

        # Clear button
        clear_button = tk.Button(self, text='C', width=5, height=2, font=('Arial', 15), command=self.clear_display)
        clear_button.grid(row=5, column=0, padx=5, pady=5)

        # Delete button
        delete_button = tk.Button(self, text='DEL', width=5, height=2, font=('Arial', 15), command=self.delete_char)
        delete_button.grid(row=5, column=1, padx=5, pady=5)

        # Evaluate button
        evaluate_button = tk.Button(self, text='=', width=5, height=2, font=('Arial', 15), command=self.evaluate)
        evaluate_button.grid(row=5, column=2, padx=5, pady=5)
        # Make buttons grow when window is resized
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
    def button_click(self, event):
        button_text = event.widget['text']
        self.display.insert(tk.END, button_text)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def delete_char(self):
        self.display.delete(len(self.display.get())-1, tk.END)

    def evaluate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "error")

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
