import customtkinter as ctk
app = ctk.CTk()
app.title("Калькулятор")
app.geometry("400x400")
entry1 = ctk.CTkEntry(app, width=150, height=50,font=("Arial", 20), corner_radius=8)
entry2 = ctk.CTkEntry(app, width=150, height=50,font=("Arial", 20), corner_radius=8)
entry1.place(relx=0.25, rely=0.11, relwidth=0.4, relheight=0.13, anchor="center")
entry2.place(relx=0.75, rely=0.11, relwidth=0.4, relheight=0.13, anchor="center")
label = ctk.CTkLabel(app, text="", font=("Arial", 18))
label.place(relx=0.50, rely=0.24, anchor="center")
def set_operation(op):
    global current_operation
    current_operation = op
def dorivnye():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if current_operation == "+":
            res = a + b
        elif current_operation == "-":
            res = a - b
        elif current_operation == "*":
            res = a * b
        elif current_operation == "^":
            res = a ** b
        elif current_operation == "%":
            res = a % b
        elif current_operation == "/":
            if b == 0:
                label.configure(text="На 0 ділити не можна!")
                return
            res = a / b
        if res.is_integer():
            res = int(res)
        label.configure(text=f"Результат: {res}")
    except ValueError:
        label.configure(text="Введіть числа!")
    except Exception:
        label.configure(text="Помилка!")
def clear():
    global current_operation
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    current_operation = None
button_dodavannya = ctk.CTkButton(app, text="+",font=("Arial", 24), command=lambda: set_operation("+"), corner_radius=8)
button_dodavannya.place(relx=0.15, rely=0.40, relwidth=0.19, relheight=0.19, anchor="center")
button_vidnimannya = ctk.CTkButton(app, text="-", font=("Arial", 24), command=lambda: set_operation("-"),corner_radius=8)
button_vidnimannya.place(relx=0.41, rely=0.40, relwidth=0.19, relheight=0.19, anchor="center")
button_dobutok = ctk.CTkButton(app, text="*", font=("Arial", 24), command=lambda: set_operation("*"),corner_radius=8)
button_dobutok.place(relx=0.15, rely=0.63, relwidth=0.19, relheight=0.19, anchor="center")
button_dilennya = ctk.CTkButton(app, text="/", font=("Arial", 24), command=lambda: set_operation("/"),corner_radius=8)
button_dilennya.place(relx=0.41, rely=0.63, relwidth=0.19, relheight=0.19, anchor="center")
button_dorivnye = ctk.CTkButton(app, text="=",font=("Arial", 28),fg_color="#2c6e49",hover_color="#1e4a32",command=dorivnye,corner_radius=8)
button_dorivnye.place(relx=0.86,rely=0.76,relwidth=0.17,relheight=0.40,anchor="center")
button_stepin = ctk.CTkButton(app, text="^", font=("Arial", 24), command=lambda: set_operation("^"),corner_radius=8)
button_stepin.place(relx=0.15, rely=0.86, relwidth=0.19, relheight=0.19, anchor="center")
button_ostacha = ctk.CTkButton(app, text="%", font=("Arial", 24), command=lambda: set_operation("%"),corner_radius=8)
button_ostacha.place(relx=0.41, rely=0.86, relwidth=0.19, relheight=0.19, anchor="center")
button_clear = ctk.CTkButton(app, text="C", font=("Arial", 24),fg_color="#942a2a",hover_color="#6b1e1e",command=clear,corner_radius=8)
button_clear.place(relx=0.77, rely=0.40, relwidth=0.33, relheight=0.19, anchor="center")
app.mainloop()