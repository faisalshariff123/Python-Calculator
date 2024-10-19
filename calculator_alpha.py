import tkinter as tk  # module
from tkinter import ttk



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        frame = Input(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

class Input(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=0, sticky="ew")

        #self.entry1.bind("<Return>", self.addition)

        self.entry_btn1 = ttk.Button(self, text="+", command=self.addition)
        self.entry_btn1.grid(row=0, column=1)

        self.entry_btn2 = ttk.Button(self, text="-", command=self.subtraction)
        self.entry_btn2.grid(row=0, column=2)

        self.entry_btn3 = ttk.Button(self, text="*", command=self.multiplication)
        self.entry_btn3.grid(row=2, column=2)

        self.entry_btn4 = ttk.Button(self, text="/", command=self.division)
        self.entry_btn4.grid(row=1, column=2)

        self.entry_btn5 = ttk.Button(self, text="Clear Answer Box", command=self.clear_list)
        self.entry_btn5.grid(row=0, column=3)

        self.entry_btn6 = ttk.Button(self, text="Clear Entry Box", command=self.clear_entry)
        self.entry_btn6.grid(row=1, column=3)

        self.answer = tk.Listbox(self)
        self.answer.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def addition(self, event=None):
        text = self.entry1.get()

        if text:
            try:

                numbers = map(float, text.split("+"))
                result = sum(numbers)
                self.answer.insert(tk.END, result)

            except ValueError:
                self.answer.insert(tk.END, "Invalid input. Please enter numbers separated by '+'.")

    def subtraction(self, event=None):
        text = self.entry1.get()

        if text:
            try:
                numbers = list(map(float, text.split("-")))

                result = numbers[0]
                for i in numbers[1:]:
                    result -= i

                self.answer.insert(tk.END, result)

            except ValueError:
                self.answer.insert(tk.END, "Invalid input. Please enter numbers separated by '-'.")

    def multiplication(self, event=None):
        text = self.entry1.get()

        if text:
            try:
                numbers = list(map(float, text.split("*")))

                result = numbers[0]
                for i in numbers[1:]:
                    result *= i

                self.answer.insert(tk.END, result)

            except ValueError:
                self.answer.insert(tk.END, "Invalid input. Please enter numbers separated by '*'.")

    def division(self, event=None):
        text = self.entry1.get()

        if text:
            try:
                numbers = list(map(float, text.split("/")))

                result = numbers[0]
                for i in numbers[1:]:
                    result /= i

                self.answer.insert(tk.END, result)

            except ValueError:
                self.answer.insert(tk.END, "Invalid input. Please enter numbers separated by '/'.")

    def clear_list(self, event=None):
        self.answer.delete(0, tk.END)

    def clear_entry(self, event=None):
        text = self.entry1.get()
        if text:
            self.entry1.delete(0, tk.END)


app = Application()
app.mainloop()
