import tkinter as tk

class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def number_entered(self, num):
        self.result = False
        first_num = txt_display.get()
        second_num = str(num)
        if self.input_value:
            self.current = second_num
            self.input_value = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txt_display.get())

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def display(self, value):
        txt_display.delete(0, tk.END)
        txt_display.insert(0, value)

root = tk.Tk()
root.title("Calculator")
calc = Calculator()

txt_display = tk.Entry(root, font=('arial', 20, 'bold'), bd=30, insertwidth=4, bg='powder blue', justify='right')
txt_display.grid(columnspan=4)

btn_7 = tk.Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='7', command=lambda: calc.number_entered(7))
btn_7.grid(row=1, column=0)

# Tambahkan tombol-tombol lainnya untuk angka dan operasi matematika

root.mainloop()
