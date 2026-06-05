from tkinter import *

root = Tk()
root.title("калькулятор")
root.geometry("340x350")  
root.resizable(False, False)

expression = ""
input_text = StringVar()

def btn_click(item): #чтоб кнопки добавляли символы в строку
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear(): #чтоб кнопка С очищала строку
    global expression
    expression = ""
    input_text.set("")

def btn_equal(): #чтоб кнопка = выполняла выраж и показывала рез
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Ошибка")
        expression = ""

Entry(root, textvariable=input_text, font=("Arial", 20), bd=5, justify="right").grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 1, 0 #шоб кнопки встали кудо надо 
for btn in buttons:
    if btn == 'C':
        cmd = btn_clear
    elif btn == '=':
        cmd = btn_equal
    else:
        cmd = lambda x=btn: btn_click(x)
        
    Button(root, text=btn, font=("Arial", 15), width=5, height=2, command=cmd).grid(row=row, column=col, padx=2, pady=2)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()