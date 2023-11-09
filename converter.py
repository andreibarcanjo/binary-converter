import tkinter as tk

def decimal_para_binario():
    try:
        decimal_num = int(input_field.get())
        binary_num = bin(decimal_num).replace("0b","")
        output_label.config(text=f"Binary: {binary_num}")
    except ValueError:
        output_label.config(text="Texto invalido por favor coloque um número decimal")

def binario_para_decimal():
    try:
        binary_num = input_field.get()
        decimal_num = int(binary_num, 2)
        output_label.config(text=f"Decimal: {decimal_num}")
    except ValueError:
        output_label.config(text=f"Texto invalido por favor coloque um número binário")

def limpar():
    output_label.config(text="")

root = tk.Tk()
root.title("Binário-Decimal Converter")

menu_frame = tk.Frame(root)
menu_frame.pack()

